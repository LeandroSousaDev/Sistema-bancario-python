def menu():
    menu = '''\n
    *** OPÇÕES ***
    1- Depositar;
    2- Sacar;
    3- Extrato;
    4- Sair;
    '''
    return int(input(menu))

def main():

    LIMITE_SAQUES = 3
    
    
    saldo = 0
    limite = 500
    extrato = ""
    numero_saque = 0


    while True:
        opcao = menu()
        
        if(opcao == 1):
            valor = int(input('\n Digite o valor que deseja depositar '))

            saldo, extrato = depositar(saldo=saldo,
                                       valor=valor,
                                       extrato=extrato)

        elif(opcao == 2):
            valor = int(input('\n Digite o valor que deseja sacar '))

            saldo, extrato, numero_saque = sacar(saldo=saldo,
                                                 valor=valor,
                                                 extrato=extrato, 
                                                 limite=limite, 
                                                 numero_saque=numero_saque, 
                                                 limite_saque=LIMITE_SAQUES)
        
        elif(opcao == 3):
           exbir_extrato(extrato=extrato, saldo=saldo)
        
        elif(opcao == 4):
            break;
        else:
            print('\n Opção invalida')

def depositar(saldo, valor, extrato):

    if(valor > 0):
        saldo += valor
        extrato += f"Depodito: R${valor: .2f} \n"
        print('\n Depósito realizado com sucesso!');
    
    else:
        print('\n O valor deve ser um numero positivo');

    return saldo, extrato;

def sacar(saldo, valor, extrato, limite, numero_saque, limite_saque):

    
    if(valor > saldo):
        print('Saldo insuficiente');
            
    elif(valor > limite):
        print('valor não deve ultrapassa o limite de R$500,00');
            
    elif(numero_saque >= limite_saque):
        print('voce ecedeu o limete de saques diario');
            
    elif(valor > 0):
        saldo -= valor
        extrato += f'Extrato: R${valor: .2f} \n'
        numero_saque += 1
        print('\n Saque realizado com sucesso!')
    
    else:
        print('O valor deve ser um numero positivo');

    return saldo, extrato, numero_saque;

def exbir_extrato(saldo, extrato):
    if(extrato == ""):
        print('Não ouve transferencia')

    else:
        print('\n **** EXTRATO ****')
        print(extrato)
        print('******************')
        print(f'Saldo: R${saldo: .2f}');

main()