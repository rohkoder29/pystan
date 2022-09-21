'''

'''

__author__ = 'rohkoder'
__version__ = '0.1.0'
__license__ = 'MIT'

# imports
from cmath import pi
from math import sqrt

class Punto:
    def __init__(self, coord_x=0, coord_y=0) -> None:
        self.coord_x = coord_x
        self.coord_y = coord_y

    def getCoordX(self) -> int:
        return self.coord_x

    def getCoordY(self) -> int:
        return self.coord_y

    def getCuadrante(self) -> str:
        if self.coord_x == 0:
            if self.coord_y != 0:
                return "El punto esta sobre el eje Y."
            else:
                return "El punto esta ubicado al origen."
        elif self.coord_y == 0:
            return "El punto esta sobre el eje X."
        elif self.coord_x > 0:
            if self.coord_y > 0:
                return "El punto esta en el cuadrante I."
            elif self.coord_y < 0:
                return "El punto esta en el cuadrante IV."
        elif self.coord_x < 0:
            if self.coord_y > 0:
                return "El punto esta en el cuadrante II."
            elif self.coord_y < 0:
                return "El punto esta en el cuadrante III."

    def getVector(self, otra_coord_x, otra_coord_y) -> tuple:
        return otra_coord_x - self.coord_x, otra_coord_y - self.coord_y

    def getDistancia(self, otra_coord_x, otra_coord_y) -> int:
        return sqrt(pow((otra_coord_x - self.coord_x), 2) + pow((otra_coord_y - self.coord_y), 2))

    def __repr__(self) -> str:
        return f"({self.coord_x}, {self.coord_y})"


class Rectangulo:
    def __init__(self) -> None:
        self.punto_inicial = (0, 0)
        self.punto_final = (0, 0)

    def setCoordenadasPunto(self) -> tuple[int, int]:
        x = int(input("Ingrese coordenada x del punto: "))
        y = int(input("Ingrese coordenada y del punto: "))
        return (x, y)

    def getBase(self, x_primer_punto, x_segundo_punto) -> float:
        return x_segundo_punto - x_primer_punto

    def getAltura(self, y_primer_punto, y_segundo_punto) -> float:
        return y_segundo_punto - y_primer_punto

    def getArea(self, altura, base) -> float:
        return altura * base


def main() -> None:
    '''  '''
    punto1 = Punto(int(input("Ingrese coordenada en X del punto: ")), int(input("Ingrese coordenada en Y del punto: ")))
    print(punto1.getCuadrante())
    print()
    punto2 = Punto(int(input("Ingrese coordenada en X del punto 2: ")), int(input("Ingrese coordenada en Y del punto 2: ")))

    vector = punto1.getVector(punto2.getCoordX(), punto2.getCoordY())
    print(f"El vector formado por los puntos {punto1.getCoordX(), punto1.getCoordY()} y {punto2.getCoordX(), punto2.getCoordY()} es: {vector}")

    distancia = punto1.getDistancia(punto2.getCoordX(), punto2.getCoordY())
    print(f"La distancia entre estos puntos es: {distancia} U.")

    print("\n[Creando rectangulo]")
    rect = Rectangulo()
    primer = rect.setCoordenadasPunto()
    segundo = rect.setCoordenadasPunto()
    print()
    print(f"Las coordenadas de la diagonal del rectangulo son: {primer} y {segundo}.")
    rect_base = abs(rect.getBase(primer[0], segundo[0]))
    print(f"Tiene una base de {rect_base} U.")
    rect_altura = abs(rect.getAltura(primer[1], segundo[1]))
    print(f"Una altura de {rect_altura} U.")
    rect_area = rect.getArea(rect_altura, rect_base)
    print(f"Y una area de {rect_area} U cuadrados.")

    


if __name__ == '__main__':
    '''  '''
    main()
