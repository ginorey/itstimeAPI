from bs4 import BeautifulSoup as bs
import requests as r

# reads URL for fighterLinkParser
def url_reader(url):
    try:
        page = r.get(url, headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}, timeout=10)
    # if request fails:
        # we will print the url to be aware of it
        # we will skip that link and move on
    except r.exceptions.RequestException as i:
        print(f'URL: {url}', i)
        return None
    html = bs(page.content, "html.parser")
    return html