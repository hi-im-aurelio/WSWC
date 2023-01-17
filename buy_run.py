from selenium.webdriver.common.by import By
from cockroach import developing_cockroach as developer
import time

from walls.buy_co_mz.scrappy import scraping, next_page
from app.blocs.excel import BlocExcel


from browser import browser
from app.models.buy_co_mz import NAMES, URLS_BUY

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
        time.sleep(1)  # It is necessary here to give it some time to load the content


# Começando a varredura.
def start_scan(document:BlocExcel):
    print('Aguarde, rolando pagina...')
    scroll()
    print('Rolagem terminada. Começando a extração.')

    

    list_items = firefox.find_element(By.XPATH, "//ul[@class='products-loop row grid clearfix']").find_elements(By.TAG_NAME, "li")
    scraping(document, list_items)


def setup():

    for URL, NAME in zip(URLS_BUY, NAMES):
        
        # Inicializando o documento excel.
        _document = BlocExcel(fileName='buy_category_'+NAME, columnNames=['PRODUCT_NAME', 'PRODUCT_LINK', 'PRODUCT_PRICE'], sheetName='Sheet')
        
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

developer.log('✔ Program finished. Found errors. 0.', name= 'Scraping')