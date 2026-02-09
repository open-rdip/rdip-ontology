import requests
import json
import os
import time
import re
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv("EMAIL")

def fetch_category_v3(source_type, target_count=100):
    """
    source_type: 'journal' or 'conference'
    """
    print(f"\n>>> TARGETING {target_count} {source_type.upper()} PAPERS...")
    base_url = "https://api.openalex.org/works"
    
    # SIGNIFICANTLY EXPANDED THEMES
    # These cover different "activity" markers in multidisciplinary research
    themes = [
        '(github OR gitlab) AND "experimental results"',
        '(github OR gitlab) AND "source code" AND evaluation',
        '(github OR gitlab) AND "benchmark" AND dataset',
        'github AND "proposed framework" AND architecture',
        'github AND "reproducible" AND "validation"',
        'github AND "prototype" AND "implementation"',
        'github AND "open source" AND "methodology"',
        'github AND "empirical study" AND "performance"',
        'github AND "software tool" AND "case study"',
        'github AND "data availability" AND "experimental design"'
    ]
    
    collected = []
    seen_dois = set()

    for q in themes:
        if len(collected) >= target_count:
            break
            
        print(f"Searching {source_type} with theme: {q}")
        params = {
            'search': q,
            # Broadened year to 2018 to ensure high volume of peer-reviewed results
            'filter': f'primary_location.source.type:{source_type},type:article,has_fulltext:true,publication_year:>2018',
            'sort': 'cited_by_count:desc',
            'per_page': 100, 
            'mailto': EMAIL
        }

        try:
            response = requests.get(base_url, params=params)
            if response.status_code != 200:
                continue
            
            results = response.json().get('results', [])
            for work in results:
                doi = work.get('doi')
                if not doi or doi in seen_dois:
                    continue
                
                title = (work.get('title') or "").lower()
                # Strict exclusion of review/survey papers
                if any(x in title for x in ['survey', 'review', 'systematic', 'meta-analysis']):
                    continue
                
                # Check abstract for "active" repo mentions
                abstract_idx = work.get('abstract_inverted_index') or {}
                abstract_text = " ".join(abstract_idx.keys()).lower()
                
                # Broaden the pattern to find repos that might not use the literal ".com"
                repo_patterns = [r"github", r"gitlab", r"available at", r"code is", r"repository"]
                if any(re.search(p, abstract_text) for p in repo_patterns):
                    collected.append({
                        'title': work.get('title'),
                        'doi': doi,
                        'venue': work.get('primary_location', {}).get('source', {}).get('display_name', 'Unknown'),
                        'venue_type': source_type,
                        'year': work.get('publication_year'),
                        'citations': work.get('cited_by_count'),
                        'concepts': [c.get('display_name') for c in work.get('concepts', [])[:3]],
                        'pdf_url': work.get('best_oa_location', {}).get('pdf_url')
                    })
                    seen_dois.add(doi)
                
                if len(collected) >= target_count:
                    break
            
            time.sleep(0.5) 
        except Exception as e:
            print(f"Error: {e}")

    return collected

# --- Execution ---
file_path = '../data/gold_standard/gold_candidates.json'
os.makedirs(os.path.dirname(file_path), exist_ok=True)

# 1. Fetch 100 of each to ensure we have enough good candidates
# Creating buffer so that so that filtering later doesn't reduce count too much
journal_papers = fetch_category_v3('journal', target_count=100)
conference_papers = fetch_category_v3('conference', target_count=100)

# 3. Combine and Deduplicate
all_papers = journal_papers + conference_papers
unique_final = {p['doi']: p for p in all_papers}.values()

with open(file_path, 'w') as f:
    json.dump(list(unique_final), f, indent=4)

print(f"\nDONE! Final Count: {len(unique_final)}")
print(f"Journals: {len(journal_papers)} | Conferences: {len(conference_papers)}")
