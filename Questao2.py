# # algoritmo para mostrar os números primos existentes em um intervalo.
# -*- coding: utf-8 -*-

import math


def Primo(num):
    if num < 2:
        return False
    
    i = 2
    for i in range(2, int(math.sqrt(num) + 1)):
        if (num % i == 0):
            return False
    return True


def main():
    print("Impressão do Intervalo dos numeros primos")
    inicio = int(input("Inicio: "))
    final = int(input("Final: "))

    for i in range(inicio, final):
        if Primo(i):
            print (i)


if __name__ == '__main__':
    main()