from selenium import webdriver 
from selenium.webdriver.common.by import By
from cockroach import developing_cockroach as developer

import time

from app.lib.models.urls import URL_BEBIDAS
from scrappy import accept_cockies, next_page, scraping

from app.lib.blocs.excel import BlocExcel


# Inicializando o documento excel.
_document = BlocExcel(fileName='bazara_bebidas', columnNames=['PRODUCT_NAME', 'PRODUCT_LINK'], sheetName='BEBIDAS')


developer.log('Calling the browser. Wait a moment...')
print()

firefox = webdriver.Firefox()
# firefox.set_window_size(500, 700)
developer.log('Browser loaded. Starting program! (っ＾▿＾)۶🍸🌟🍺٩(˘◡˘ )')
firefox.get(URL_BEBIDAS)
# firefox.add_cookie()

# Aceitando cockies do website.
#
accept_cockies(firefox, 'amgdprcookie-button')

# Começando a varredura.
def start_scan():
    ordered_list = firefox.find_element(By().TAG_NAME, 'ol') 
    list_item = ordered_list.find_elements(By().TAG_NAME, 'li')
    developer.log('✔ Found data.')
    print('Consuming fetched data.')

    scraping(_document, list_item)

# setup
while True:
    print('Starting scan in 2 second...')
    time.sleep(2)
    start_scan() # primeiro pega os dados da pagina.
    if next_page(browser=firefox): # depois vefica se ainda há paginas.
        continue # continua caso hajam paginas.
    else:
        _document.generate_and_save_excel()
        break # caso contrario

developer.log('✔ Program finished. Found errors. 0.', name= 'Scraping')