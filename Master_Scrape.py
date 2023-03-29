import requests
from bs4 import BeautifulSoup
import json

print("Please choose an ISO from the list: ")
print("CAISO")
print("ERCOT")
print("ISONE")
print("MISO")
print("NYISO")
print("PJM")
user_input = input().lower()


def miso():
    miso_url = "https://api.misoenergy.org/MISORTWDDataBroker/DataBrokerServices.asmx?messageType=getfuelmix" \
               "&returnType=json"
    miso_response = requests.get(miso_url)
    miso_html = miso_response.content
    miso_soup = BeautifulSoup(miso_html, "html.parser")
    site_json = json.loads(miso_soup.get_text())

    # print(miso_html)
    fuel_list = site_json["Fuel"]["Type"]
    for x in range(6):
        fuel = fuel_list[x]
        label = fuel["CATEGORY"]
        amount = fuel["ACT"]
        print(f"{label}: {amount} MW")


def caiso():
    caiso_url = "http://www.caiso.com/outlook/SP/stats.txt"
    caiso_response = requests.get(caiso_url)
    caiso_html = caiso_response.content
    caiso_soup = BeautifulSoup(caiso_html, "html.parser")
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

    print(f"System: {system} MW")
    print(f"Renewables: {renewables} MW")
    print(f"Natural Gas: {nat_gas} MW")
    print(f"Nuclear: {nuclear} MW")
    print(f"Solar: {solar} MW")
    print(f"Wind: {wind} MW")
    print(f"Coal: {coal} MW")
    print(f"Biogas: {biogas} MW")
    print(f"Geothermal: {geothermal} MW")


def isone():

    isone_url = "https://www.iso-ne.com"
    isone_response = requests.get(isone_url)
    isone_html = isone_response.content
    isone_soup = BeautifulSoup(isone_html, "html.parser")

    isone_titles = isone_soup.find_all("td")
    isone_titles = isone_titles[20:50]
    length_list = len(isone_titles)

    print("ISONE:")
    for x in range(int(length_list / 3)):
        y = x * 3
        isone_title = isone_titles[y].get_text()
        isone_amount = isone_titles[y + 2].get_text()
        print(f"{isone_title}: {isone_amount}")


def ercot():
    ercot_url = "https://www.ercot.com/api/1/services/read/dashboards/fuel-mix.json"
    ercot_response = requests.get(ercot_url)
    ercot_html = ercot_response.content
    ercot_soup = BeautifulSoup(ercot_html, "html.parser")
    site_json = json.loads(ercot_soup.get_text())

    time_stamp = site_json["lastUpdated"]
    time_stamp_date = time_stamp[0:10]
    recent_pull = site_json["data"][time_stamp_date][time_stamp]

    fuel = ["Coal and Lignite", "Hydro", "Nuclear", "Other", "Power Storage", "Solar", "Wind", "Natural Gas"]

    for x in range(8):
        name = fuel[x]
        amount = recent_pull[name]["gen"]
        print(f"{name}: {amount} MW")


def nyiso():
    nyiso_url = "https://www.nyiso.com/o/oasis-rest/oasis/currentfuel/pie-data?1680007657720"
    nyiso_response = requests.get(nyiso_url)
    nyiso_html = nyiso_response.content
    nyiso_soup = BeautifulSoup(nyiso_html, "html.parser")
    site_json = json.loads(nyiso_soup.get_text())

    for x in range(7):
        fuel = site_json["data"][x]
        fuel_type = fuel["fuelCategory"]
        fuel_amount = fuel["genMWh"]
        print(f"{fuel_type}: {fuel_amount} MW")


def pjm():
    pjm_url = "https://pjm.com"
    pjm_response = requests.get(pjm_url)
    pjm_html = pjm_response.content
    pjm_soup = BeautifulSoup(pjm_html, "html.parser")

    renewables = pjm_soup.find_all("div", class_="container-gen-total")

    for renewable in renewables:
        title = renewable.find("div", class_="left")
        amount = renewable.find("div", class_="right")
        title = title.get_text()
        amount = amount.get_text()
        print(f"PJM {title} {amount}")  


while user_input != "exit":
   
    if user_input == "caiso":
        caiso()
       
    elif user_input == "ercot":
        ercot()
     
    elif user_input == "isone":
        isone()
      
    elif user_input == "miso":
        miso()
    
    elif user_input == "nyiso":
        nyiso()

    elif user_input == "pjm":
        pjm()
    user_input = input().lower()
