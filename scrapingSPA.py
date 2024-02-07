import requests
from bs4 import BeautifulSoup
import os
import pandas as pd

target_url = 'https://scrapingclub.com/exercise/list_infinite_scroll/'

current_directory = os.path.dirname(os.path.realpath(__file__))
data_list = [] 

def pagination_scraper(url):
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f'Status failed with {response.status_code}')
        return
    else:
        # parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
 
        # get the product containers
        product_containers = soup.find_all('div', class_ ='p-4')
 
        # iterate through the product containers and extract the product content
        for product in product_containers:
            name_tag = product.find('h4')
            price_tag = product.find('h5')
 
            name = name_tag.text.strip() if name_tag else ''
            price = price_tag.text.strip() if price_tag else ''
 
            data_list.append({"Name": name, "Price": price})

# scrape infinite scroll by intercepting the page numbers in the Network tab
for page in range(1, 7):
    requested_page_url = f'{target_url}?page={page}'  # Formatear la URL correctamente
    pagination_scraper(requested_page_url)

data = pd.DataFrame(data_list)
csv_file_path = os.path.join(current_directory, "name-and-prices.csv")
data.to_csv(csv_file_path, index=False)

print("¡Se han extraído y guardado todos los datos de los productos!")
