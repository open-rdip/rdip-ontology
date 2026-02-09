import json
import pandas as pd
import re
import os
from thefuzz import process, fuzz
import uuid

# --- CONFIGURATION ---
JSON_INPUT = './data/gold_standard/gold_candidates.json'
JSON_OUTPUT = './data/gold_standard/gold_candidates_ranked.json'
CORE_CSV = './data/rankings/core.csv' 
SCIMAGO_CSV = '..data/rankings/scimagojr.csv' 

def extract_acronym_from_text(text):
    """Finds acronyms like (EMNLP) or INFOCOMP in titles."""
    match = re.search(r'\b[A-Z]{3,10}\b', text)
    return match.group(0) if match else None

def load_rankings():
    # Load CORE: Standard comma separator
    core_df = pd.read_csv(CORE_CSV, encoding='utf-8')
    core_df['Acronym'] = core_df['Acronym'].astype(str).str.upper().str.strip()
    core_df['Title'] = core_df['Title'].astype(str).str.lower().str.strip()
    core_df['Rank'] = core_df['Rank'].astype(str).str.strip()
    
    # Load Scimago: Semicolon separator as seen in your snippet
    sjr_df = pd.read_csv(SCIMAGO_CSV, sep=';', encoding='utf-8', low_memory=False)
    sjr_df['Title'] = sjr_df['Title'].astype(str).str.replace('"', '').str.lower().str.strip()
    sjr_df['SJR Best Quartile'] = sjr_df['SJR Best Quartile'].astype(str).str.strip()
    
    return core_df, sjr_df

def get_rank_and_acronym(paper, core_df, sjr_df):
    venue = paper.get('venue', '')
    venue_type = paper.get('venue_type', '').lower()
    
    # --- CONFERENCE LOGIC ---
    if venue_type == 'conference':
        acronym = extract_acronym_from_text(venue)
        
        # 1. Try matching by extracted Acronym
        if acronym:
            match = core_df[core_df['Acronym'] == acronym]
            if not match.empty:
                val = match.iloc[0]['Rank']
                if val.lower() not in ['unranked', 'nan', 'null', '']:
                    return val, acronym

        # 2. Try Fuzzy Match by Title
        best_match = process.extractOne(venue.lower(), core_df['Title'], scorer=fuzz.token_set_ratio)
        if best_match and best_match[1] > 85:
            row = core_df.iloc[best_match[2]]
            val = str(row['Rank'])
            if val.lower() not in ['unranked', 'nan', 'null', '']:
                return val, row['Acronym']
                
    # --- JOURNAL LOGIC ---
    elif venue_type == 'journal':
        best_match = process.extractOne(venue.lower(), sjr_df['Title'], scorer=fuzz.token_set_ratio)
        if best_match and best_match[1] > 90:
            row = sjr_df.iloc[best_match[2]]
            val = str(row['SJR Best Quartile'])
            if val.lower() not in ['nan', 'null', '', 'unranked']:
                return val, None # Journals don't usually use acronyms in SJR

    return None, None

def main():
    if not os.path.exists(JSON_INPUT):
        print(f"Error: {JSON_INPUT} not found.")
        return

    core_df, sjr_df = load_rankings()
    
    with open(JSON_INPUT, 'r') as f:
        papers = json.load(f)

    ranked_papers = []

    for paper in papers:
        rank_val, acronym_val = get_rank_and_acronym(paper, core_df, sjr_df)
        
        # STRICTOR FILTER: Only keep if a valid rank was found
        if rank_val:
            paper['rank'] = rank_val
            if acronym_val:
                paper['acronym'] = acronym_val
            paper['pass'] = True
            ranked_papers.append(paper)
            paper['id'] = str(uuid.uuid4())

    with open(JSON_OUTPUT, 'w') as f:
        json.dump(ranked_papers, f, indent=4)
            
    print(f"Process Complete!")
    print(f"Original Count: {len(papers)}")
    print(f"Final Ranked/Included Count: {len(ranked_papers)}")
    print(f"Filtered out {len(papers) - len(ranked_papers)} unranked or unmatched papers.")

if __name__ == "__main__":
    main()
