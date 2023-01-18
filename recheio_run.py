from selenium import webdriver 
from selenium.webdriver.common.by import By
from cockroach import developing_cockroach as developer
import time

from app.blocs.excel import BlocExcel
from app.models.recheio_co_mz import ALL_URLS, NAMES
from walls.recheio_co_mz.scrappy import next_page, scraping
from browser import browser

def main():
    print('Calling the browser. Wait a moment.')

    firefox = browser()

    def scroll():
        total_page_height = firefox.execute_script("return document.body.scrollHeight")
        browser_window_height = firefox.get_window_size(windowHandle='current')['height']
        current_position = firefox.execute_script('return window.pageYOffset')
        
        while total_page_height - current_position > browser_window_height:
            firefox.execute_script(f"window.scrollTo({current_position}, {browser_window_height + current_position});")
            current_position = firefox.execute_script('return window.pageYOffset')
            time.sleep(5)  # It is necessary here to give it some time to load the content

    # Começando a varredura.
    def start_scan(document:BlocExcel):
        
        print('Aguarde, rolando pagina.')
        scroll()
        print('Rolagem terminada -> Começando a extração.')

        row = firefox.find_element(By.CLASS_NAME, "ps-shopping-product")    
        row_ProductList = row.find_element(By.TAG_NAME, "div")

        list_item = row_ProductList.find_elements(By.XPATH, "//div[@class=' col-lx-1 col-lg-4 col-md-4 col-sm-6 col-6']")

        scraping(document, list_item)

    def setup():

        for URL, NAME in zip(ALL_URLS, NAMES):
            
            # Inicializando o documento excel.
            _document = BlocExcel(fileName='recheio_category_'+NAME, columnNames=['PRODUCT_NAME', 'PRODUCT_LINK', 'PRODUCT_PRICE'], sheetName='Sheet')
            
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