from cockroach import developing_cockroach as coc
from selenium.webdriver.common.by import By
from app.blocs.excel import BlocExcel
from app.models.pep_co_mz import ALLURLS, URLSNAMES
from browser import browser
import time

from walls.pep_co_mz.scrappy import ignore_newslatter, next_page, scraping

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

        list_items = firefox.find_elements(By.XPATH, "//section/div/article[@class='grid grid-cols-1 md:grid-rows-2']")

        scraping(document, list_items)

    def setup():


        newslatter_ignored = False


        for URL, NAME in zip(ALLURLS, URLSNAMES):
            
            # Inicializando o documento excel.
            _document = BlocExcel(fileName='pep_category_'+NAME, columnNames=['PRODUCT_NAME', 'PRODUCT_LINK', 'PRODUCT_PRICE'], sheetName='Sheet')
            
            firefox.get(URL) # Pegando a categoria

            # Aceitando inicilamente os cookies.
            if newslatter_ignored == False:
                time.sleep(10) # await load page
                ignore_newslatter(firefox) 
                newslatter_ignored = True
            else : print('Todos cookies foram aceitos')

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