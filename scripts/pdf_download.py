import json
import os
import time
import cloudscraper
from tqdm import tqdm
from urllib.parse import urlparse

# --- CONFIGURATION ---
JSON_INPUT = '../data/gold_standard/gold_candidates_ranked.json'
SAVE_DIR = '../data/gold_standard/raw_pdfs'
TIMEOUT = 60 # Academic servers can be slow

os.makedirs(SAVE_DIR, exist_ok=True)

def download_corpus():
    with open(JSON_INPUT, 'r') as f:
        papers = json.load(f)

    # Initialize cloudscraper (bypasses TLS fingerprinting & Cloudflare)
    scraper = cloudscraper.create_scraper(
        browser={
            'browser': 'chrome',
            'platform': 'windows',
            'desktop': True
        }
    )

    print(f"Starting robust download of {len(papers)} papers...")
    failed_ids = []

    for paper in tqdm(papers, desc="Downloading PDFs"):
        paper_id = paper.get('id') or paper.get('doi', '').split('/')[-1]
        pdf_url = paper.get('pdf_url')
        
        if not pdf_url:
            failed_ids.append(f"{paper_id} (No URL)")
            continue

        file_path = os.path.join(SAVE_DIR, f"{paper_id}.pdf")

        # 1. Skip if file exists
        if os.path.exists(file_path):
            continue

        try:
            # 2. Add dynamic referer based on domain
            domain = urlparse(pdf_url).netloc
            scraper.headers.update({'Referer': f"https://{domain}/"})

            # 3. Perform the download
            response = scraper.get(pdf_url, timeout=TIMEOUT, stream=True)
            
            if response.status_code == 200:
                with open(file_path, 'wb') as f:
                    for chunk in response.iter_content(chunk_size=1024 * 1024): # 1MB chunks
                        if chunk:
                            f.write(chunk)
                # Polite delay to prevent IP bans
                time.sleep(2) 
            else:
                failed_ids.append(f"{paper_id} (HTTP {response.status_code})")
                time.sleep(5) # Back off if blocked
        
        except Exception as e:
            failed_ids.append(f"{paper_id} (Error: {str(e)})")
            time.sleep(5)

    # --- FINAL SUMMARY ---
    print("\n" + "="*30)
    print(f"REPORT: {len(papers) - len(failed_ids)} downloaded, {len(failed_ids)} failed.")
    if failed_ids:
        print("FAILED IDS (Needs manual download):")
        for fid in failed_ids:
            print(f" - {fid}")
    print("="*30)

if __name__ == "__main__":
    download_corpus()
