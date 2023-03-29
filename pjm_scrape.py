import requests
from bs4 import BeautifulSoup

pjm_url = "https://pjm.com"
pjm_response = requests.get(pjm_url)
pjm_html = pjm_response.content
pjm_soup = BeautifulSoup(pjm_html, "html.parser")

renewables = pjm_soup.find_all("script")
print(renewables)
# renewables = pjm_soup.find_all("div", class_="container-gen-total")
#
# for renewable in renewables:
#     title = renewable.find("div", class_="left")
#     amount = renewable.find("div", class_="right")
#     title = title.get_text()
#     amount = amount.get_text()
#     print(f"PJM {title} {amount}")
