notas = []
soma = 0
for contador in range (5):
    nota = float(input(f"Digite a {contador + 1}ª nota: "))
    notas.append(nota)
    soma += nota

    if contador == 0:
        maior = nota
        menor = nota
    else:
        if nota > maior:
            maior = nota
        if nota < menor:
            menor = nota

media = soma / len(notas)