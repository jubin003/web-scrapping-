from selenium import webdriver
from selenium.webdriver.common.by import By
import re

browser = webdriver.Chrome(executable_path=r"C:\Users\Lenovo\Downloads\chromedriver_win32\chromedriver.exe")
URL1 = 'https://www.daraz.com.np/?spm=a2a0e.searchlistcategory.header.dhome.3c24160aCf3EvV'
URL2 ='https://www.sastodeal.com/'
#browser.get(URL1)
#browser.get(URL2)

#########APPLE PHONE URL FOR DAZAR###################
def get_url1(search_term):
    template = 'https://www.daraz.com.np/smartphones/{}/?spm=a2a0e.11779170.cate_1_1.4.2b102d2bP73Uof'
    search_term = search_term.replace(' ','+')
    return template.format(search_term)
url1= get_url1('apple')
browser.get(url1)

############### FOR TOTAL PRODUCTS######################
numofproducts_daraz= browser.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[1]/div/div[1]/div[1]/div/div[1]/div/div/span[1]').text
totoalpro_daraz= numofproducts_daraz.split(' ').pop(0)
print("Total number of products in Daraz are: ",int(totoalpro_daraz))
allprodetail= browser.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[1]/div/div[1]').text

############PRODUCT PRICE DARAZ#########
product_list=[]
i= 1
while (i<= int(totoalpro_daraz)):
    data=browser.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[1]/div/div[1]/div[3]/div['+str(i)+']/div/div/div[2]/div[3]/span').text
    product_list.append(data)
    i +=1
#print(product_list)
Only_price = []
for name in product_list:
  Only_price.append(name.split()[-1])

#### Change list str into int###
Only_price=[ sub.replace(',', '') for sub in Only_price]
Only_price = [float(y) for y in Only_price]
#print(Only_price)



#########PRODUCT NAME DARAZ##########
#/html/body/div[3]/div/div[2]/div[1]/div/div[1]/div[3]/div[1]/div/div/div[2]/div[2]/a
#/html/body/div[3]/div/div[2]/div[1]/div/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/a
productname_list=[]
a= 1
while (a<= int(totoalpro_daraz)):
    data_name_daraz=browser.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[1]/div/div[1]/div[3]/div['+str(a)+']/div/div/div[2]/div[2]/a').text
    productname_list.append(data_name_daraz)
    a +=1
#print(productname_list)

#product_price= browser.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[1]/div/div[1]/div[3]/div[1]/div/div/div[2]/div[3]/span').text
#product2_price= browser.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[1]/div/div[1]/div[3]/div[2]/div/div/div[2]/div[3]/span').text
#print(allprodetail)
#print(product_price)
#print(product2_price)
#print(url1)

res = {}
for key in productname_list:
    for value in Only_price:
        res[key] = value
        Only_price.remove(value)
        break
rex=res
print("All the rpoducts in Daraz are:")
print(rex)

with open("darazproducts.txt", 'w') as g:
    for key, value in rex.items():
        g.write('%s:%s\n' % (key, value))


print("*******************************************************************************************************************************************")

#************************************************************************************************************************************************************

####### FOR SASTO DEAL URL FOR APPLE###################
def get_url2(search_term2):
    templ= 'https://www.sastodeal.com/electronic/mobile/{}.html'
    search_term2 = search_term2.replace(' ','+')
    return templ.format(search_term2)
url2= get_url2('apple')
browser.get(url2)
#print(url2)
#********TOTAL NO> OF PRODUCTS FOR SASTO DEAL*********#######
numofproducts_sasto=browser.find_element_by_xpath('/html/body/div[2]/main/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div/div[4]/div').text
totoalpro_sasto= (numofproducts_sasto.split(' ').pop(0))
print("Total number of products in Sasto-deal are: ",int(totoalpro_sasto))


####******LOOOPPPP TO FIND THE PRICE******
product_list_sasto=[]
j= 1
while (j<= int(totoalpro_sasto)):
    data_sasto=browser.find_element_by_xpath('/html/body/div[2]/main/div[2]/div[1]/div[7]/ol/li['+str(j)+']/div/div/div[1]/span/span/span/span').text
    product_list_sasto.append(data_sasto)
    j +=1
#print(product_list_sasto)
Only_price_sasto = []
for names in product_list_sasto:
  Only_price_sasto.append(names.split()[-1])

# change list str in int#########
Only_price_sasto=[ sub.replace(',', '') for sub in Only_price_sasto]
Only_price_sasto = [float(x) for x in Only_price_sasto]
#print(Only_price_sasto)


#######NAME OF PRODUCT SASTO DEAL########
#/html/body/div[2]/main/div[2]/div[1]/div[7]/ol/li[1]/div/div/strong/a
#/html/body/div[2]/main/div[2]/div[1]/div[7]/ol/li[2]/div/div/strong/a
productnamesasto_list=[]
b= 1
while (b<= int(totoalpro_sasto)):
    data_name_sasto=browser.find_element_by_xpath('/html/body/div[2]/main/div[2]/div[1]/div[7]/ol/li['+str(b)+']/div/div/strong/a').text
    productnamesasto_list.append(data_name_sasto)
    b +=1
#print(productnamesasto_list)

ress = {}
for key in productnamesasto_list:
    for value in Only_price_sasto:
        ress[key] = value
        Only_price_sasto.remove(value)
        break
print("All the products in Sasto-Deal are: ")
print(ress)

with open("sasto-dealproducts.txt", 'w') as f:
    for key, value in ress.items():
        f.write('%s:%s\n' % (key, value))

print("****************************************************************************************************88****8********************************************")

min_val=list(rex.values())
min_key=list(rex.keys())
min_price_daraz= min(min_val)
min_prod_daraz= min_key[min_val.index(min(min_val))]
#print(min_key[min_val.index(min(min_val))], "has the lowest price of Rs.",min_price_daraz,"in Dazar")

minn_vall=list(ress.values())
minn_keyy=list(ress.keys())
min_price_sasto= min(minn_vall)
min_prod_sasto= minn_keyy[minn_vall.index(min(minn_vall))]
#print(minn_keyy[minn_vall.index(min(minn_vall))], "has the lowest price of Rs.",min_price_sasto,"in SastoDeal")

if min_price_sasto == min_price_daraz:
    print("Both the websites have Lowest prices.")
    print("Daraz with ",min_prod_daraz,": Rs.", min_price_daraz)
    print("Sasto-deal with ",min_prod_sasto,": Rs.",min_price_sasto)
elif min_prod_sasto < min_prod_daraz:
    print("Sasto-Deal has the cheaper value of:", min_prod_sasto,": Rs.", min_price_sasto)
elif min_price_daraz < min_price_sasto:
    print("Dazar has the cheaper value of:", min_prod_daraz,": Rs.", min_price_daraz )
else:
    print("Sadgeeee..Dont bye anything..")


















