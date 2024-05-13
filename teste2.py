"""Código que conta os números maiores que 60. Contagem de números maiores que 60"""
numeros = input('Insira os números da lista, separados por espaço: ')
listaNumeros = numeros.split()


def maior_60():
    """conta se maior que 60"""
    contador = 0
    for i, numeros in enumerate(listaNumeros):
        listaNumeros[i] = int(listaNumeros[i])
        if listaNumeros[i] >= 60:
            contador = contador+1
    print('Total de números maior ou igual a 60 é', contador)


maior_60()
