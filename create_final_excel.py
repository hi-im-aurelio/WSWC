import os

from app.lib.blocs.excel import BlocLoadExcel
from app.lib.blocs.excel import BlocExcel

FILES = os.listdir('./')

NEW_DOCUMENT = BlocExcel(fileName='bazara_ALL_PRODUCTS', columnNames=['PRODUCT_NAME', 'PRODUCT_LINK', 'PRODUCT_PRICE'], sheetName='Sheet')

for FILE in FILES:
    if '.xlsx' in FILE:
        document = BlocLoadExcel().load_excel(FILE)['Sheet']
        for ROW in document.iter_rows(min_row=2):
            NEW_DOCUMENT.save_data_in_excel([ROW[0].value, ROW[1].value, ROW[2].value])

NEW_DOCUMENT.generate_and_save_excel() # commit