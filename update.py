from read import *

def update():
    # Lê o banco
    info = read(printar=False)

    # Força a escolha de uma das opções
    escolha = None
    while escolha not in ('1', '2', 'E'):
        escolha = input("""
        \tVocê deseja alterar o usuário ou a senha? 
        \t[1] Usuário 
        \t[2] Senha
        \t[E] Exit
        \t> """).upper()

    # Mudar o nome de usuário
    if escolha == '1':
        usuario = input('Insira o usuário antigo: ')
        # Checa se o usuário realmente existe no banco
        if usuario in info.keys():
            novo_user = input('Insira o novo usuário: ')
            confirmar = input('Para confirmar, insira a senha: ')
            # Checa se a senha bate com a senha atual do usuário
            if confirmar == info.get(usuario):
                # Atualiza a senha do usuário
                info.pop(usuario)
                info.update({novo_user: confirmar})
                # Salva o arquivo
                with open('db.json', 'w') as db:
                    json.dump(info, db)
            else:
                print('Senha incorreta!')
        else:
            print('Usuário não encontrado!')

    # Mudar a senha
    elif escolha == '2':
        usuario = input('Insira o usuário: ')
        # Checa se o usuário realmente existe no banco
        if usuario in info.keys():
            nova_senha = input('Insira a nova senha: ')
            confirmar = input('Para confirmar, insira a senha antiga: ')
            # Checa se a senha bate com a senha atual do usuário
            if confirmar == info.get(usuario):
                info.update({usuario: nova_senha})
                # Salva o arquivo
                with open('db.json', 'w') as db:
                    json.dump(info, db)
            else:
                print('Senha incorreta!')
        else:
            print('Usuário não encontrado!')

    # Se a opção for de saída
    elif escolha == 'E':
        exit()
