from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import pandas as pd

url = 'https://www.residentevildatabase.com/personagens/'

options = Options()
options.add_argument("--headless=new") 

def config_driver():
  service = Service(ChromeDriverManager().install())
  driver = webdriver.Chrome(service=service, options=options)
  return driver

def open_page(url):
  driver = config_driver()
  #driver.maximize_window()
  driver.get(url)
  return driver

def close_driver(driver):
  driver.quit()

def get_basics_info(url):
  driver = open_page(url)
  try:
    driver.find_element(By.CLASS_NAME, "td-page-content")
  except:
    close_driver(driver)
    print(f"Error: Could not find the element with class 'td-page-content' in {url}")
    return {}
  div_container = driver.find_element(By.CLASS_NAME, "td-page-content")
  if div_container is None:
    close_driver(driver)
    return {}
  p = div_container.find_elements(By.TAG_NAME, "p")
  texto = p[1].text.split("<br/>")
  data = {}
  for t in texto:
    for i in t.split('\n'):
      if ":" in i:
        key, value = i.split(":", 1)
        data[key.strip()] = value.strip()
  close_driver(driver)
  return data

def get_links(url):
  driver = open_page(url)
  try:
    div_container = driver.find_element(By.CLASS_NAME, "td-page-content")
  except:
    close_driver(driver)
    return []
  if div_container is None:
    close_driver(driver)
    return []
  a = div_container.find_elements(By.TAG_NAME, "a")
  links = []
  for i in a:
    links.append(i.get_attribute("href"))
  close_driver(driver)
  return links

def get_characters_data(url):
  links = get_links(url)
  database = []
  for link in links:
    data = get_basics_info(link)
    database.append(data)
  return database

def transform_data(database):
  df = pd.DataFrame(database)
  return df

def save_to_parquet(df, filename):
  df.to_parquet(filename, index=False)

database = get_characters_data(url)
df = transform_data(database)
save_to_parquet(df, "resident_evil_characters.parquet")
