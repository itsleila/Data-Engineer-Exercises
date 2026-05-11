
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.letras.mus.br/roar/discografia/" 
response = requests.get(url)

def open_page(url):
  response = requests.get(url)
  return response

def get_infos(soup):
  data = []
  div_discografia = soup.findAll('div', class_='songList-header-content')
  for div in div_discografia:
    title = div.find('h1').text
    infos = div.find('div', class_='songList-header-info').text
    ano_lancamento = infos.split('•')[0].strip()
    tipo = infos.split('•')[1].strip()
    data.append({'title': title, 'ano_lancamento': ano_lancamento, 'tipo': tipo})

  return data

def get_discography(url):
  response = open_page(url)
  if response.status_code != 200:
    print(f"Error: Could not open the page {url}")
    return []
  soup = BeautifulSoup(response.content, 'html.parser')
  data = get_infos(soup)
  return data

def save_to_csv(data, filename):
  df = pd.DataFrame(data)
  df.to_csv(filename, index=False)


discography = get_discography(url)
save_to_csv(discography, 'roar_discography.csv')

