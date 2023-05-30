saldo = 0
extrato = ''
numero_saques = 0
limite = 500
LIMITE_DE_SAQUE_DIÁRIO = 3

while True:
    menu = '''
        ++++++++++MENU++++++++++
        SELECIONE A OPÇÃO DESEJADA:

        [1] Depósito
        [2] Saque
        [3] Extrato
        [0] Sair

        ++++++++++++++++++++++++
    '''
    opcao = input(menu)

    if opcao == '1': #Depósito
        deposito = float(input('Digite o valor que deseja transferir para sua conta: '))
        if deposito > 0:
            saldo += deposito
            extrato += f'Depósito: R$ {deposito:.2f}\n'
            print('Depósito realizado com sucesso!')
        else:
            print('Depósito recusado, valor inválido.')

    elif opcao == '2': #Saque
        valor = float(input('Informe o valor do saque: '))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saque = numero_saques >= LIMITE_DE_SAQUE_DIÁRIO
        
        if excedeu_saldo:
            print('Operação inválida: Você não possui saldo suficiente.')
        elif excedeu_limite:
            print('Operação inválida: O valor do saque excede o limite da sua conta.')
        elif excedeu_saque:
            print('Operação inválida: Limite de saque diário excedido!')
            
        elif valor > 0:
            saldo -= valor
            extrato += f'Saque: R$ {valor:.2f}\n'
            numero_saques += 1
            print('Saque realizado com sucesso!')
        else: 
            print('Operação inválida: O valor informado é inválido.')

    elif opcao == '3': #Extrato
        print('\n==========EXTRATO==========')
        print('Não foi encontrato nenhum valor na sua conta!' if not extrato else extrato)
        print(f'\nSaldo: R${saldo:.2f}')
        print('===========================')

    elif opcao == '0':
        print('Saindo do sistema...')
        break
    else:
        print('Opção inválida. Tente novamente.')
