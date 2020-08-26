import requests
from bs4 import BeautifulSoup

request = requests.get("https://www.johnlewis.com/herman-miller-aeron-office-chair-graphite-polished-aluminium/p3177260")
content = request.content

soup = BeautifulSoup(content, "html.parser")

element = soup.find("p", {"class": "price price--large"})
# <p class="price price--large">£1,299.00</p>

string_price = element.text.strip() # "£1,299.00"

price_without_symbol = string_price[1:]

price = float(price_without_symbol.replace(',', ''))

if price < 200:
    print("You should buy the chair!")
    print("The current price is {}.".format(string_price))
else:
    print("Do not buy, it's too expensive!")
    print("The current price is {}.".format(string_price))