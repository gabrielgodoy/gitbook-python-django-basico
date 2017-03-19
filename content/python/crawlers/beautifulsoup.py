import pprint
from bs4 import BeautifulSoup  # Screen-scraping Library

# SSL Cert Verification
# Requests verifies SSL certificates for HTTPS requests, just like a web browser
# By default, SSL verification is enabled, and Requests will throw a SSLError if it's unable to verify the certificate
import requests  # Python HTTP for humans

requests.packages.urllib3.disable_warnings()  # Remove InsecureRequestWarning

where_site_url = 'http://wwwhere.io/p'  # Starts in page 1 results


def go_to_each_item_and_get_title(url):
    source_code = requests.get(url, verify=False)  # Disable SSL verification for HTTPS requests
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    if (soup.title):
        print(soup.title.string)  # Get title in each product page


def crawler(maxPages, url):
    page = 1
    while page < maxPages:
        source_code = requests.get(url + str(page))
        plain_text = source_code.text  # Get the text of the website
        soup = BeautifulSoup(plain_text, 'html.parser')  # Convert to a BeutifulSoup Object to manipulate
        links = soup.select('div.link-main > a:nth-of-type(1)')
        my_links = []
        for link in links:
            href = link.get('href')
            label = link.select('h2')[0].getText()
            new_dictionary = {
                'link': href,
                'label': label
            }
            my_links.append(new_dictionary)
            go_to_each_item_and_get_title(href)
        pp = pprint.PrettyPrinter(depth=3)
        pp.pprint(my_links)
        page += page


crawler(3, where_site_url)
