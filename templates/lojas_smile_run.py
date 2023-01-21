
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
        
        list_items = []
        n = firefox.find_elements(By.XPATH, "//div/div/ul/li/div[@class='product-block']")
        
        for i in n:
            try:
                # se falha aqui, então a lista não será preenchida.
                i.find_element(By.CLASS_NAME, "product-block-inner").find_element(By.CLASS_NAME, "container-inner").find_element(By.TAG_NAME, "a").get_attribute("href")
                list_items.append(i.find_element(By.CLASS_NAME, "product-block-inner"))
            except:
                ...

        coc.log('✔ Found data.')
        print('Consuming fetched data.')

        scraping(document, list_items)


    def setup():
        for URL, NAME in zip(ALL_URLS, NAMES):
            
            # Inicializando o documento excel.
            _document = BlocExcel(fileName='lojas-smile_category_'+NAME, columnNames=['PRODUCT_NAME', 'PRODUCT_LINK', 'PRODUCT_PRICE'], sheetName='Sheet')
            
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