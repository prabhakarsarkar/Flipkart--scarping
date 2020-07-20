import requests
from pprint import pprint
from  bs4 import BeautifulSoup

def mobile_delails():
	res=requests.get("https://www.flipkart.com/redmi-8-sapphire-blue-64-gb/p/itme9614ba9b9bda?pid=MOBFKPYDENDXZZ7U&lid=LSTMOBFKPYDENDXZZ7U5KFCKA&marketplace=FLIPKART&srno=b_1_1&otracker=nmenu_sub_Electronics_0_Mi&fm=organic&iid=cd3e6da8-9b8b-4251-baed-dd461ff1d7fb.MOBFKPYDENDXZZ7U.SEARCH&ppt=browse&ppn=browse&ssid=s0pfsus4ps0000001579495830409")
	soup=BeautifulSoup(res.text,"html.parser")
	mobile=soup.find("span",class_="_35KyD6").text
	mobile_name=mobile[0:8]
	print(mobile_name)
	rate=soup.find("div",class_="_1uv9Cb").div.text
	print(rate)
	# mobile_image=soup.find("div",class_="_3BTv9X _3iN4zu",style="height:inherit;width:inherit").img.text
	# print(mobile_image)
	mobile_delails=soup.find_all("li",class_="_2-riNZ")
	for i in mobile_delails:
		print(i.div.text)
mobile_delails()
