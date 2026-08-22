import requests
from scholarly import scholarly
import os
import time
import re

# --- Step 1: Author Scholar profiles ---
# Google Scholar's name-search endpoint (`scholarly.search_author`) gets
# redirected to a login page from most cloud/CI IPs, which makes it
# unreliable for automated runs. Direct profile lookup
# (`scholarly.search_author_id`) doesn't hit that block, so authors are
# identified by their Scholar user ID (the `user=` parameter in their
# profile URL) instead of by name.
AUTHORS = {
    "Jonathan Kua": "MCbG3NUAAAAJ",
    "Shiva Raj Pokhrel": "gESkh60AAAAJ",
}

# --- Step 2: Base Directory ---
BASE_DIR = "content/publication"
os.makedirs(BASE_DIR, exist_ok=True)

# --- Step 3: Fetch CrossRef Metadata ---
def fetch_crossref_metadata(title, retries=3, delay=5):
    url = f"https://api.crossref.org/works?query.bibliographic={title}&rows=1"
    for attempt in range(retries):
        try:
            response = requests.get(url, timeout=30)
            if response.status_code == 200:
                items = response.json().get('message', {}).get('items', [])
                if items:
                    item = items[0]
                    return {
                        "type": item.get("type", "unknown"),
                        "abstract": re.sub(r'<.*?>', '', item.get("abstract", "")).replace("\n", " ").strip(),
                        "doi": item.get("DOI", ""),
                        "publisher": item.get("publisher", ""),
                        "volume": item.get("volume", ""),
                        "issue": item.get("issue", ""),
                        "pages": item.get("page", ""),
                        "published": item.get("issued", {}).get("date-parts", [[2000]])[0][0]
                    }
            return None
        except requests.RequestException:
            if attempt < retries - 1:
                time.sleep(delay)
    return None

# --- Step 4: Categorize Paper ---
def categorize_paper(crossref_type):
    types = {
        'journal-article': ("2", "Journal Article"),
        'proceedings-article': ("1", "Conference Paper"),
        'posted-content': ("3", "Preprint"),
        'book': ("4", "Book"),
        'book-chapter': ("5", "Book Chapter"),
        'report': ("7", "Report"),
        'thesis': ("6", "Thesis"),
        'other': ("8", "Other")
    }
    return types.get(crossref_type, ("3", "Preprint"))

# --- Utilities ---
def clean_file_name(title):
    return title.replace(" ", "_").replace("/", "_").replace(":", "_")[:50]

def yaml_escape(value):
    """Escape a value for embedding inside a double-quoted YAML string."""
    return str(value).replace("\\", "\\\\").replace('"', '\\"')

# --- Step 5: Process Publications ---
for author_name, scholar_id in AUTHORS.items():
    print(f"\n🔍 Fetching profile: {author_name} ({scholar_id})")
    try:
        author = scholarly.search_author_id(scholar_id)
        author = scholarly.fill(author, sections=["publications"])
    except Exception as e:
        print(f"❌ Could not load '{author_name}' ({scholar_id}): {e}. Skipping...")
        continue

    author_folder = os.path.join(BASE_DIR, author_name.replace(" ", "_").lower())
    os.makedirs(author_folder, exist_ok=True)

    # Scoped per author (not shared across authors) so a paper co-authored by
    # both people in AUTHORS still gets saved into each of their folders.
    processed_titles = set()

    for pub in author['publications']:
        try:
            scholarly.fill(pub)
        except Exception as e:
            print(f"⚠️  Could not load publication details, skipping: {e}")
            continue

        title = pub.get('bib', {}).get('title', 'Untitled Paper')
        # Filled Scholar entries join authors with " and " (e.g. "A and B and
        # C"), never commas.
        authors_raw = pub.get('bib', {}).get('author', author_name)
        # `venue` is never present on a filled Scholar entry; the real field
        # is `journal`, with the raw `citation` string as a fallback.
        publication = (
            pub.get('bib', {}).get('journal')
            or pub.get('bib', {}).get('citation')
            or 'N/A'
        )
        cited_by = pub.get('num_citations', 0)
        tags = pub.get('bib', {}).get('keywords', '').split(",")
        link = pub.get('pub_url', '')

        if not title or title in processed_titles:
            continue

        crossref = fetch_crossref_metadata(title)
        if not crossref:
            year = pub.get('bib', {}).get('pub_year', '2000')
            abstract = pub.get('bib', {}).get('abstract', '')
            publisher = pub.get('bib', {}).get('publisher', '')
            doi = ''
        else:
            year = str(crossref.get("published", "2000"))
            abstract = crossref.get("abstract") or pub.get('bib', {}).get('abstract', '')
            publisher = crossref.get("publisher") or pub.get('bib', {}).get('publisher', '')
            doi = crossref.get("doi", "")

        try:
            year_int = int(year)
            formatted_date = f"{year_int}-01-01"
        except Exception:
            formatted_date = "2000-01-01"

        pub_type_code, pub_type_label = categorize_paper(crossref.get("type", "other") if crossref else "other")

        safe_title = clean_file_name(title)
        folder_path = os.path.join(author_folder, safe_title)
        os.makedirs(folder_path, exist_ok=True)
        file_path = os.path.join(folder_path, "index.md")

        authors_list = [a.strip() for a in authors_raw.split(" and ")]
        authors_yaml = "\n  - " + "\n  - ".join(authors_list)

        paper_data = f"""---
title: "{yaml_escape(title)}"
authors:{authors_yaml}
year: "{year}"
date: "{formatted_date}"
publication_types: ["{pub_type_code}"]  # {pub_type_label}
publication_type_label: "{pub_type_label}"
publication: "{yaml_escape(publication)}"
publisher: "{yaml_escape(publisher)}"
doi: "{yaml_escape(doi)}"
abstract: "{yaml_escape(abstract)}"
cited_by: "{cited_by}"
tags:
  - {", ".join(f'"{yaml_escape(tag.strip())}"' for tag in tags if tag.strip())}

url_pdf: "{yaml_escape(link)}"
url_code: ""
url_dataset: ""
url_poster: ""
url_project: ""
url_slides: ""
url_source: ""
image:
  caption: ""
  focal_point: ""
  preview_only: false
projects: []
slides: ""
---
"""

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(paper_data)

        processed_titles.add(title)
        print(f"📄 Saved: {file_path}")

print("\n✅ All publications have been processed and saved.")
