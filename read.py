import json

def read(printar=True):
    # Lê o banco de dados (nesse caso apenas um json)
    with open('db.json', 'r') as db:
        info = json.load(db)

    # Caso precise das informações em outras funções
    if not printar:
        return info

    # Printa as informações (usuários + senha)
    print(info)  # Preciso melhorar a apresentação
