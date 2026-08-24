def media(a,b):
    if b > 0:
        media = a / b
        return media
    
    else:
        return 0

def erro001(variavel):
    while True:
        try:
            variavel = input('> ')
            variavel = int(variavel)
            return variavel
        
        except ValueError:
            print('Erro 001: entrada digitada não numerico')

def erro002(variavel):
    while True:
        try:
            variavel = input('>')
            variavel = float(variavel)
            return variavel

        except ValueError:
            print('Erro 002: entrada digitada não numerica float')

def estacionamento():

    clientes = 0
    total = 0.0
    clientes_altos = 0
    totallitros = 0.0

    print('Bem vindo ao sistema do posto')
    while True:
        print('.\nMenu\n1 - atender cliente\n2 - faturamento atual\n3 - Sair\n.')

        choose = erro001('>')

        if choose == 3:
            print('Saindo...')
            return

        elif choose == 1:

            clientes += 1
            print('cliente Nº ', clientes)
            print('Digite a quantidade em litros abastecido')
            abast = erro001('>')

            print(abast, 'abastecido')
            print('Digite o valor do combustivel(valor por litro):')
            valor_litro = erro001('>')

            valor = abast * valor_litro

            print('Total a pagar: R$', valor)
            input()
            
            total = total + valor
            totallitros = totallitros + abast

            

            if abast > 40:
                clientes_altos += 1

        elif choose == 2:

            print('...Faturamento atual...')
            print('Total: R$', total)
            print('Total de clientes atendidos', clientes)
            print('Clientes que abasteceram mais de 40L: ', clientes_altos)
            print(f'Media abastecida por clientes: {media(totallitros, clientes)}')

        else:

            print('Opção incorreta')

def FolhaPagamento():

    funcionarios = {}
    nomes = []

    print('...Folha de pagemento...')
    while True:
        print('1 - Cadastrar funcionario\n2 - Folha de pagamento\n3 - relatorio 4 - sair')
        choose = erro001('>')

        if choose == 4:
            print('Saindo...')
            return

        elif choose == 1:

            print('Digite o nome do funcionario')
            nome = input('> ')
            nomes.append(nome)

            print('Digite o salario bruto de', nome)
            sb = erro002('>')

            print('quantas horas extras registrada ?')
            horas = erro001('>')

            if horas < 1:

                sf = sb

            elif horas == 1:
                sf = sb + 25.00

            elif horas > 1:
                sf = sb + (horas * 25.00)


            funcionarios[nome] = {"salario_bruto": sb, "horas_extras": horas, 'salario_final': sf}

        elif choose == 2:
            
            for chave in funcionarios:
                print(chave, funcionarios[chave]['salario_final'])
                

        elif choose == 3:
            salario = []

            for x in funcionarios.values():
                salario.append(x['salario_final'])

            total = sum(salario)
            qtd = len(nomes)
            print('Média:',media(total, qtd))
            print(f'Total funcionarios: {qtd}')
            print('Maior salario', max(salario))
            print('Menor salario', min(salario))

