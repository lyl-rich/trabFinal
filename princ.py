#
from time import sleep
import defs
import os

afazeres = []

while True:
    defs.título()
    print('''
    1 - Adicionar item
    2 - Exibir lista
    3 - Remover item
    4 - Sair
    ''')
    e = int(input('O que quero fazer: '))


    if e == 1:
        defs.adicionar(afazeres)
    
    elif e == 2:
        defs.exibir(afazeres)
    
    elif e == 3:
        defs.remover(afazeres)
    
    elif e == 4:
        print('Finalizando programa...')
        sleep(2)
        print('Finalizado')
        break
   
    else:
        print('Operação desconhecida')
        sleep(1)
        continue


    
    input('\nAperte qualquer tecla para prosseguir')
    print("...")
    sleep(1)
    os.system('clear')
