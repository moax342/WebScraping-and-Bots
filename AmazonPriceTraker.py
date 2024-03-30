import requests
from bs4 import BeautifulSoup
import lxml

Url=("https://www.amazon.com/Fintie-Samsung-Multiple-Portfolio-Business/dp/B0CLV3FL43/ref=sr_1_1?"
     "crid=2PCVZD6NRJLL1&dib=eyJ2IjoiMSJ9.xaGy7f7XoFe3fN-XcZBLzVfRLp-oDJeA-Mz6Pqo1iPtMSer1T0J0eUbws_"
     "XkHCca9hiSIRqxhzPocUVYg8DjaGvBVk6cPSNsCpmTpPX_2synXacBnsZsiAQK8YhAqxeBiEy71_3jjfx1eA6Fm7ia6b2o9D562UvzWZN-"
     "L6acCSNXA1xWmo8WIXuMxhh6Eutj5nY6fioB5lKJtcMhSDyejnOPXyYfKByv6PAPri8r66g.WF6Ap7x6DYbfq1lz6D6aXHrx5_Di9RjWyfx_"
     "s3gxt2M&dib_tag=se&keywords=Galaxy+Tab+S9+FE+5G&qid=1711189080&sprefix=galaxy+tab+s9+fe+5g%2Caps%2C340&sr=8-1")

header={
     "User-Agent":" YOUR USER AGENT",
     "Accept-Language":"YOUR LANGUAGE"
}

response = requests.get(url=Url,headers=header)
price = response.text

price_is = BeautifulSoup(price,"lxml")

# getting the price from the web page
price_now =float(price_is.select_one("td span span").getText().split("$")[1])
print(price_now)