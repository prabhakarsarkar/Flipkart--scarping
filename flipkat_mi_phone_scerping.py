# import requests,json,os
# from bs4 import BeautifulSoup
# from pprint import pprint

# def all_link():
# 	name_list=[]
# 	price_list=[]
# 	detailes=[]
# 	res=requests.get("https://www.flipkart.com/mobiles/mi~brand/pr?sid=tyy,4io&otracker=nmenu_sub_Electronics_0_Mi")
# 	soup=BeautifulSoup(res.text,"html.parser")
# 	# main = soup.find_all("a", class_="_2Xp0TH fyt9Eu")
# 	# print(main)
# 	main = soup.find("div", class_="_2zg3yZ")
# 	link = main.find_all("a", class_="_2Xp0TH")
# 	url_list=[]
# 	for i in link:
# 		a = i.get("href")
# 		url="https://www.flipkart.com"+a
# 		url_list.append(url)
# 	return url_list

# link=all_link()
# def all_mi_mobaile_details(link):
# 	for h in link:
# 		name_list=[]
# 		price_list=[]
# 		detailes=[]
# 		res=requests.get(h)
# 		soup=BeautifulSoup(res.text,"html.parser")
# 		name = soup.find_all("div",class_="_3wU53n")
# 		for i in name:
# 			mobiles_name=""
# 			mobiles=i.text
# 			for j in mobiles:
# 				if j!="(":
# 					mobiles_name+=j
# 				else:
# 					break
# 			name_list.append(mobiles_name)
# 		rate=soup.find_all("div",class_="_1vC4OE _2rQ-NK")
# 		for n in rate:
# 			price=n.text
# 			price_list.append(price)
# 		ra=soup.find_all("div",class_="_3ULzGw")
# 		for k in ra:
# 			ram=k.find_all("li",class_="tVe95H")
# 			RAM_list=[]
# 			dic={}
# 			for b in ram:
# 				RAM_list.append(b.text)
# 				dic["all_mi_mobaile_details"]=RAM_list
# 			detailes.append(dic)
# 		dic1={}
# 		for all1 in name_list:
# 			dic1["price"]=str(price_list[name_list.index(all1)])
# 			dic1["detailes"]=str(detailes[name_list.index(all1)])
# 			dic1["name"]=all1
# 			pprint(dic1)

# all_mi_mobaile_details(link)












import requests
import json
from os import path
from pprint import pprint
if path.exists("courses.json"):
    with open("courses.json","r") as file:
        data1=json.load(file)
        data=json.loads(data1)
        file.close
else:
    url="http://saral.navgurukul.org/api/courses"
    a=requests.get(url)
    with open('courses.json',"w") as file:
        b=json.dump(a.text,file)
    with open("courses.json","r") as file:
        data1=json.load(file)
        data=json.loads(data1)
        file.close

a=1
for i in data["availableCourses"]:
    print (a,"  ",i["name"])
    a+=1

user=int(input("give any number \n"))
id_=(data["availableCourses"][user-1]["id"])
print("\n")

if path.exists("exercises_"+str(id_)+".json"):
    with open("exercises_"+str(id_)+".json","r") as new_file:
        new_data1=json.load(new_file)
        new_data=json.loads(new_data1)
        new_file.close
else:
    new_data_url=requests.get("http://saral.navgurukul.org/api/courses/"+str(id_)+"/exercises")
    print(new_data_url.text)
    with open("exercises_"+str(id_)+".json","w") as new_file:
        z=json.dump(new_data_url.text,new_file)
        new_file.close
    with open("exercises_"+str(id_)+".json","r") as new_file:
        new_data1=json.load(new_file)
        new_data=json.loads(new_data1)
        new_file.close
        
a=1
for j in new_data["data"]:
    print(a,".")
    print(j["name"])
    print("          " ,j["childExercises"])
    print(j["parentExerciseId"])
    print(" ")
    a+=1

user=int(input("give input for slug"))
slug=(new_data["data"][user-1]["slug"])
print(slug)

slug_id_url="http://saral.navgurukul.org/api/courses/"+str(id_)+"75/exercise/getBySlug?slug="+slug
slug_id_data=requests.get(slug_id_url)
print(slug_id_data.text)