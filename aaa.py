numero = int(input("digite um numero:"))
soma = 0
maior = 0
quantidade = 0
while numero != 0:
    numero = int(input("digite um numero:"))
    if numero == 0:
            break
    soma = soma + numero
    quantidade += 1
    if numero > maior:
             maior = numero
print("a soma dos numeros é:", soma)
print("o maior numero é:", maior)
print("a quantidade de numeros é:", quantidade)
