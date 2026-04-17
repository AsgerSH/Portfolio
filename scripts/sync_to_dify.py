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
        text = f"Page: {title}\nURL: {page_url}\n\n{body}"

        docs.append({"name": title, "text": text})
    return docs


def list_existing() -> list[dict]:
    r = requests.get(
        f"{BASE_URL}/datasets/{DIFY_DATASET_ID}/documents",
        headers=HEADERS,
        params={"limit": 100},
    )
    r.raise_for_status()
    return r.json().get("data", [])


def delete_doc(doc_id: str):
    r = requests.delete(
        f"{BASE_URL}/datasets/{DIFY_DATASET_ID}/documents/{doc_id}",
        headers=HEADERS,
    )
    r.raise_for_status()


def upload_doc(name: str, text: str):
    payload = {
        "name": name,
        "text": text,
        "indexing_technique": "high_quality",
        "process_rule": {"mode": "automatic"},
    }
    r = requests.post(
        f"{BASE_URL}/datasets/{DIFY_DATASET_ID}/document/create_by_text",
        headers=HEADERS,
        json=payload,
    )
    r.raise_for_status()
    return r.json()


def sync():
    print("--- Dify Portfolio Sync ---")

    existing = list_existing()
    print(f"Deleting {len(existing)} existing documents...")
    for doc in existing:
        delete_doc(doc["id"])
        print(f"  deleted: {doc['name']}")

    docs = parse_content()
    print(f"\nUploading {len(docs)} documents...")
    for doc in docs:
        upload_doc(doc["name"], doc["text"])
        print(f"  uploaded: {doc['name']}")
        time.sleep(2)

    print(f"\nDone. {len(docs)} documents synced to Dify.")


if __name__ == "__main__":
    try:
        sync()
    except requests.HTTPError as e:
        print(f"API error: {e.response.status_code} {e.response.text}")
        sys.exit(1)
