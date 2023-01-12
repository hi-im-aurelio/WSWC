from selenium import webdriver 
from selenium.webdriver.common.by import By
from cockroach import developing_cockroach as developer

import time

from app.lib.models.urls import ALL_URLS, NAMES
from scrappy import accept_cockies, next_page, scraping

from app.lib.blocs.excel import BlocExcel

developer.log('Calling the browser. Wait a moment...')
print()

firefox = webdriver.Firefox()
# firefox.set_window_size(500, 700)

developer.log('Browser loaded. Starting program! (っ＾▿＾)۶🍸🌟🍺٩(˘◡˘ )')

# Começando a varredura.
def start_scan(document:BlocExcel):
    ordered_list = firefox.find_element(By().TAG_NAME, 'ol') 
    list_item = ordered_list.find_elements(By().TAG_NAME, 'li')
    developer.log('✔ Found data.')
    print('Consuming fetched data.')

    scraping(document, list_item)


def setup():


    do_you_accept_cookies = False


    for URL, NAME in zip(ALL_URLS, NAMES):
        
        # Inicializando o documento excel.
        _document = BlocExcel(fileName='bazara_category_'+NAME, columnNames=['PRODUCT_NAME', 'PRODUCT_LINK', 'PRODUCT_PRICE'], sheetName='Sheet')
        
        firefox.get(URL) # Pegando a categoria

        # Aceitando inicilamente os cookies.
        if do_you_accept_cookies == False:
            time.sleep(45) # await load page
            accept_cockies(firefox, 'amgdprcookie-button') 
            do_you_accept_cookies = True
        else : print('Todos cookies foram aceitos')

        while True:
            print('Starting scan in 2 second...')
            time.sleep(2)
            start_scan() # primeiro pega os dados da pagina.
            if next_page(browser=firefox): # depois vefica se ainda há paginas.
                continue # continua caso hajam paginas.
            else:
                _document.generate_and_save_excel()
                break # caso contrario

setup()

developer.log('✔ Program finished. Found errors. 0.', name= 'Scraping')