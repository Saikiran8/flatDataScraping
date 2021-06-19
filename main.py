from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import openpyxl

price =[]
perSqft = []
facing = []
address = []
area = []
status = []
floor = []
furnishing = []
ownership = []
noofBathroom = []
agent = []
postedAgo = []

driver = webdriver.Chrome("S:/sdev/Python Projects/chromedriver.exe")
driver.get("https://www.propertiesguru.com/residential-search/2bhk-residential_apartment_flat-for-sale-in-new_delhi")
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(1)
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(1)
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(1)

size = int(((driver.find_element_by_xpath("//*[@id='properties']/div/div[1]/h1")).text)[0:2]) #total no of results
for i in range(2,size+2):
    i = str(i)
    p = (driver.find_element_by_xpath("//*[@id='properties']/div/div["+i+"]/div[1]/div/div[2]/div/span[2]")).text
    price.append(p)
    ps = ((driver.find_element_by_xpath("//*[@id='properties']/div/div["+i+"]/div[1]/div/div[2]/div/span[3]")).text)[1:]
    perSqft.append(ps)
    fac = ((driver.find_element_by_xpath("//*[@id='properties']/div/div["+i+"]/div[2]/div[2]/div[1]/div[2]")).text).splitlines()[1]
    facing.append(fac)
    add = (driver.find_element_by_xpath("//*[@id='properties']/div/div["+i+"]/div[1]/div/div[1]/h1/span")).text
    address.append(add)
    ar = ((driver.find_element_by_xpath("//*[@id='properties']/div/div["+i+"]/div[2]/div[2]/div[1]/div[1]")).text)[5:]
    area.append(ar)
    stat = ((driver.find_element_by_xpath("//*[@id='properties']/div/div["+i+"]/div[2]/div[2]/div[1]/div[3]")).text).splitlines()[1]
    status.append(stat)
    flor = (driver.find_element_by_xpath("//*[@id='properties']/div/div["+i+"]/div[2]/div[2]/ul/li[1]")).text
    floor.append(flor)
    furnish = (driver.find_element_by_xpath("//*[@id='properties']/div/div["+i+"]/div[2]/div[2]/ul/li[2]")).text
    furnishing.append(furnish)
    owner = (driver.find_element_by_xpath("//*[@id='properties']/div/div["+i+"]/div[2]/div[2]/ul/li[3]")).text
    ownership.append(owner)
    noofBath = (driver.find_element_by_xpath("//*[@id='properties']/div/div["+i+"]/div[2]/div[2]/ul/li[4]")).text
    noofBathroom.append(noofBath)
    agen = ((driver.find_element_by_xpath("//*[@id='properties']/div/div["+i+"]/div[2]/div[2]/div[2]/div[2]/span[1]")).text)[:-7]
    agent.append(agen)
    postAgo = ((driver.find_element_by_xpath("//*[@id='properties']/div/div["+i+"]/div[2]/div[2]/div[2]/div[2]/span[2]")).text)[8:]
    postedAgo.append(postAgo)
# print(price)
# print(address)
# print(perSqft)
# print(area)
# print(facing)
# print(status)
# print(agent)
# print(floor)
# print(furnishing)
# print(ownership)
# print(postedAgo)
df = pd.DataFrame.from_dict({'Address':address,'Price':price,'Price/Sq.Ft':perSqft,'Area':area,'Facing':facing,'Status':status,'Floor':floor,"Furnishing Status":furnishing,"Ownership Type":ownership,"No.of Bathrooms":noofBathroom,'Agent':agent})
df.to_excel('FlatData.xlsx', header=True, index=False)