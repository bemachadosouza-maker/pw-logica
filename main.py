print("=== PAR OU IMPAR ===")   
nome1 = input("Nome do jogador 1: ")
nome2 = input("Nome do jogador 2: ")
escolha = input(f"{nome1}. Você escolhe (par/impar): ") .lower()

n1 = int(input(f"{nome1}. seu número: "))
n2 = int(input(f"{nome2}. seu número: "))

soma = n1 + n2
resultado = "par" if soma % 2 -- O else "impar"

print(f"\n{n1} + {n2} = {soma} ({resultado})")

if escolha == resultado:
    print(f"{nome1} ganhou!")
else:
    print(f"{nome2} ganhou!")