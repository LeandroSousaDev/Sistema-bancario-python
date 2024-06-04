saldo = 0
opcao = 0
limite = 500
extrato = ""
numero_saque = 0
LIMETE_SAQUES = 3

menu = '''
*** OPÇÕES ***
1- Depositar;
2- Sacar;
3- Extrato;
4- Sair;
'''

while True:
    opcao = int(input(menu)) 
    
    if(opcao == 1):
        valor = int(input('Digite o valor que deseja depositar'))

        if(valor > 0):
            saldo += valor
            extrato += f"Depodito: R${valor: .2f} \n"
        else:
            print('O valor deve ser um numero positivo')

    elif(opcao == 2):
        valor = int(input('Digite o valor que deseja sacar'))

        if(valor > saldo):
            print('Saldo insuficiente');
        
        elif(valor > limite):
            print('valor não deve ultrapassa o limite de R$500,00');
        
        elif(numero_saque >= LIMETE_SAQUES):
            print('voce ecedeu o limete de saques diario');
        
        elif(valor > 0):
            saldo -= valor
            extrato += f'Extrato: R${valor: .2f} \n'
            numero_saque += 1;
        
        else:
             print('O valor deve ser um numero positivo');
    
    elif(opcao == 3):
        if(extrato == ""):
            print('Não ouve transferencia')

        else:
            print('\n **** OPÇÃO ****')
            print(extrato)
            print('******************')
            print(f'Saldo: R${saldo: .2f}')
    
    elif(opcao == 4):
        break;
    else:
        print('Opção invalida')