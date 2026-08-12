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

    AlunosQuantidade = int(input("Digite a quuantidade de alunos: "))

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


