from selenium import webdriver
from selenium.webdriver.common.by import By
import sqlite3

browser = webdriver.Firefox()
browser.implicitly_wait(2.5)


connection = sqlite3.connect('vdl(sqlite3).db')
cursor = connection.cursor()

# Create the table (if it doesn't exist)
cursor.execute("""CREATE TABLE IF NOT EXISTS events (
    Event TEXT NOT NULL,
    Location TEXT NOT NULL,
    Date INTEGER,
    Start INTEGER,
    End INTEGER,
    Image TEXT NOT NULL
)""")

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
        event_info=(name.text.strip(),
                    location.text.strip(),
                    date.text.strip(),
                    start_date.text.strip(),
                    end_date.text.strip(),
                    image.get_attribute('src')
                )
        cursor.execute("INSERT INTO events (Event, Location, Date, Start, End, Image) VALUES (?, ?, ?, ?, ?, ?)", event_info)
  
print("Event data saved successfully to vdl.db!")
connection.commit()
browser.quit()
connection.close()
