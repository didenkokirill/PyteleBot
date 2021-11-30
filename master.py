import requests
from bs4 import BeautifulSoup


url = "https://bitinfocharts.com/ru/crypto-kurs/"


page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
print(page.status_code)


info_bank = []
with open("currency") as file:
    lines = file.readline()
    for i in range(int(lines)):
        a = file.readline()
        info_bank.append(soup.findAll("tr", id=f"tr_{int(a)}"))
print(info_bank)


