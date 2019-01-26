from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from time import sleep
from selenium.webdriver.common.keys import Keys

options=Options()
options.add_argument("--headless")
driver = webdriver.Firefox(firefox_options=options)

regnum=input("reg number")
driver.get("http://rvrjcce.ac.in/examcell/results/regnoresults.php")
sleep(1)
x= driver.find_elements_by_tag_name("input")
x[0].send_keys(regnum)
x[1].click()
sleep(1)
 #####################################################################
lis1=[]
td=driver.find_elements_by_tag_name("td")
poi=[]
poi.append(td[7].get_attribute("innerText"))
lis1.append(poi)
i=8
k=[]
j=0
while (i<len(td)):
   if (j > 12):
        j = 0
        u=k.pop(0)
        u="sem: "+u
        k.insert(0,u)
        lis1.append(k)
        k=[]
   k.append(td[i].get_attribute("innerText"))
   i=i+1
   j=j+1
u=k.pop(0)
u="sem: "+u
k.insert(0,u)
lis1.append(k)
k=[]
   #####################################################################
s=""
for i in lis1:
    for k in i:
        for m in k:
          s=s+m+" "
    s=s+"\n"
driver.quit()
print("Finished")

for i in lis1:
 print(i)
v=input()
