import requests
import os
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse, urlunparse
import html2text


def save_content_to_file(url, content, save_path, ext="md"):
    """
    Saves website content to a separate file named after the URL's path.

    :param url: The URL of the website.
    :param content: The content to be saved.
    :param save_path: The path to save the file.
    :param ext: The extension of the file.
    """
    parsed_url = urlparse(url)
    (host, path) = [getattr(parsed_url, name) for name in ['hostname', 'path']]
    slug = '_'.join([seg for segs in [host.split('.'), path.split('/')] for seg in segs if seg])

    filename = f"{slug}.{ext}"
    if not filename:
        filename = f"catch_all.{ext}"

    # print(f"Saving content to {os.path.join(save_path, filename)}")
    with open(os.path.join(save_path, filename), "w", encoding='utf-8') as file:
        file.write(content)


def get_base_url(url):
    parsed_url = urlparse(url)
    return f"{parsed_url.scheme}://{parsed_url.netloc}"


def no_anchor_url(url):
    # Parse url to remove the fragment
    parsed_url = urlparse(url)
    # Recreate the URL without the fragment
    clean_url = urlunparse(parsed_url._replace(fragment=""))

    return clean_url


def valid_url(base_url, url, within_domain, visited):
    """Check if the URL is within the same domain (if required)"""
    # Resolve a relative URL
    resolved_url = urljoin(base_url, url)
    clean_url = no_anchor_url(resolved_url)

    result = (clean_url not in visited) and (not urlparse(clean_url).path.endswith("pdf")) and (
            not within_domain or clean_url.startswith(base_url))

    return result


def crawl_page(base_url, max_depth, converter, save_path, url, within_domain, visited=set(), depth=0):
    if depth > max_depth:
        return
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise an exception for bad status codes
        soup = BeautifulSoup(response.text, 'html.parser')
        markdown = converter.handle(str(soup)).replace("\n\n\n", "\n\n")
        print(f"scraped: {url}")

        save_content_to_file(url, f"> {url}\n\n{markdown}", save_path)

        clean_url = no_anchor_url(url)
        visited.add(clean_url)
        links = [urljoin(clean_url, no_anchor_url(tag['href'])) for tag in soup.find_all('a', href=True) if
                 valid_url(base_url, urljoin(clean_url, no_anchor_url(tag['href'])), within_domain, visited)]

        for link in links:
            crawl_page(base_url, max_depth, converter, save_path, link, within_domain, visited, depth + 1)

    except Exception as e:
        print(f"Failed to access {url}: {e}")


def crawl(url, max_depth=1, within_domain=True):
    # visited = set()
    converter = html2text.HTML2Text()
    converter.ignore_links = False
    base_url = get_base_url(url)
    print(f"Base URL: {base_url}")

    base_path = "crawled_text/"
    base_domain = urlparse(base_url).netloc.replace(".", "_")
    save_path = f"{base_path}{base_domain}/"

    # Create a directory to store the text files
    if not os.path.exists(base_path):
        os.mkdir(base_path)

    if not os.path.exists(save_path):
        os.mkdir(save_path)

    crawl_page(base_url, max_depth, converter, save_path, url, within_domain)

# Example of usage:
# crawl("http://example.com", max_depth=2, within_domain=True)