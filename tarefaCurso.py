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