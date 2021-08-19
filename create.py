import json

from read import *

def create():
    # Recebe o usuário e senha
    usuario = input('[C] Insira o nome de usuário: ')
    senha = input('[C] Insira a senha: ')

    # Sistema simples para adicionar ao banco
    db = read(printar=False)
    db.update({usuario: senha})

    # Salva o arquivo
    json.dump(db, open('db.json', 'w'))

    # Mensagem de sucesso
    print('[C] Usuário criado com sucesso!')
