from selenium.webdriver.common.by import By
from app.blocs.excel import BlocExcel
from app.models.mukhero_com import NAMES, ALL_URLS 
from browser import browser
import time

from walls.mukhero_com.scrappy import next_page, scraping

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
            time.sleep(2)  # It is necessary here to give it some time to load the content

    # Começando a varredura.
    def start_scan(document:BlocExcel):
        pages = firefox.find_elements(By.XPATH, "//ul/li/div/div/div/a[@class='woocommerce-LoopProduct-link woocommerce-loop-product__link']")

        links = []
        
        for pagein in pages:
            page = pagein.get_attribute('href')
            links.append(page)
        
        names = []
        
        for name in firefox.find_elements(By.XPATH, "//ul/li/div/div/div/a/h2[@class='woocommerce-loop-product__title']"):
            if name.text != '': names.append(name.text)

        prices = firefox.find_elements(By.XPATH, "//div[@class='price-add-to-cart']")

        scraping(document, pages=links, names=names, prices=prices)

    def setup():

        for URL, NAME in zip(ALL_URLS, NAMES):
            
            # Inicializando o documento excel.
            _document = BlocExcel(fileName='mukhero_category_'+NAME, columnNames=['PRODUCT_NAME', 'PRODUCT_LINK', 'PRODUCT_PRICE'], sheetName='Sheet')
            
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
