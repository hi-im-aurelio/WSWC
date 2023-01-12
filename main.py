from selenium import webdriver 
from selenium.webdriver.common.by import By
from cockroach import developing_cockroach as developer

import time

from app.lib.models.urls import URL_BEBIDAS
from scrappy import accept_cockies, scraping

developer.log('Calling the browser. Wait a moment...')
print()

firefox = webdriver.Firefox()
firefox.set_window_size(500, 700)
developer.log('Browser loaded. Starting program! (っ＾▿＾)۶🍸🌟🍺٩(˘◡˘ )')
firefox.get(URL_BEBIDAS)
# firefox.add_cookie()

# Aceitando cockies do website.
#
accept_cockies(firefox, 'amgdprcookie-button')

ordered_list = firefox.find_element(By().TAG_NAME, 'ol') 

print('Starting scan in 2 seconds...')
time.sleep(1)

list_item = ordered_list.find_elements(By().TAG_NAME, 'li')
print('✔ Found data.')
developer.log('✔ Consuming fetched data.')

scraping(list_item)