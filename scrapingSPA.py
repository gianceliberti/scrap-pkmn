# import the required libraries
import requests
from bs4 import BeautifulSoup
 
target_url = 'https://scrapingclub.com/exercise/list_infinite_scroll/'
 
def pagination_scraper(url):
 
    response = requests.get(url) 
    
    if response.status_code != 200:
        return f'status failed with {response.status_code}'
    else:
 
        # parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
 
        # get the product containers
        product_containers = soup.find_all('div', class_ ='p-4')
 
        # iterate through the product containers and extract the product content
        for product in product_containers:
            name_tag = product.find('h4')
            price_tag = product.find('h5')
 
            name = name_tag.text if name_tag else ''
            price = price_tag.text if price_tag else ''
 
            print(f'name: {name}, price: {price}')
 
# set an initial request count
request_count = 1
 
# scrape infinite scroll by intercepting the page numbers in the Network tab
for page in range(1, 7):
 
     # simulate the full URL format
    requested_page_url = f'{target_url}?page={request_count}'
 
    pagination_scraper(requested_page_url)
 
    # increment the request count
    request_count += 1
