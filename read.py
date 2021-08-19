import json
import os

def read(printar=True):
    # Lê o banco de dados (nesse caso apenas um json)
    db = json.load(open('db.json', 'r'))

    # Caso precise das informações em outras funções
    if not printar:
        return db

    # Printa as informações (usuários + senha)
    print("{:<24} {:<24}".format('USUÁRIOS', 'SENHAS'))
    print("{:<24} {:<24}".format('------------------------', '------------------------'))

    for usuario, senha in db.items():
        print("{:<24} {:<24}".format(usuario, senha))

    # Pausa o Prompt para a visualização
    input('\n[R] Enter para voltar ao Menu!')
    os.system('cls')
