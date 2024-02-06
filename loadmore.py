# import the required libraries
import requests
 
ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
 
xhr_api_base_url = 'https://www.3m.com.au/snaps2/api/pcp-show-next/'
 
target_url = 'https://www.3m.com.au/3M/en_AU/p/c/medical'
 
full_api_endpoint = xhr_api_base_url + target_url
 
# specify data size to query per request
data_size = 51
 
def pagination_scraper(api_endpoint):
 
    headers = {'User-Agent': ua}
 
    # make request and pass in the user agent headers
    response = requests.get(api_endpoint, headers=headers)
 
    # validate your request
    if response.status_code != 200:
        print(f'status failed with {response.status_code}')
 
    else:
        # load the items from the JSON response
        data = response.json()['items']  
 
        # extract data from the JSON response
        for product in data:
            product_name = product['name']
            image_url = product['imageUrl']
 
            print(f'name: {product_name}, image_url: {image_url}')
 
# set the maximum number of requests to make per execution
max_requests = 4
 
# ensure the requests doesn't exceed the number of requests 
for i in range(max_requests):
 
    # change the data size dynamically in URL
    dynamic_url = f'{full_api_endpoint}?size={data_size}&start=51'
 
    # increment the data size
    data_size += 51
 
    # run the scraper funcion on the dynamic URL
    pagination_scraper(dynamic_url)
