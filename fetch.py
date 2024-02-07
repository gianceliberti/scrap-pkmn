import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

def fetch_pokemon_data(base_url):
    pokemon_list = []
    page_number = 1

    while True:
        url = f"{base_url}page/{page_number}/"
        response = requests.get(url)
        
        if response.status_code != 200:
            break
        
        soup = BeautifulSoup(response.text, "html.parser")
        main_wrapper = soup.find(id="main")
        get_pokemons = main_wrapper.find_all(class_="product")

        for pokemon in get_pokemons:
            pokemon_name = pokemon.find(class_="woocommerce-loop-product__title").text.strip()
            pokemon_price = pokemon.find(class_="price").text.strip()

            pokemon_data = {
                "Pokemon": pokemon_name,
                "Price": pokemon_price
            }

            pokemon_list.append(pokemon_data)

        page_number += 1

    return pokemon_list

def save_to_csv(data, file_path):
    data_frame = pd.DataFrame(data)
    data_frame.to_csv(file_path, index=False)

def main():
    current_directory = os.path.dirname(os.path.realpath(__file__))
    base_url = "https://scrapeme.live/product-category/pokemon/"
    csv_file_path = os.path.join(current_directory, "Pokemon-and-price.csv")

    pokemon_data = fetch_pokemon_data(base_url)
    save_to_csv(pokemon_data, csv_file_path)

    print("¡Se han extraído y guardado todos los datos de los pokemones!")

if __name__ == "__main__":
    main()
