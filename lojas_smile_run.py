
from selenium.webdriver.common.by import By
from cockroach import developing_cockroach as coc
from app.blocs.excel import BlocExcel
from app.models.lojas_smile_com import ALL_URLS, NAMES
from walls.lojas_smile_com.scrappy import next_page, scraping
import time
from browser import browser

def main():
    print('Iniciando o browser.')
    firefox = browser()

    # Começando a varredura.
    def start_scan(document:BlocExcel):
        
        list_items = firefox.find_element(By.XPATH, "//ul[@class='products  columns-4 list']").find_elements(By.TAG_NAME, "li")
        coc.log('✔ Found data.')
        print('Consuming fetched data.')

        scraping(document, list_items)


    def setup():


        do_you_accept_cookies = False


        for URL, NAME in zip(ALL_URLS, NAMES):
            
            # Inicializando o documento excel.
            _document = BlocExcel(fileName='lojas_smile_category_'+NAME, columnNames=['PRODUCT_NAME', 'PRODUCT_LINK', 'PRODUCT_PRICE'], sheetName='Sheet')
            
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