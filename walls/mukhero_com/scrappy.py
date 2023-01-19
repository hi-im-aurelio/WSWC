from selenium import webdriver 
from selenium.webdriver.common.by import By
from browser import browser
from cockroach import developing_cockroach as developer


import time
from app.blocs.excel import BlocExcel

# Função para clicar no butão de cockies.
#
def accept_cockies(firefox : webdriver.Firefox, class_name: str):
    button = firefox.find_element(By().CLASS_NAME, class_name)
    button.click()


def scraping(document:BlocExcel, prices:list, names:list, pages:list):
    # Consummer.
    # html navigational structure.

    shaved = 0
    with open('details.coc', 'a') as file:
        for price, name, page in zip(prices, names, pages):
            
            product_price = price.find_element(By.TAG_NAME, "span").find_element(By.TAG_NAME, 'bdi').text
            product_name = name
            product_page = page

            document.save_data_in_excel([product_name,product_page,product_price])
            shaved += 1
            print('Product scraping: {}/{}'.format(shaved, len(prices)))

def next_page(browser:webdriver.Firefox):
    try:
        print('5 seconds to the next page. Wait a moment.')
        time.sleep(5)
        # browser.find_element(By.XPATH, "//a[@class='next page-numbers']").click()
        browser.find_element(By.XPATH, "//a[@class='NOT-IN']").click()
        print('Going to the next page...')
        
        # Caracas! Isso resolveu um problema de 1 hora em 1 segundo.
        # time.sleep(5)
        # browser.refresh() # O refresh permite que os elementos permançam como estavam no primeiro estado.
        # time.sleep(1)
        return True
    except:
        developer.log('No more pages to scratch.')
        return False
    