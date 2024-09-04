#
from time import sleep
import os

def título():
    os.system('clear')
    print('\033[7mLISTAGEM\033[m')
    print('-=' * 15)



def adicionar(afazeres):
    os.system('clear')
    print('\033[7mADICIONAR\033[m')
    print('-='*15)
    while True:
        item = str(input('\nDigite seu novo item:\n')).strip()
        afazeres.append(item)
        print(f'\nÍtem "{item}" adicionado com \033[32msucesso\033[m!')
        
        nv = str(input('\nAdicionar outro?')).lower() 
        if nv == 's' and 'sim':
            continue
        elif nv == 'n' and 'nao':
            print('...')
            sleep(1)
            break
        else:
            print('ERRO...')
            sleep(1)
            break



def exibir(afazeres):
   os.system('clear')
   print('\033[7mPRODUTOS CADASTRADOS\033[m')
   print('-='*15)
   for x, item in enumerate(afazeres, 1):
      print(f"{x}. {item}")



def remover(afazeres):
    os.system('clear')
    exibir(afazeres)
    item = int(input("\nDigite o número do item que deseja remover: "))
    confirm = str(input(f"Tem certeza que deseja remover o item {item}?")).lower()
    if confirm == 's' and 'sim':
        if 0 <= item < len(afazeres):
            afazeres.pop(item)
            print(f"\nÍtem {item} removido com \033[32msucesso\033[m!")
        
        else:
            print("\nÍtem inválido.")
    else:
            print("\nRemoção cancelada.")

