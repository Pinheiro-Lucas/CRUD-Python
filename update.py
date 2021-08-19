from read import read
from create import checar_digitos

import json

def update():
    # Lê o banco
    db = read(printar=False)

    # Força a escolha de uma das opções
    escolha = None
    while escolha not in ('1', '2', 'E'):
        escolha = input("""
        \tVocê deseja alterar o usuário ou a senha? 
        \t[U] Usuário 
        \t[S] Senha
        \t[E] Exit
        \t> """).upper()

    # Mudar o nome de usuário
    if escolha == 'U':
        usuario = input('[U] Insira o usuário antigo: ')
        # Checa se o usuário realmente existe no banco
        if usuario in db.keys():
            novo_user = input('[U] Insira o novo usuário: ')
            if checar_digitos(novo_user, 'usuario'):
                confirmar = input('[U] Para confirmar, insira a senha: ')
                # Checa se a senha bate com a senha atual do usuário
                if confirmar == db.get(usuario):
                    # Atualiza a senha do usuário
                    db.pop(usuario)
                    db.update({novo_user: confirmar})
                    # Salva o arquivo
                    json.dump(db, open('db.json', 'w'))
                    # Mensagem de sucesso
                    print('[U] Usuário alterado!')
                else:
                    print('[U] Senha incorreta!')
        else:
            print('[U] Usuário não encontrado!')

    # Mudar a senha
    elif escolha == 'S':
        usuario = input('[U] Insira o usuário: ')
        # Checa se o usuário realmente existe no banco
        if usuario in db.keys():
            nova_senha = input('[U] Insira a nova senha: ')
            if checar_digitos(nova_senha, 'senha'):
                confirmar = input('[U] Para confirmar, insira a senha antiga: ')
                # Checa se a senha bate com a senha atual do usuário
                if confirmar == db.get(usuario):
                    db.update({usuario: nova_senha})
                    # Salva o arquivo
                    json.dump(db, open('db.json', 'w'))
                    # Mensagem de sucesso
                    print('[U] Senha alterada!')
                else:
                    print('[U] Senha incorreta!')
        else:
            print('[U] Usuário não encontrado!')

    # Se a opção for de saída
    elif escolha == 'E':
        exit()
