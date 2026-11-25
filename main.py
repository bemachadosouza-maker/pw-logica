nome1 = input("Digite seu nome: ")
peso = float(input("Digite seu peso em KG: "))
altura = float(input("Digite sua altura: "))

resultado = peso / (altura ** 2)

print(f"Olá {nome1}, seu indice de massa corporal é {resultado}")