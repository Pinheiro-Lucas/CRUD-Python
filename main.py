# Importando o Sistema CRUD (organização)
from create import *
from read import *
from update import *
from delete import *

def main():
    # Mostra o menu
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
        opcao = input("Escolha uma opção: ").upper()

    # Resumindo 500 if else em duas linhas =)
    opcoes = {'C': create, 'R': read, 'U': update, 'D': delete, 'E': exit}
    opcoes[opcao]()


# Execução padrão do main.py
if __name__ == '__main__':
    main()
