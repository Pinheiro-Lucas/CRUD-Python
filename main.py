# Importando o Sistema CRUD (organização)
import json

from create import *
from read import *
from update import *
from delete import *

# Biblioteca(s) necessária(s)
import os

def main():
    # Armazena as informações em um json (bem simples mesmo)
    if not os.path.isfile('db.json'):
        with open('db.json', 'w') as db:
            json.dump({}, db)
            db.close()

    # Mostra o menu das opções
    print("""
    \t[C] Create
    \t[R] Read
    \t[U] Update
    \t[D] Delete
    \t[E] Exit
    """)

    # Força a escolha de uma opção válida
    opcao = None
    while opcao not in ('C', 'R', 'U', 'D', 'E'):
        opcao = input("Escolha uma das opções: ").upper()

    os.system('cls')  # Caso esteja no CMD
    print('\n')  # Apenas por questões de toc

    # Resumindo 500 if else em duas linhas =)
    opcoes = {'C': create, 'R': read, 'U': update, 'D': delete, 'E': exit}
    opcoes[opcao]()


# Execução padrão do main.py
if __name__ == '__main__':
    while True:
        main()
