from selenium import webdriver 
from selenium.webdriver.common.by import By
from cockroach import developing_cockroach as coc
import time
from app.models.megafresh_co_mz import ALL_URLS, NAMES

from app.blocs.excel import BlocExcel
from walls.megafresh_co_mz.scrappy import next_page, scraping


print('Iniciando o browser.')
firefox = webdriver.Firefox()


def scroll():
    total_page_height = firefox.execute_script("return document.body.scrollHeight")
    browser_window_height = firefox.get_window_size(windowHandle='current')['height']
    current_position = firefox.execute_script('return window.pageYOffset')
    
    while total_page_height - current_position > browser_window_height:
        firefox.execute_script(f"window.scrollTo({current_position}, {browser_window_height + current_position});")
        current_position = firefox.execute_script('return window.pageYOffset')
        time.sleep(2.5)  # It is necessary here to give it some time to load the content


# Começando a varredura.
def start_scan(document:BlocExcel):
    
    print('Aguarde, rolando pagina...')
    scroll()
    print('Rolagem terminada. Começando a extração.')

    

    list_items = firefox.find_element(By.ID, 'product_listing').find_elements(By.TAG_NAME, "li")
    coc.log('✔ Found data.')
    print('Consuming fetched data.')

    scraping(document, list_items)


def setup():

    for URL, NAME in zip(ALL_URLS, NAMES):
        
        # Inicializando o documento excel.
        _document = BlocExcel(fileName='megafresh_category_'+NAME, columnNames=['PRODUCT_NAME', 'PRODUCT_LINK', 'PRODUCT_PRICE'], sheetName='Sheet')
        
        firefox.get(URL) # Pegando a categoria

        while True:
            print('Starting scan in 2 second...')
            time.sleep(2)
            start_scan(_document) # primeiro pega os dados da pagina.
            if next_page(browser=firefox): # depois vefica se ainda há paginas.
                continue # continua caso hajam paginas.
            else:
                _document.generate_and_save_excel()
                break # caso contrario

setup()

coc.log('✔ Program finished. Found errors. 0.', name= 'Scraping')
