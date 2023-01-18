from selenium import webdriver 
from selenium.webdriver.common.by import By
from cockroach import developing_cockroach as developer
import time
from app.models.krolyc_co_mz import KROLYC_URLS, NAMES
from walls.krolyc_co_mz.scrappy import scraping, next_page
from app.blocs.excel import BlocExcel
from browser import browser

def main():
    print('Calling the browser. Wait a moment...')
    firefox = browser()
    print('Browser loaded. Starting program!')

    def scroll():
        total_page_height = firefox.execute_script("return document.body.scrollHeight")
        browser_window_height = firefox.get_window_size(windowHandle='current')['height']
        current_position = firefox.execute_script('return window.pageYOffset')
        
        while total_page_height - current_position > browser_window_height:
            firefox.execute_script(f"window.scrollTo({current_position}, {browser_window_height + current_position});")
            current_position = firefox.execute_script('return window.pageYOffset')
            time.sleep(3)  # It is necessary here to give it some time to load the content

    # Começando a varredura.
    def start_scan(document:BlocExcel):
        
        print('Aguarde, rolando pagina...')
        scroll()
        print('Rolagem terminada. Começando a extração.')

        
        list_item = firefox.find_elements(By().CLASS_NAME, 'product-wrapper')
        scraping(document, list_item)

    # firefox.get(KROLYC_URLS[0]) 

    def setup():

        for URL, NAME in zip(KROLYC_URLS, NAMES):
            
            # Inicializando o documento excel.
            _document = BlocExcel(fileName='krolyc_category_'+NAME, columnNames=['PRODUCT_NAME', 'PRODUCT_LINK', 'PRODUCT_PRICE'], sheetName='Sheet')
            
            firefox.get(URL) # Pegando a categoria

            while True:
                print('Starting scan in 2 second...')
                time.sleep(10)
                start_scan(_document) # primeiro pega os dados da pagina.
                if next_page(browser=firefox): # depois vefica se ainda há paginas.
                    continue # continua caso hajam paginas.
                else:
                    _document.generate_and_save_excel()
                    break # caso contrario
    setup()
