import os

from app.blocs.excel import BlocLoadExcel
from app.blocs.excel import BlocExcel
import os

FILES = os.listdir('./')
_documentPath = 'documents/'

def create_final_doc():
    _document = list()

    fileName = ''
    for FILE in FILES:
        if '.xlsx' in FILE:
            _document.append(FILE)
        else: 
            ...
    
    while True:
        if len(_document) == 0:
            print('Nenhum documento encotrado na diretorio: /.')
            _docDirs = list()
            try:
                _docDirs = os.listdir(_documentPath)
            except FileNotFoundError as notFoundPathError:
                print('Tu sabes, o tempo é tão sombrio. Saindo...')
                break
            
            if len(_docDirs) != 0: 
                print(f'DIR {_documentPath} encotrado:\nDiretorios de modelos. Escolha:')
                for dir in _docDirs:
                    print(' -> ' + dir)
                _input = input('Para sair digite (n/N). Ou\nSelecione o Modelo : ')
            else:
                print('DIR documents/ encotrado. Mas nenhum modelo encotrado.\n')
                print('Tu sabes, o tempo é tão sombrio. Saindo...')
                break
        
            if _input in _docDirs:
                _path = _documentPath+f'{_input}'
                _acess(_path)
                break
            elif _input.upper() in ['N', 'NÃO', 'NO']:
                print('Tu sabes, o tempo é tão sombrio. Saindo...')
                break

    
def _acess(path):
    NEW_DOCUMENT = BlocExcel(fileName=path.replace(f'{_documentPath}', '') + '_final_document', columnNames=['PRODUCT_NAME', 'PRODUCT_LINK', 'PRODUCT_PRICE'], sheetName='Sheet')
    _acessFILES = os.listdir(path)
    _document = list()
    for FILE in _acessFILES:
        if '.xlsx' in FILE:
            _document.append(FILE)
        else: 
            ...
    if len(_document) == 0: 
        print(f'Nenhum documento encontrado em: DIR({path})')
        print('Tu sabes, o tempo é tão sombrio. Saindo...')
    else:
        for FILE in _acessFILES:
            if '.xlsx' in FILE:
                document = BlocLoadExcel().load_excel(path+'/'+FILE)['Sheet']
                for ROW in document.iter_rows(min_row=2):
                    NEW_DOCUMENT.save_data_in_excel([ROW[0].value, ROW[1].value, ROW[2].value])
        NEW_DOCUMENT.generate_and_save_excel() # commit