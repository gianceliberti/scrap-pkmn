# import the required libraries
import requests
from bs4 import BeautifulSoup
 
target_url = 'https://scrapeme.live/shop/'
 
def pagination_scraper(url):
 
    response = requests.get(url, verify=False) 
    
    if response.status_code != 200:
 
        return f'status failed with {response.status_code}'
    else:
 
        # parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
 
        # obtain main product card
        product_card = soup.find_all('a', class_='woocommerce-loop-product__link')
 
        # iterate through product card to retrieve product names and prices
        for product in product_card:
            name_tag = product.find('h2', class_= 'woocommerce-loop-product__title')
 
            name = name_tag.text if name_tag else 'Name tag not found'
 
            price_tag = product.find('span', class_= 'price')
 
            price = price_tag.text if price_tag else 'Price tag not found'
 
            print(f'name: {name}, price: {price}')           
 
# set the initial page number to 1
page_count = 1
 
# scrape until the last page (1 to 48)
for next in range(1, 49):
 
    # get the new page number
    page_url = f'page/{page_count}'
 
    # append the incremented page number to the target URL
    full_url = target_url + page_url
 
    print(f'Scraping from: {full_url}')
 
    pagination_scraper(full_url)
 
    # increment the page number
    page_count += 1
