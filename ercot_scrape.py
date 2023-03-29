#Can't pull appropriate values

import requests
from bs4 import BeautifulSoup
import json

ercot_url = "https://www.ercot.com/api/1/services/read/dashboards/fuel-mix.json"
ercot_response = requests.get(ercot_url)
ercot_html = ercot_response.content
ercot_soup = BeautifulSoup(ercot_html,"html.parser")
site_json = json.loads(ercot_soup.get_text())

time_stamp = site_json["lastUpdated"]
time_stamp_date = time_stamp[0:10]
recent_pull = site_json["data"][time_stamp_date][time_stamp]

coal = "Coal and Lignite"
hydro = "Hydro"
nuclear = "Nuclear"
other = "Other"
storage = "Power Storage"
solar ="Solar"
wind = "Wind"
nat_gas = "Natural Gas"

fuel = ["Coal and Lignite","Hydro","Nuclear","Other","Power Storage","Solar","Wind","Natural Gas"]

for x in range(8):
    name = fuel[x]
    amount = recent_pull[name]["gen"]
    print(f"{name}: {amount} MW")

