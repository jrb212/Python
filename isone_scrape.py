import requests
from bs4 import BeautifulSoup
import json

isone_url = "https://www.iso-ne.com"
isone_response = requests.get(isone_url)
isone_html = isone_response.content
isone_soup = BeautifulSoup(isone_html, "html.parser")

isone_titles = isone_soup.find_all("td")
isone_titles = isone_titles[20:50]
length_list = len(isone_titles)

print("ISONE:")
for x in range(int(length_list/3)):
    y = x*3
    isone_title = isone_titles[y].get_text()
    isone_amount = isone_titles[y + 2].get_text()
    print(f"{isone_title}: {isone_amount}")
