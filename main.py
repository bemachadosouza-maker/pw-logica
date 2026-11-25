import random
numero_secretos = random.randint(1, 20)
tentativas = 0
palpite = int(input(
    "Tente adibinhar um numero entre 1 a 20"))

while palpite != numero_secretos:
    tentativas += 1
    if palpite < numero_secretos:
        print("O numero secreto e maior!")
    else:
        print("O numero secreto e menor!")
        palpite = int(input("Tente novamente:"))
tentativas = 1
print("Parabens! você acertou!")
print(f"O numero secreto era: {numero_secretos}")
print(F"Você utilizou {tentativas} Tentativas.")