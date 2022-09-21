#!/usr/bin/env python3

'''

'''

__author__ = 'rohkoder'
__version__ = '0.1.0'
__license__ = 'MIT'

# imports
from cliente import Cliente
from cuenta import Cuenta
from movimiento import Movimiento


def main() -> None:
    '''  '''
    print('')
    # info del cliente
    def validar_dni() -> int:
        while True:
            try:
                dni = input("Ingrese su DNI: ")
                assert dni.isdigit()
            except AssertionError:
                print("Por favor ingrese un numero de DNI correcto.")
                continue
            else:
                return dni

    def validar_nombre_apellidos() -> dict[str, str]:
        while True:
            try:
                nombre = input("Ingrese su nombre: ")
                apellidos = input("Ingrese su/s apellido/s: ")
                assert nombre.isalpha() and apellidos.isalpha()
            except AssertionError:
                print("Por favor ingrese su nombre / apellido correctamente.")
                continue
            else:
                return {
                    "nombre": nombre,
                    "apellidos": apellidos}

    # info cliente
    dni = validar_dni()
    nombre = validar_nombre_apellidos()
    cliente = Cliente(dni, nombre.get("nombre"), nombre.get("apellidos"))
    # print(cliente)
    print()

    # info cuenta corriente 1
    cuenta1 = Cuenta(1, cliente)
        # movimentos
    cuenta1.setNuevoMovimiento("Deposito", 2_000.00)
    cuenta1.setNuevoMovimiento("Deposito", 1_500.00)
    cuenta1.setNuevoMovimiento("Retiro", 2_200.00)
    print(f"Saldo cuenta #1 : ${cuenta1.getSaldo():,.2f}")

    # info cuenta corriente 2
    cuenta2 = Cuenta(2, cliente)
        # movimientos
    cuenta2.setNuevoMovimiento("Deposito", 1_000.00)
    cuenta2.setNuevoMovimiento("Retiro", 500.00)
    cuenta2.setNuevoMovimiento("Retiro", 200.00)
    print(f"Saldo cuenta #2 : ${cuenta2.getSaldo():,.2f}")

if __name__ == '__main__':
    '''  '''
    main()
