from app.blocs.excel import BlocExcel
from app.models.milano_co_mz import ALL_URLS, NAMES

from cockroach import developing_cockroach as developer
import time
from selenium.webdriver.common.by import By
from browser import browser
from walls.milano_co_mz.scrappy import next_page, scraping


def main():

    print('Calling the browser. Wait a moment.')
    firefox = browser()

    def start_scan(document:BlocExcel):
        list_items = firefox.find_elements(By.XPATH, "//div[@class='product-inner clr']")
        
        developer.log('✔ Found data.')
        print('Consuming fetched data.')

        scraping(document, list_items)

    def setup():

        for URL, NAME in zip(ALL_URLS, NAMES):
            _document = BlocExcel(fileName='milano_category_'+NAME, columnNames=['PRODUCT_NAME', 'PRODUCT_LINK', 'PRODUCT_PRICE'], sheetName='Sheet')
    
            firefox.get(URL) # Pegando a categoria
            while True:
                print('Starting scan in 2 second...')
                time.sleep(2)
                start_scan(_document)
                if next_page(browser=firefox):
                    continue
                else:
                    _document.generate_and_save_excel()
                    break
    setup()