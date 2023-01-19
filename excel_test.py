from app.blocs.excel import BlocExcel

NAME = 'BANHEIRAS'
document = BlocExcel(fileName='bazara_category_'+NAME, columnNames=['PRODUCT_NAME', 'PRODUCT_LINK', 'PRODUCT_PRICE'], sheetName='Sheet')
document.generate_and_save_excel()