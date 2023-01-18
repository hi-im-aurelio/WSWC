from app.blocs.excel import BlocExcel
from app.models.milano_co_mz import ALL_URLS, NAMES

from cockroach import developing_cockroach as developer
import time
from selenium.webdriver.common.by import By
from browser import browser
from walls.milano_co_mz.scrappy import next_page, scraping


def main():
    developer.log('Calling the browser. Wait a moment.')
    firefox = browser()
    print('Browser loaded. Starting program!')

    # Começando a varredura.
    def start_scan(document:BlocExcel):
        elemento_de_lista = firefox.find_element(By.XPATH, "//ul[@class='products oceanwp-row clr grid']")
        list_items = elemento_de_lista.find_elements(By.TAG_NAME, "li")


        developer.log('✔ Found data.')
        print('Consuming fetched data.')

        scraping(document, list_items)


    def setup():


        do_you_accept_cookies = False


        for URL, NAME in zip(ALL_URLS, NAMES):
            
            # Inicializando o documento excel.
            _document = BlocExcel(fileName='milano_category_'+NAME, columnNames=['PRODUCT_NAME', 'PRODUCT_LINK', 'PRODUCT_PRICE'], sheetName='Sheet')
            
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