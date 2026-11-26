alunos = {
    "João" : 8,
    "Maria" : 9,
    "Bernardo" : 5,
    "Pedro" : 6
}
for nome, nota in alunos.items():
    if nota >= 7:
        print(f"[nome] Está aprovado!")
    else:
        print(f"{nome} Esta reprovado!")