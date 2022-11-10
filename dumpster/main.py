from selenium import webdriver
from selenium import *
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

import csv
import os
repo = input(" repo you would like to target ")
repo1 = repo
chrome_driver_path = "/Users/ryan/Desktop/developer/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(repo)

res = driver.find_elements(By.CLASS_NAME, "repo")

actual_txt_file = []

def going_for_raw(repo5):
    driver.get(repo5)
    print("worked")
    raw = driver.find_element(By.CLASS_NAME, "js-permalink-replaceable-link")
    raw.click()
    html = driver.page_source
    # print(html)
    if "pass" in html:
        print(f"pass found{repo5}")
    driver.back()
    driver.back()
    time.sleep(3)



def loop(repo3):
    driver.get(repo3)
    ress = driver.find_elements(By.CLASS_NAME, "js-navigation-open")
    for a in ress:
        print(a.text)
        # repo4 = f"{repo3}/blob/main/{a.text}"
        # actual_txt_file.append(repo4)
    if "py" in a.text:
        print("py")
        repo5 = f"{repo3}/blob/main/{a.text}"
        going_for_raw(repo5)
    elif "txt" in a.text:
        print("txt")
        repo5 = f"{repo3}/blob/main/{a.text}"
        # reop4 = repo3
        going_for_raw(repo5)
    elif "js" in a.text:
        print("js")
        repo5 = f"{repo3}/blob/main/{a.text}"
        going_for_raw(repo5)
    elif "json" in a.text:
        print("json")
    elif "php" in a.text:
        print("php")




        repo4 = repo3
    # print(actual_txt_file)
    time.sleep(3)

    # driver.back()

links = []
flinks = []

for e in res:
    links.append(e.text)

i = 0
for l in links:
    repo3 = f"{repo}/{l}"
    flinks.append(repo3)
    loop(repo3)
    repo = f"{repo1}"

# print(links)
# print(flinks)https://github.com/crackallcode/




# with open('output.csv', 'w') as data_file:
#     writer = csv.writer(data_file)
#     writer.writerows([flinks])

# with open('output.csv', 'r') as data_file:
#     reader = csv.reader(data_file)
#     for i in reader:
#         print(i)


    # loop()




# res = driver.find_elements_by_class_name("repo")


driver.close()





driver.quit()