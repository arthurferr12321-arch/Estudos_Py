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

CaixaMercado()
