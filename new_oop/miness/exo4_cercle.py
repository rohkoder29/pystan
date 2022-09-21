#!/usr/bin/env python3

'''

'''

# import

__author__ = 'rohkoder'
__version__ = '0.1.0'
__license__ = 'MIT'

from math import pi, pow

class Cercle:
    def __init__(self, rayon) -> None:
        self.rayon = rayon

    def getAire(self):
        return round(pow(pi * self.rayon, 2), 2)

    def getPerimetre(self):
        return round(pi * self.rayon * 2, 2)
    


def main():
    '''  '''
    while True:
        try:
            rayon = float(input("Inserez le rayon du cercle: "))
            assert isinstance(rayon, float) and rayon >= 0.0
        except AssertionError:
            print("SVP inserez une valeur valide.")
            continue
        else:
            break
    cercle1 = Cercle(rayon)
    print(f'Un cercle de rayon {rayon} U a une aire de {cercle1.getAire()} U^2.')
    print(f'Et un perimetre de {cercle1.getPerimetre()} U.')


if __name__ == '__main__':
    '''  '''
    main()
