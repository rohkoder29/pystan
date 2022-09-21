#!/usr/bin/env python3

'''

'''

__author__ = 'rohkoder'
__version__ = '0.1.0'
__license__ = 'MIT'

# import

from xml import dom


class Domino:
    def __init__(self, cote_1, cote_2) -> None:
        self.cote_1 = cote_1
        self.cote_2 = cote_2

    def getPoints(self):
        return (self.cote_1, self.cote_2)

    def getSommePoints(self):
        return sum(self.getPoints())

def main():
    '''  '''
    dom1 = Domino(5, 2)
    print(dom1.getPoints())
    print(dom1.getSommePoints())
    dom2 = Domino(4, 5)
    print(dom2.getPoints())
    print(dom2.getSommePoints())
    print(dom1.getSommePoints() + dom2.getSommePoints())


if __name__ == '__main__':
    '''  '''
    main()
