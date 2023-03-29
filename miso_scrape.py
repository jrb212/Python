#Finally tracked down API url, not even sure how I got there
#It has a json dictionary with variables of interest
#Converted the text to json and was able to pull what I needed
#weather api practice file was a big help

import requests
from bs4 import BeautifulSoup

import json
miso_url = "https://api.misoenergy.org/MISORTWDDataBroker/DataBrokerServices.asmx?messageType=getfuelmix&returnType=json"
miso_response = requests.get(miso_url)
miso_html = miso_response.content
miso_soup = BeautifulSoup(miso_html,"html.parser")
site_json = json.loads(miso_soup.get_text())

#print(miso_html)
fuel_list = site_json["Fuel"]["Type"]
for x in range(6):
    fuel = fuel_list[x]
    label = fuel["CATEGORY"]
    amount = fuel["ACT"]
    print(f"{label}: {amount} MW")



