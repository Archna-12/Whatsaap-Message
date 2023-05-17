from selenium import webdriver
from csv import reader

contacts = []
with open('contacts.csv', "r") as f:
    csv_reader = reader(f)
    for row in csv_reader:
        contacts.append(row[0])

driver = webdriver.Chrome()  # Selenium chromedriver path
driver.implicitly_wait(10)
driver.get("https://web.whatsapp.com/")

while True:
    for name in contacts:
        try:
            user = driver.find_element_by_xpath("//span[@title='{}']".format(name))
            user.click()

            text_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
            text_box.send_keys(name)

            send_btn = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]')
            send_btn.click()
        except Exception as e:
            print('Keep Scrolling Your WhatsApp Contacts')
            pass
        else:
            print('Successfully sent a message to', name)
            print(len(contacts) - 1, 'more messages left to send')
            contacts = [c for c in contacts if c != name]

    if len(contacts) == 0:
        break

driver.quit()