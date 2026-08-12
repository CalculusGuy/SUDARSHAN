# crawler/crawler.py
import requests
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup

def crawl(target_url, max_pages=10):
    visited = set()
    to_visit = [target_url]
    pages = []
    forms = []

    while to_visit and len(pages) < max_pages:
        url = to_visit.pop(0)
        if url in visited:
            continue

        try:
            print(f"[*] Crawling: {url}")
            response = requests.get(url, timeout=5, verify=False)
            visited.add(url)

            if response.status_code == 200:
                pages.append(url)
                soup = BeautifulSoup(response.text, "html.parser")

                for link in soup.find_all("a", href=True):
                    href = link["href"]
                    full_url = urljoin(url, href)
                    if urlparse(full_url).netloc == urlparse(target_url).netloc:
                        if full_url not in visited and full_url not in to_visit:
                            to_visit.append(full_url)

                for form in soup.find_all("form"):
                    form_action = form.get("action", "")
                    form_method = form.get("method", "GET").upper()
                    form_inputs = []
                    for input_tag in form.find_all(["input", "textarea", "select"]):
                        input_name = input_tag.get("name")
                        if input_name:
                            form_inputs.append(input_name)
                    forms.append({
                        "action": urljoin(url, form_action),
                        "method": form_method,
                        "inputs": form_inputs
                    })
        except Exception as e:
            print(f"[!] Error crawling {url}: {e}")

    return pages, forms
