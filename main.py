# Importando o Sistema CRUD (organização)
from create import create
from read import read
from update import update
from delete import delete

# Biblioteca(s) necessária(s)
import os
import json

def main():
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
    # Armazena as informações em um json (bem simples mesmo)
    if not os.path.isfile('db.json'):
        with open('db.json', 'w') as db:
            json.dump({}, db)
            db.close()
    # Limpa o CMD (apenas estética)
    os.system('cls')
    # Roda o menu até o usuário escolher sair
    while True:
        main()
