#Programas para entregar:
#1 - Faça um programa que diga se o primeiro e o último ítens de uma lista são iguais(deve funcionar para qualquer lista, ou seja, a quatidade de ítens não é fixa)
#2 - Faça um programa que diga o maior divisor primo de um número dado como input
#3 - Diga se um número qualquer é um palíndromo
#4 - Dê a soma de todos os números primos menores que 1000

#1
def programa1(lista):

    #Verificação de Entrada
    if(type(lista) != list):
        return print("Argumento Inválido.")

    return print(lista[0] == lista[-1])

#2
def programa2(): 

    num = int(input("Escreva um número: "))

    if (num == 0) or (num == 1) or (num == -1):
        return print("Resultado não determinado")

    #Algoritmo adaptado do utilizado nas aulas de Números Inteiros e Criptografia do curso de Ciência da Computação da UFRJ    
    fatorar = abs(num)
    candidato = 2
    while (fatorar > 1):
        while (fatorar % candidato == 0):
            maiorDivisor = candidato
            fatorar /= candidato

        candidato += 1
    
    return print(f"O maior divisor primo de {num} é {maiorDivisor}.")
    

#3
def programa3(num):

    #Verificação de Entrada
    if (type(num) != int) or (num < 0):
        return print("Entrada Inválida.")
    
    if(num < 100):
        if (num < 10) or (int(num/10) == num %10):
            return print(f"O número {num} é palíndromo.")
    else:
        if(int(num/100) == num %10):
            return print(f"O número {num} é palíndromo.")

    return print(f"O número {num} não é palíndromo.")

#4
def programa4():

    primos = crivoEratóstenes(1000)
    soma = sum(primos)
    return print("A soma dos primos menores que 1000 é: {} ".format(soma))

    
def crivoEratóstenes(max):

    numeros = [True] * (max+1)
    numeros[0] = numeros[1] = False
    primos = []

    for index, value in enumerate(numeros):
        if (value == True):  
            primos.append(index)

            for i in range(index,len(numeros),index):
                numeros[i] = False
            

    return primos
