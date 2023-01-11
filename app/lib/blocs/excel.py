'''Fragmento responsavel por gerar o excel.'''
import openpyxl
from cockroach import developing_cockroach as developer

page:str = 'Bebidas'

class BlocExcel:
    def __init__(self, fileName:str):
        self.fileName:str = fileName
        
        self.book = openpyxl.Workbook()

        self.book.create_sheet(page)

        self.sheet = self.book[page]

        self.sheet.append(['NOME_DO_PRODUTO', 'LINK_DA_IMAGEM_DO_PRODUTO', 'PAGINA_DO_PRODUTO', 'PREÇO_DO_PRODUTO', 'LOJA', 'PÁGINA_DA_LOJA'])

    def save_data_in_excel(self,productName, linkImage, productPage, productPrice, productStore, storePage):
        '''Save data'''
        self.sheet.append([productName, linkImage, productPage, productPrice, productStore, storePage])

    def generate_and_save_excel(self):
        '''Generate and save excel file'''
        self.book.save(self.fileName + '.xlsx')
        developer.log(message='Saved Excel file.', name='Excel')
