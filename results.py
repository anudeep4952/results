from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from time import sleep
from selenium.webdriver.common.keys import Keys

options=Options()
options.add_argument("--headless")
driver = webdriver.Firefox(firefox_options=options)
x3=801
lmain=[]
while(x3<=810):
 print("processing reg number ",x3,"\n")
 regnum="y16it"+str(x3)
 driver.get("http://rvrjcce.ac.in/examcell/results/regnoresults.php")
 sleep(1)
 x= driver.find_elements_by_tag_name("input")
 x[0].send_keys(regnum)
 x[1].click()
 sleep(1)
 #####################################################################
 lis1=[]
 td=driver.find_elements_by_tag_name("td")
 lis1.append(td[7].get_attribute("innerText"))
 i=8
 k=[]
 j=0
 while (i<len(td)):
   if (j > 12):
        j = 0
        u=k.pop(0)
        k.insert(0,u)
        lis1.append(k)
        k=[]
   k.append(td[i].get_attribute("innerText"))
   i=i+1
   j=j+1
 if(len(k)>0):
  u=k.pop(0)
  u="sem: "+u
  k.insert(0,u)
  lis1.append(k)
  k=[]
 lmain.append([lis1,x3])
 x3=x3+1
   #####################################################################
n=int(input("enter regnum"))
for i in lmain:
     if(n==i[1]):
         for j in i[0]:
             print(j,"\n")
driver.quit()
print("Finished")
