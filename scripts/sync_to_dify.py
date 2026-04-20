import os
import sys
import time
import requests
import frontmatter
from pathlib import Path

DIFY_API_KEY    = os.environ["DIFY_API_KEY"]
DIFY_DATASET_ID = os.environ["DIFY_DATASET_ID"]
BASE_URL        = "https://api.dify.ai/v1"
CONTENT_DIR     = Path("content")
SITE_URL        = "https://asgersh.github.io/Portfolio"

HEADERS = {"Authorization": f"Bearer {DIFY_API_KEY}"}

REQUEST_DELAY   = 5   # seconds between normal requests
MAX_RETRIES     = 6
RETRY_BASE      = 30  # seconds; doubles each retry


def request_with_retry(method: str, url: str, **kwargs):
    for attempt in range(MAX_RETRIES):
        r = requests.request(method, url, **kwargs)
        if r.status_code in (429, 403) and attempt < MAX_RETRIES - 1:
            wait = RETRY_BASE * (2 ** attempt)
            print(f"  rate limited ({r.status_code}), waiting {wait}s before retry {attempt + 1}/{MAX_RETRIES - 1}...")
            time.sleep(wait)
            continue
        r.raise_for_status()
        return r
    r.raise_for_status()
    return r


def url_for(path: Path) -> str:
    parts = path.with_suffix("").parts[1:]  # strip 'content'
    slug = "/".join(p for p in parts if p != "_index")
    return f"{SITE_URL}/{slug}/"


def parse_content() -> list[dict]:
    docs = []
    for md_file in sorted(CONTENT_DIR.rglob("*.md")):
        post = frontmatter.load(md_file)
        title = post.get("title", md_file.stem)
        body  = post.content.strip()

        if not body:
            continue

        page_url = url_for(md_file)
        relative = str(md_file.relative_to(CONTENT_DIR))
        text = f"Page: {title}\nDirect link (use this exact URL, do not modify): {page_url}\n\n{body}"

        docs.append({"name": title, "text": text})
    return docs


def list_existing() -> list[dict]:
    r = request_with_retry(
        "GET",
        f"{BASE_URL}/datasets/{DIFY_DATASET_ID}/documents",
        headers=HEADERS,
        params={"limit": 100},
    )
    return r.json().get("data", [])


def delete_doc(doc_id: str):
    request_with_retry(
        "DELETE",
        f"{BASE_URL}/datasets/{DIFY_DATASET_ID}/documents/{doc_id}",
        headers=HEADERS,
    )


def upload_doc(name: str, text: str):
    payload = {
        "name": name,
        "text": text,
        "indexing_technique": "high_quality",
        "process_rule": {"mode": "automatic"},
    }
    r = request_with_retry(
        "POST",
        f"{BASE_URL}/datasets/{DIFY_DATASET_ID}/document/create_by_text",
        headers=HEADERS,
        json=payload,
    )
    return r.json()


def sync():
    print("--- Dify Portfolio Sync ---")

    existing = list_existing()
    print(f"Deleting {len(existing)} existing documents...")
    for doc in existing:
        delete_doc(doc["id"])
        print(f"  deleted: {doc['name']}")
        time.sleep(REQUEST_DELAY)

    docs = parse_content()
    print(f"\nUploading {len(docs)} documents...")
    for doc in docs:
        upload_doc(doc["name"], doc["text"])
        print(f"  uploaded: {doc['name']}")
        time.sleep(REQUEST_DELAY)

    print(f"\nDone. {len(docs)} documents synced to Dify.")


if __name__ == "__main__":
    try:
        sync()
    except requests.HTTPError as e:
        print(f"API error: {e.response.status_code} {e.response.text}")
        sys.exit(1)
