def ListaDeProdutos ():


    ListaDeProdutos = []
    CodigoDosProdutos = []

    Quantidade = int(input("Digite a quantidade de produtos que serão cadastrados: "))

    for i in range(Quantidade):
        produto = input("Digite o nome do Produto: ")
        codigo = input(f"Digite o codigo do {produto}: ")

        ListaDeProdutos.append(produto)
        CodigoDosProdutos.append(codigo)

    print(ListaDeProdutos)
    print(CodigoDosProdutos)

def CaixaMercado ():

    """"
        receber valores = float 
        receber ate ser igua a 0
        quantidades de produtos 
        total
        valor medio de cada produto

        entradas : valores
        info acumulada: preços
        repetição: for
        quando digitar 0 finalizar e entregar o resultado
    """

    Valores = []
    i = True

    while i == True:
    
        valor = float(input("Digite o valor (use '0' para valores quebrados): "))
        Valores.append(valor)

        if valor == 0:
            i = False
            totalQuantidade = len(Valores)
            ValorTotal = sum(Valores)
            ValorMedio = sum(Valores) / len(Valores)

            print(f'O total de produto é: {totalQuantidade}')
            print(f'O valor total é: R${ValorTotal}')
            print(f'Valor médio de cada produto: R${ValorMedio}')

def ControleAcesso():
    '''
    Entrada e saida de funcionario
    login e senha
    3 tentativas

    qual condição para permissão de acesso ?: se usuario e senha estiver correto, login efetuado com sucesso
    o que precisa se contado ?: as tentativas
    estrutura de repetição: while
    o que acontece se o usuario acertar antes da 3º tentativa ?
    '''


    logado = False
    login = ""
    senha = ""
    tentativas = 1 
    admin = "admin"
    senha_admin = '1234'
    escolha = 0

    while escolha == 0:
        print("Bem Vindo! \n 1 - Entrar \n 2 - Cadastrar \n 3 - Sair")
        escolha = int(input())

        if escolha > 3:
            print("Opção inexistente")
            escolha = 0

        elif escolha == 1:

            loginI = input("Digite seu Login: ")
            senhaI = input('Digite sua Senha: ')

            if loginI == login:

                while tentativas < 3:
                    if senhaI == senha:
                        print("Logado com sucesso")
                        break


                    elif tentativas > 3:
                        print("Tentativas excedidas")
                        break

                    elif senhaI != senha:
                        print(f"Senha incorreta, tente novamente, Você tem: {3 - tentativas} restantes")
                        tentativas = tentativas + 1
                        senhaI = input(">")



            elif loginI == 'admin' and senhaI == senha_admin:
                print('Admin logado com sucesso')

            else:
                print("Login não encontrado")
                escolha = 0

        elif escolha == 2:
            loginI = input("Digite o seu nome: ")
            senhaI = input("Crie uma senha: ")

            login = loginI
            senha = senhaI
            print("Cadastro concluido!")
            escolha = 0

        elif escolha == 3:
            print("saindo")

def Sistema_De_Nota():
    '''
    sistema pra ver o aluno aprovado e o reprovado
    '''

    Notas = []
    Alunos = []
    Situacao = []
    situation = ''

    AlunosQuantidade = int(input("Digite a quantidade de alunos: "))

    for i in range(AlunosQuantidade):

        print('Nome do Aluno')
        NomeAluno = input('> ')
        Alunos.append(NomeAluno)

        print(f'Nota do {NomeAluno}')
        nota = float(input('> '))
        Notas.append(nota)

        if nota >= 7:
            situation = 'Aprovado'
            Situacao.append('Aprovado')

        else:
            situation = 'Reprovado'
            Situacao.append('Reprovado')

    for NomeAluno, nota, situation in zip(Alunos, Notas, Situacao):
        print(f'{NomeAluno}: {nota:.1f} - {situation}')


