from read import read

import json

def create():
    # Recebe o usuário
    usuario = input('[C] Insira o nome de usuário: ')

    # Lê o banco
    db = read(printar=False)

    if usuario not in db.keys():
        if checar_digitos(usuario, 'usuario'):
            # Recebe a senha
            senha = input('[C] Insira a senha: ')
            if checar_digitos(senha, 'senha'):
                # Adiciona ao banco os novos registros
                db.update({usuario: senha})
                # Salva o arquivo
                json.dump(db, open('db.json', 'w'))
                # Mensagem de sucesso
                print('[C] Usuário criado com sucesso!')
    else:
        print('[C] O usuário já existe!')


def checar_digitos(texto, parametro):
    if len(texto) > 24:
        if parametro == 'usuario':
            print('[C] O usuário não pode ultrapassar 24 dígitos!')
        elif parametro == 'senha':
            print('[C] A senha não pode ultrapassar 24 dígitos!')
        return False
    else:
        return True
