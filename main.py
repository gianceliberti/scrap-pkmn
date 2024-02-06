import requests
from bs4 import BeautifulSoup
import pandas as pd
import os


current_directory = os.path.dirname(os.path.realpath(__file__))

# Define la URL base de la categoría de Pokémon
base_url = "https://scrapeme.live/product-category/pokemon/"

# Lista para almacenar los datos de todos los pokemones de todas las páginas
pokemon_list = []

# Ciclo para recorrer todas las páginas, hay que verificar como se muestra.
page_number = 1
while True:
    url = base_url + "page/" + str(page_number) + "/"
    #url = base_url + f"?page={page_number}"
    response = requests.get(url)
    if response.status_code != 200:
        break  # Salir del bucle si no hay más páginas o si hay un error
    
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

# Convertir la lista de datos de pokemones en un DataFrame de pandas
data = pd.DataFrame(pokemon_list)
# Guardar el DataFrame en un archivo CSV
csv_file_path = os.path.join(current_directory, "Pokemon-and-price.csv")
data.to_csv(csv_file_path, index=False)
print("¡Se han extraído y guardado todos los datos de los pokemones!")
