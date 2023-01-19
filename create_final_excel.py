import os

from app.blocs.excel import BlocLoadExcel
from app.blocs.excel import BlocExcel
import os

FILES = os.listdir('./')

def create_final_doc():
    fileName = ''
    for FILE in FILES:
        if '.xlsx' in FILE:
            fileName = FILE
            document = BlocLoadExcel().load_excel(FILE)['Sheet']
            for ROW in document.iter_rows(min_row=2):
                NEW_DOCUMENT.save_data_in_excel([ROW[0].value, ROW[1].value, ROW[2].value])
    NEW_DOCUMENT = BlocExcel(fileName=fileName.replace('_category', '') + 'FINAL-DOC', columnNames=['PRODUCT_NAME', 'PRODUCT_LINK', 'PRODUCT_PRICE'], sheetName='Sheet')

    NEW_DOCUMENT.generate_and_save_excel() # commit