def estacionamento():
    '''
    ate 1 hora = 8 reais
    de 1 ate 3 horas 15 reais
    3 horas pra cima é 20 reais
    '''

    i = True
    Carros = []
    total = []

    while i == True:

        print('1 - cadastrar veiculo \n2 - saida de veiculo \n3 - verificar valores \n4 - sair')
        escolha = int(input('> '))

        if escolha == 1:
            print("Digite o placa do veiculo")
            placa = input('> ')
            Carros.append(placa)

        elif escolha == 2:
            print('Digite a placa do veiculo')
            placa = input('> ')

            try:
                Carros.remove(placa)

            except:
                print('Carro não cadastrado')

            else:
                print('quanto tempo esse carro ficou no estacionamento ?(ex: 2)\nSe for menos que 1 hora digite 1')
                tempo = int(input('> '))

                if tempo == 1:
                    print('Cliente fico 1 hora ou menos \nValor a pagar R$8,00\n')
                    total.append(8.00)

                elif tempo > 1 and tempo <= 3:
                    print(f'Cliente ficou {tempo} horas \nValor a paagr R$15,00')
                    total.append(15.00)

                elif tempo > 3:
                    print(f'Cliente ficou {tempo} horas \nValor a paagr R$20,00')
                    total.append(20.00)

        elif escolha == 3:
            ValorTotal = sum(total)

            print(f'O total até esse momento é R${ValorTotal}')

def SistemaSenha():
    '''
    zfill - preencher com uma quantidade de zeroa a esquerda:
    ord - transforma a letra em numero
    chr - transforma o numero em letra
    '''

    letra = 'A'
    numero = 1
    ListaDeEspera = []

    while True:

        print('Clinte prioritario ? [Y] - Sim  [N] - Não')
        resposta = input('>')

        if resposta == 'Y' or resposta == 'y':
            letra = 'P'

            troca = str(numero)
            senha = letra + troca
            print('Senha atual:' + letra + troca.zfill(3) + '\n')
            input()
            ListaDeEspera.append(senha)
            print(ListaDeEspera)
            numero =+ 1

        elif resposta == 'N' or resposta == 'n':

            letra = 'C'
            troca = str(numero)
            senha = letra + troca
            print('Senha atual:' + letra + troca.zfill(3) + '\n')
            ListaDeEspera.append(senha)
            print(ListaDeEspera)
            numero =+ 1
            

        else:
            print('Resposta Invalida')
        

def SistemaVendas():

    total = 0.0
    quantidades = 0
    Vendas = 0
    while True:

        print('Bem vindo! \nDigite o Codigo do produto, digite 0 para sair:')
        codigo = int(input('> '))

        if codigo != 0 :
            print('Qual a quantidade ?')
            quantidade = int(input('> '))

            quantidades = quantidade + quantidades

            print('Qual é o valor unitario ?')
            valor = float(input('> '))
            valor = valor * quantidades
            total = valor + total

            if valor > Vendas:
                Vendas = valor

        else:
            print(f'O total de vendas é: {total} \nQuantidades vendidas: {quantidades} \nVenda mais alta foi uam de: R${Vendas}')
            break

def Enel():
    meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    Valores = []
       
    for mes in meses:
           
        print(f'digite o valor de {mes}')
        valor = float(input('R$'))
   
        Valores.append(valor)
   
    for mes, valor in zip(meses, Valores):
        print(f'{mes}: R${valor:.2f}')
   
    total = sum(Valores)
    media = sum(Valores) / len(Valores)
    maximo = max(Valores)
    menor = min(Valores)
   
    print(f"\ntotal - {total}\nmédia - {media}\nmaximo - {maximo}\nminimo - {menor}")
           
def Biblioteca():

    livros = 50

    while True:


        print('Biblioteca Sr. Armando \n1 - Emprestar\n2 - devolver 3 - Consultar quantidade\n4- sair')
        escolha = int(input('> '))

        if escolha == 1:
            if livros == 0:
                print('Sem livros para emprestar')
            else:
                print('Livro emprestado')
                livros =- 1

        elif escolha == 2:
            if livros == 50:
                print('estoque cheio')
            else:
                print('Livro devolvido')

        elif escolha == 3:
            print(f'Estoque: {livros}')

        elif escolha == 4:
            print('Saindo')
            break

        else:
            print('Escolha incorreta')
    



    