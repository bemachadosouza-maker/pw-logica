nota = float(input("Sua nota: "). replace(".", "."))

if nota >= 9:
    print("Conceito A - Excelente!")
elif nota >= 7:
    print("Conceito B - Bom!")
else:
    print("Conceito D - Reprovado")