from read import read

import json

def delete():
    # Lê o banco
    db = read(printar=False)

    usuario = input('[D] Insira o usuário que deseja deletar: ')
    # Checa se o usuário realmente existe no banco
    if usuario in db.keys():
        senha = input('[D] Para confirmar, insira a senha: ')
        # Checa se a senha bate com a senha atual do usuário
        if senha == db.get(usuario):
            # Apaga o usuário+senha do banco
            db.pop(usuario)
            # Salva o arquivo
            json.dump(db, open('db.json', 'w'))
            # Mensagem de sucesso
            print('[D] Usuário deletado!')
        else:
            print('[D] Senha incorreta!')
    else:
        print('[D] Usuário não encontrado!')
