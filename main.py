operacao = input(
    "escolha a conversão:\n"
    "1 - celsius para fahreneit\n"
    "2 - quilometros para milhas\n"
    "3 - reais para dolar\n"
    "4 - quilogramas para libras\n")
valor = float(input("Digite o valor que deseja converter: "))
if operacao == "1":
    resultado = (valor * 9/5) + 32
    print(f"resultado: {resultado:.f}°F")