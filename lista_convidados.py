nomes = []

while True: 
    print('\n1. Adcicionar nome')
    print('2. Buscar nome')
    print('3. Listar nome')
    print('4. Exluir nome da lista')
    print('5. Sair')

    opcao = input('\nEscolha uma opção: ')

    if opcao == '1':
        nome = input('\nDigite seu nome: ')
        nomes.append(nome)
        print(f'\n{nome} foi adicionado na lista')

    elif opcao == '2':
        if nomes:
            print('\n nomes na lista: ') 
            for nome in nomes:
                print(f' - {nome}')
        else:
            print('\na lista esta vazia!')   

    elif opcao == '3':
        buscar = input('\nDigite seu nome: ')
        if buscar in nomes:
            print(f'\n{nome} seu nome esta na lista')
        else:
            print('\nvoce nao foi convido')

    elif opcao ==  '4':
        if nomes:
            exclui = input('\nDigite o nome da pessoa: ')
            if exclui in nomes:
                nomes.remove(exclui)
                print(f'\nVoce exclui {exclui} da lista')
            else:
                print('\nesse nome nao esta na lista')
        else:
            print('\nA lista esta vazia nao tem nome para remover')


    elif opcao == '5':
        print('\nSaindo...')
        break