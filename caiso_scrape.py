#Value's showing up as dashes, could NOT figure this out
#Did some investigating and stumbled onto the "Network" tab of the developer pane
#Found a file called 'stats.txt' that appears to be a json dictionary of ALL DATA pulled into the site
#Was able to mirror some code from MISO file to convert the text into JSON


import requests
from bs4 import BeautifulSoup
import json

caiso_url = "http://www.caiso.com/outlook/SP/stats.txt"
caiso_response = requests.get(caiso_url)
caiso_html = caiso_response.content
caiso_soup = BeautifulSoup(caiso_html,"html.parser")
site_json = json.loads(caiso_soup.get_text())

nuclear = site_json["currentNuclear"]
solar = site_json["currentSolar"]
wind = site_json["currentWind"]
system = site_json["CurrentSystemDemand"]
nat_gas = site_json["currentNaturalGas"]
coal = site_json["currentCoal"]
biogas = site_json["currentBiogas"]
geothermal = site_json["currentGeothermal"]
renewables = site_json["currentRenewables"]

print(f"System: {system}")
print(f"Renewables: {renewables}")
print(f"Natural Gas: {nat_gas}")
print(f"Nuclear: {nuclear}")
print(f"Solar: {solar}")
print(f"Wind: {wind}")
print(f"Coal: {coal}")
print(f"Biogas: {biogas}")
print(f"Geothermal: {geothermal}")
