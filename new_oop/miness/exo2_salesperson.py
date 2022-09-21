#!/usr/bin/env python3

'''

'''

# import

__author__ = 'rohkoder'
__version__ = '0.1.0'
__license__ = 'MIT'


class Salesperson:
    def __init__(self, first_name, last_name) -> None:
        self.first_name = first_name
        self.last_name = last_name

    sales = 0

    def makeSale(self, number):
        self.sales += number

    def salesReport(self):
        return f'My total sales are: ${self.sales}.'


def main():
    '''  '''
    miz = Salesperson("Miz", "Wheeler")
    miz.makeSale(450)
    print(miz.salesReport())
    


if __name__ == '__main__':
    '''  '''
    main()
