gastos=[]
for i in range(5):
    gastos.append(int(input("digite seu gasto:")))

gasto_maior = gastos[0]
soma = 0
valor_maior100 = 0

for valor in gastos:
    if valor > gasto_maior:
        gasto_maior=valor
    soma += valor
    if valor>100:
        valor_maior100 += 1
print("O maior gasto foi:", "R$ {:.2f}".format(gasto_maior))
print("A soma dos gastos foi:", "R$ {:.2f}".format(soma))
print("A quantidade de gastos maiores que 100 foi:", valor_maior100)

