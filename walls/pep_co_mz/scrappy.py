from selenium import webdriver 
from selenium.webdriver.common.by import By
from cockroach import developing_cockroach as developer

import time
from app.blocs.excel import BlocExcel
from selenium import webdriver

# Função para clicar no butão de cockies.
#
def ignore_newslatter(firefox : webdriver.Firefox):
    button = firefox.find_element(By.XPATH, "//div/div/span[@class='absolute right-2 top-1 text-5xl cursor-pointer m-0 p-2 leading-4']")
    button.click()


def scraping(document:BlocExcel, list_item):
    # Consummer.
    # html navigational structure.

    shaved = 0
    for ELEMENT in list_item:

        product_name = ELEMENT.find_element(By.CLASS_NAME, "row-span-1").find_element(By.TAG_NAME, "header").find_element(By.TAG_NAME,"a").find_element(By.TAG_NAME, "span").text
        product_price = ELEMENT.find_element(By.CLASS_NAME, "row-span-1").find_element(By.TAG_NAME, "strong").text
        product_url = ELEMENT.find_element(By.CLASS_NAME, "row-span-1").find_element(By.TAG_NAME, "header").find_element(By.TAG_NAME,"a").get_attribute("href")

        document.save_data_in_excel([product_name,product_url,product_price])
        shaved += 1
        print('Product scraping: {}/{}'.format(shaved, len(list_item)))

def next_page(browser:webdriver.Firefox):
    try:
        print('5 seconds to the next page. Wait a moment.')
        time.sleep(5)
        browser.find_element(By.XPATH, "//div/div/a[@class='btn-transparent text-xl ml-1']").click()
        print('Going to the next page...')
        
        # Caracas! Isso resolveu um problema de 1 hora em 1 segundo.
        # time.sleep(5)
        # browser.refresh() # O refresh permite que os elementos permançam como estavam no primeiro estado.
        # time.sleep(1)
        return True
    except:
        developer.log('No more pages to scratch.')
        return False
    