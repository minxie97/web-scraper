import requests
from bs4 import BeautifulSoup

URL_ONE = "https://en.wikipedia.org/wiki/Lunar_New_Year"
URL_TWO = "https://en.wikipedia.org/wiki/Seattle"

def get_citations(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    return soup.find_all("a", string="citation needed")

def get_citations_needed_count(url):
    results = get_citations(url)
    return len(results)

def get_citations_needed_report(url):
    results = get_citations(url)
    citation_string = ""
    for result in results:
        parent = result.find_parent("p")
        if parent:
            citation_string += f"{parent.text}\n"
    return citation_string

print(get_citations_needed_count(URL_ONE))
print(get_citations_needed_report(URL_ONE))

print(get_citations_needed_count(URL_TWO))
print(get_citations_needed_report(URL_TWO))