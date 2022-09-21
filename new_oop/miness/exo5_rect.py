#!/usr/bin/env python3

'''

'''
__author__ = 'rohkoder'
__version__ = '0.1.0'
__license__ = 'MIT'

# import
import exo5_paralle_class as exo5

class Rectangle:
    def __init__(self, longueur, largeur) -> None:
        self.longueur = longueur
        self.largeur = largeur

    def getPerimetre(self):
        return (self.longueur + self.largeur) * 2

    def getAire(self):
        return self.longueur * self.largeur


def main():
    '''  '''
    rect1 = Rectangle(2, 6)
    print(rect1.getAire())
    print(rect1.getPerimetre())
    print()
    paral1 = exo5.Parallelepipede(2, 6, 3)
    print(paral1.getAire())
    print(paral1.getPerimetre())
    print(paral1.getVolume())


if __name__ == '__main__':
    '''  '''
    main()
