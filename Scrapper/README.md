# Whatsapp-automation-using-python-selenium
This python program will read the names of contacts availabe in 'contacts.csv' file and send a particular msg to all

## Requirements:
1. Install openpyxl library(used to read and write file from or to .csv file) : 
	>$ pip install openpyxl
2. Install selenium ( tool used for automation) : 
	>$ pip install selenium
2. Update chrome to latest version
3. Download chrome webdriver

## To run the project : 
1. Firstly update the contact list of 'contacts.csv' file ( the contact name should be same as it is saved in mobile)
2. Update the msg variable with your new msg availabe in 'WhatsApp.py' file
2. Run WhatsApp.py
	>$ python WhatsApp.py

## After running the code:
1. Wait till the whatsapp web page opens.
2. Now scan the code shown at the page using whatsapp installed in mobile.
3. Once the whatsapp web page is loaded compeletely, scroll down the contacts list area until you reached to the last contact you want to send msg and it will automatically send the msg to all the contacts available in the 'contacts.csv' file

