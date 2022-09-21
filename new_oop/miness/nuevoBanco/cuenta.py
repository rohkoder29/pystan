#
from movimiento import Movimiento


class Cuenta:
    def __init__(self, numero, titular) -> None:
        self.__numero = numero
        self.__titular = titular
        self.__movimientos = []
        self.__saldo = 0.00

    def getNumero(self) -> int:
        return self.__numero

    def getTitular(self) -> str:
        return self.__titular

    def getSaldo(self) -> float:
        return self.__saldo

    def setNuevoMovimiento(self, concepto, cantidad) -> None:
        self.__movimientos.append(Movimiento(concepto, cantidad))
        if concepto == "Retiro":
            self.__saldo -= cantidad
        else:
            self.__saldo += cantidad
