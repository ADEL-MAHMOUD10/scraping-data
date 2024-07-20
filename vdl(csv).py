from selenium import webdriver
from selenium.webdriver.common.by import By
import csv

browser = webdriver.Firefox()
browser.implicitly_wait(2.5)

for i in range(0,76):
    url = "https://www.vdl.lu/en/whats-on?page="+str(i)
    browser.get(url)
    
    images = browser.find_elements(By.CSS_SELECTOR,"figure img")
    names = browser.find_elements(By.CSS_SELECTOR,".media-title p")
    locations = browser.find_elements(By.CSS_SELECTOR,".media-text p")
    Dates = browser.find_elements(By.CSS_SELECTOR,".media-date :nth-child(1)")
    start_dates = browser.find_elements(By.CSS_SELECTOR,".media-date :nth-child(2)")
    end_dates = browser.find_elements(By.CSS_SELECTOR,".media-date :nth-child(3)")


    for name,location,date,start_date,end_date,image in zip(names,locations,Dates,start_dates,end_dates,images):
        print(f"Event: {name.text.strip()}")
        print(f"Location: {location.text.strip()}")
        print(f"Date: {date.text.strip()}")
        print(f"Start: {start_date.text.strip()}")
        print(f"End: {end_date.text.strip()}")
        print(f"Image:{image.get_attribute('src')}")
        event_info={"Event":name.text.strip(),
                    "Location":location.text.strip(),
                    "Date":date.text.strip(),
                    "Start":start_date.text.strip(),
                    "End":end_date.text.strip(),
                    "Image":image.get_attribute('src')
                }
        with open("vdl.csv",'a',newline='',encoding="utf-8") as csv_file:
            write = csv.DictWriter(csv_file,fieldnames=["Event","Location","Date","Start","End","Image"])
            if not csv_file.tell():
                write.writeheader()

            write.writerow(event_info)
print("Event data saved successfully to vdl_events.csv!")
browser.close()
