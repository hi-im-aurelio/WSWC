from selenium.webdriver.common.by import By
from cockroach import developing_cockroach as coc
from app.blocs.excel import BlocExcel
from app.models.mozbuy_com import mozbuyurls, mozbuynames

import time
from browser import browser
from walls.mozbuy_com.scrappy import next_page, scraping

def main():
    print('Calling the browser. Wait a moment...')
    firefox = browser()
    print('Browser loaded. Starting program!')

    def start_scan(document:BlocExcel):
        print('Iniciando o scaneamento...')
        list_items =  items = firefox.find_elements(By.XPATH, "//div/div/div[@class='xs-single-product']")
        print('Dados encontrados. Começando.')

        scraping(document, list_items)


    def setup():

        for URL, NAME in zip(mozbuyurls, mozbuynames):
            
            # Inicializando o documento excel.
            _document = BlocExcel(fileName='mozbuy_category_'+NAME, columnNames=['PRODUCT_NAME', 'PRODUCT_LINK', 'PRODUCT_PRICE'], sheetName='Sheet')
            
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