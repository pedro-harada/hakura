lista = []
   
def somar(lista):
    soma = 0
    for n in lista:
        soma += n
    return soma

def definir_menor(lista):
    menor = lista[0]
    for n in lista:
        if n < menor:
            menor = n
    return menor

def definir_maior(lista):
    maior = lista[0]
    for n in lista:
        if n > maior:
            maior = n
    return maior

    
while True:
    print("1 - adicionar numero")
    print("2 - mostrar soma")
    print("3 - mostrar menor")
    print("4 - mostrar maior")
    print("5 - mostrar numeros")
    print("0 - sair")
    opcao = int(input(" selecione uma opção: "))
    

    if opcao == 1:
        lista.append(int(input("Digite um numero:")))
    elif opcao == 2:
        if len(lista) == 0:
            print("nenhum numero foi digitado")
        else:
            print("A soma é: ", somar(lista))

    elif opcao == 3:
        if len(lista) == 0:
            print("nenhum numero foi digitado")
        else:
            print("O menor numero é:", definir_menor(lista))
    elif opcao == 4:
        if len(lista) == 0:
            print("nenhum numero foi digitado")
        else:    
            print("O maior numero é:", definir_maior(lista))
    elif opcao == 5:
        if len(lista) == 0:
            print("nenhum numero foi digitado")
        else:
            print(lista)
    elif opcao == 0:
        print("saindo...")
        break
    else:
        print("opcao invalida")
    