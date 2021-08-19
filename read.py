import json

def read(printar=True):
    # Lê o banco de dados (nesse caso apenas um json)
    db = json.load(open('db.json', 'r'))

    # Caso precise das informações em outras funções
    if not printar:
        return db

    # Printa as informações (usuários + senha)
    print(db)  # Preciso melhorar a apresentação
