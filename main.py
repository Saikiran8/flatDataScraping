from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
from xlsxwriter import Workbook
import openpyxl

#2BHK
price =[]     #lists of all the data is created so as to store them and convert it into dataframes
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
driver = webdriver.Chrome("E:/Sai2/chromedriver.exe")  #webdriver path intimation
driver.get("https://www.propertiesguru.com/residential-search/2bhk-residential_apartment_flat-for-sale-in-new_delhi") #url to open
time.sleep(2)
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(1)
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(1)
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(2)
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
df2 = pd.DataFrame.from_dict({'Address':address,'Price':price,'Price/Sq.Ft':perSqft,'Area':area,'Facing':facing,'Status':status,'Floor':floor,"Furnishing Status":furnishing,"Ownership Type":ownership,"No.of Bathrooms":noofBathroom,'Agent':agent})
#3BHK
price.clear()    #clearing all lists from previous data inorder to reuse same lists.
perSqft.clear()
facing.clear()
address.clear()
area.clear()
status.clear()
floor.clear()
furnishing.clear()
ownership.clear()
noofBathroom.clear()
agent.clear()
postedAgo.clear()
driver = webdriver.Chrome("E:/Sai2/chromedriver.exe")
driver.get("https://www.propertiesguru.com/residential-search/2bhk-residential_apartment_flat-for-sale-in-new_delhi")
driver.find_element_by_xpath("//*[@id='navbarNavDropdown']/ul[1]/li[3]").click()
driver.find_element_by_xpath("//*[@id='navbarNavDropdown']/ul[1]/li[3]/ul/li/div/ul/li[2]/label").click() #deselecting 2
driver.find_element_by_xpath("//*[@id='navbarNavDropdown']/ul[1]/li[3]/ul/li/div/ul/li[3]/label").click() #selecting 3
time.sleep(2)
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(1)
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(1)
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(2)
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
df3 = pd.DataFrame.from_dict({'Address':address,'Price':price,'Price/Sq.Ft':perSqft,'Area':area,'Facing':facing,'Status':status,'Floor':floor,"Furnishing Status":furnishing,"Ownership Type":ownership,"No.of Bathrooms":noofBathroom,'Agent':agent})
#4bhk
price.clear()
perSqft.clear()
facing.clear()
address.clear()
area.clear()
status.clear()
floor.clear()
furnishing.clear()
ownership.clear()
noofBathroom.clear()
agent.clear()
postedAgo.clear()
driver = webdriver.Chrome("E:/Sai2/chromedriver.exe")
driver.get("https://www.propertiesguru.com/residential-search/2bhk-residential_apartment_flat-for-sale-in-new_delhi")
driver.find_element_by_xpath("//*[@id='navbarNavDropdown']/ul[1]/li[3]").click()
driver.find_element_by_xpath("//*[@id='navbarNavDropdown']/ul[1]/li[3]/ul/li/div/ul/li[2]/label").click() #deselecting 2
driver.find_element_by_xpath("//*[@id='navbarNavDropdown']/ul[1]/li[3]/ul/li/div/ul/li[4]/label").click() #selecting 4
time.sleep(2)
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(1)
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(1)
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(2)
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
df4 = pd.DataFrame.from_dict({'Address':address,'Price':price,'Price/Sq.Ft':perSqft,'Area':area,'Facing':facing,'Status':status,'Floor':floor,"Furnishing Status":furnishing,"Ownership Type":ownership,"No.of Bathrooms":noofBathroom,'Agent':agent})

write = pd.ExcelWriter('FlatData.xlsx', engine='xlsxwriter')
df2.to_excel(write, sheet_name='2BHK',index=False)
df3.to_excel(write, sheet_name='3BHK',index=False)
df4.to_excel(write, sheet_name='4BHK',index=False)
write.save()
time.sleep(10)
print("Done with Scraping!!")
driver.quit()