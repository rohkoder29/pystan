#


class Cliente:
    def __init__(self, dni, nombre, apellidos) -> None:
        self.__dni = dni
        self.__nombre = nombre
        self.__apellidos = apellidos

    def getDNI(self) -> str:
        return self.__dni

    def getNombre(self) -> str:
        return self.__nombre

    def getApellidos(self) -> str:
        return self.__apellidos

    def __repr__(self) -> str:
        return f'dni:{self.__dni},nombre:"{self.__nombre}",apellidos:"{self.__apellidos}"'
