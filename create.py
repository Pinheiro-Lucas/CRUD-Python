import json

from read import *

def create():
    # Recebe o usuário e senha
    usuario = input('[C] Insira o nome de usuário: ')
    senha = input('[C] Insira a senha: ')

    # Sistema simples para adicionar ao banco
    info = read(printar=False)
    info.update({usuario: senha})

    # Salva o arquivo
    with open('db.json', 'w') as db:
        json.dump(info, db)
