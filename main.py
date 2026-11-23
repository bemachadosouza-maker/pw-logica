
while True:

    print("___Calculadora___\n"
          "1- Somar\n"
          "2- Subtrair\n"
          "3- Multiplicar\n"
          "4- Sair\n")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 4:
        print("Encerrando calculadora...")
        break

    elif opcao == 1:
        print("Você escolheu somar")

        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))

        print("Resultado:", n1 + n2)

    elif opcao == 2:
        print("Você escolheu subtrair")

        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))

        print("Resultado:", n1 - n2)

    elif opcao == 3:
        print("Você escolheu multiplicar")

        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))

        print("Resultado:", n1 * n2)

    else:
        print("Opção inválida!")
    
        