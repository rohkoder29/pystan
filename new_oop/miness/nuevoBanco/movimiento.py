#


class Movimiento:
    def __init__(self,concepto, cantidad) -> None:
        self.__concepto = concepto
        self.__cantidad = cantidad

    def getConcepto(self)-> str:
        return self.__concepto

    def getCantidad(self) -> float:
        return self.__cantidad
