from selenium import webdriver 
from selenium.webdriver.common.by import By
import openpyxl
from cockroach import developing_cockroach as developer


import time


from app.lib.models.urls import URL_BEBIDAS

fileName:str = 'bazara_bebidas_datas'

page:str = 'Bebidas'
        
book = openpyxl.Workbook()

book.create_sheet(page)
sheet = book[page]
sheet.append(['NOME_DO_PRODUTO', 'LINK_DA_IMAGEM_DO_PRODUTO', 'PAGINA_DO_PRODUTO', 'PREÇO_DO_PRODUTO', 'LOJA', 'PÁGINA_DA_LOJA'])


# Função para clicar no butão de cockies.
#
def accept_cockies(firefox : webdriver.Firefox, class_name: str):
    time.sleep(50) # await load page
    button = firefox.find_element(By().CLASS_NAME, class_name)
    button.click()


def scraping(list_item):
    # Consummer.
    # html navigational structure.

    shaved = 0
    for ELEMENT in list_item:

        div_class_product_item_info = ELEMENT.find_elements(By().TAG_NAME, 'div')
        div_class_image_grid = div_class_product_item_info[0].find_elements(By().TAG_NAME, 'div')

        # photo bloc
        #
        a_class_product_photo = div_class_image_grid[0].find_element(By().TAG_NAME, 'a')
        span1 = a_class_product_photo.find_element(By().TAG_NAME, "span")
        span2 = span1.find_element(By().TAG_NAME, "span")
        img = span2.find_element(By().TAG_NAME, "img")
        image_link = img.get_attribute('src')

        # details bloc
        #
        div_class_product_item_details = div_class_product_item_info[0].find_element(By().CLASS_NAME, 'product-item-details')
        strong_class_product_ite_name = div_class_product_item_details.find_element(By().CLASS_NAME, 'product-item-link')
        product_name = strong_class_product_ite_name.get_attribute('title')
        product_page = strong_class_product_ite_name.get_attribute('href')


        product_price = div_class_product_item_details.find_element(By().CLASS_NAME, 'price')
        product_store = div_class_product_item_details.find_elements(By().TAG_NAME, 'a')

        # print(product_name)
        sheet.append([str(product_name),str(image_link), str(product_page), str(product_price),  str(product_store[1].text), str(product_store[1].get_attribute('href'))])
        shaved += 1
        print('Product scraping: {}/{}'.format(shaved, len(list_item)))

    book.save(fileName + '.xlsx')
    developer.log('✔ Program finished. Found errors. 0.', name= 'Scraping')