# crawler/crawler.py
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import time

# Disable SSL warnings globally
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def crawl(target_url, max_pages=10, timeout=5):
    """
    Crawl the target URL and return discovered pages and forms.
    All requests use verify=False to handle expired/self-signed certificates.
    """
    visited = set()
    pages = []
    forms = []
    to_visit = [target_url]
    
    while to_visit and len(pages) < max_pages:
        url = to_visit.pop(0)
        
        if url in visited:
            continue
        visited.add(url)
        
        try:
            # verify=False to handle SSL certificate issues
            response = requests.get(url, timeout=timeout, verify=False)
            response.raise_for_status()
            
            # Add to discovered pages
            pages.append(url)
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extract all links
            for link in soup.find_all('a', href=True):
                href = link.get('href')
                if href:
                    absolute_url = urljoin(url, href)
                    if absolute_url not in visited and is_same_domain(absolute_url, target_url):
                        to_visit.append(absolute_url)
            
            # Extract all forms
            for form in soup.find_all('form'):
                form_data = extract_form_data(form, url)
                if form_data:
                    forms.append(form_data)
                    
        except requests.exceptions.SSLError:
            # Skip SSL errors silently
            continue
        except requests.exceptions.Timeout:
            continue
        except Exception:
            continue
    
    return pages, forms


def extract_form_data(form, base_url):
    """
    Extract action, method, and input fields from a form.
    """
    action = form.get('action', '')
    if action:
        action = urljoin(base_url, action)
    else:
        action = base_url
    
    method = form.get('method', 'get').lower()
    
    inputs = []
    for input_tag in form.find_all('input'):
        name = input_tag.get('name')
        if name:
            input_type = input_tag.get('type', 'text')
            inputs.append({
                'name': name,
                'type': input_type
            })
    
    return {
        'action': action,
        'method': method,
        'inputs': inputs
    }


def is_same_domain(url, target_url):
    """
    Check if the URL belongs to the same domain as the target.
    """
    try:
        parsed_url = urlparse(url)
        parsed_target = urlparse(target_url)
        return parsed_url.netloc == parsed_target.netloc or parsed_url.netloc == ''
    except Exception:
        return False
