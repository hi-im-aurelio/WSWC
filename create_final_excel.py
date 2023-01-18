import os

from app.blocs.excel import BlocLoadExcel
from app.blocs.excel import BlocExcel
import os

FILES = os.listdir('./')

def create_final_doc():
    NEW_DOCUMENT = BlocExcel(fileName='final_document', columnNames=['PRODUCT_NAME', 'PRODUCT_LINK', 'PRODUCT_PRICE'], sheetName='Sheet')

    for FILE in FILES:
        if '.xlsx' in FILE:
            document = BlocLoadExcel().load_excel(FILE)['Sheet']
            for ROW in document.iter_rows(min_row=2):
                NEW_DOCUMENT.save_data_in_excel([ROW[0].value, ROW[1].value, ROW[2].value])

    NEW_DOCUMENT.generate_and_save_excel() # commit

    _isPath = os.path.abspath("./final_document.xlsx")
    print('Data collected for {}'.format(_isPath))