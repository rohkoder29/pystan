#!/usr/bin/env python3

'''

'''

__author__ = 'rohkoder'
__version__ = '0.1.0'
__license__ = 'MIT'

# import
from math import factorial

class Calcul:
    def __init__(self, nombre) -> None:
        self.nombre = nombre

    def getFactorielle(self):
        return factorial(self.nombre)

    def getListDiviseur(self):
        return [i for i in range(1, self.nombre + 1) if self.nombre % i == 0]

    def getNombrePremier(self):
        return len(self.getListDiviseur()) == 2

def main():
    '''  '''
    nombre1 = Calcul(5)
    print(nombre1.getFactorielle())
    print(nombre1.getListDiviseur())
    print(nombre1.getNombrePremier())


if __name__ == '__main__':
    '''  '''
    main()
