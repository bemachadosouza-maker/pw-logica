
print("=== CINEMA ===")

preco = 30.00

dia = input("Qual o dia da semana? ").lower()

tipo = input("Digite inteira ou meia: ").lower()

if tipo == "meia":
    valor = preco * 0.5

elif tipo == "inteira":
    valor = preco

else:
    print("Tipo de ingresso inválido!")
    valor = 0

if dia == "quarta":
    valor = valor * 0.5
    print("Promoção de quarta-feira: 50% de desconto!")

print("===== RESULTADO =====")
print("Valor do ingresso: R$", valor)
