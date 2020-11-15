import requests
from bs4 import BeautifulSoup
//Get HTTP Request
req=requests.get("https://www.nykaa.com/nykaa-naturals-face-wash/p/863854?categoryId=8380&pps=1&productId=863854&ptype=product&skuId=790570")
//Get the content
cont=req.content
search=BeautifulSoup(cont,"html.parser")
//Extract the price
element=search.find("span",{"class" : "post-card__content-price-offer"})
value=element.text.strip()
original_price=float(value[1:])
//Verify whether the price is reasonable
if original_price<200:
    print("You can buy the product..The cost is {}".format(value))
else:
    print("You can not buy the product")
