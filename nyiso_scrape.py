import requests
from bs4 import BeautifulSoup
import json

nyiso_url = "https://www.nyiso.com/o/oasis-rest/oasis/currentfuel/pie-data?1680007657720"
nyiso_response = requests.get(nyiso_url)
nyiso_html = nyiso_response.content
nyiso_soup = BeautifulSoup(nyiso_html,"html.parser")
site_json = json.loads(nyiso_soup.get_text())


for x in range(7):
    
  fuel = site_json["data"][x]
  fuel_type = fuel["fuelCategory"]
  fuel_amount = fuel["genMWh"]
  print(f"{fuel_type}: {fuel_amount} MW")



