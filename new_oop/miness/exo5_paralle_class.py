# parellelepipede class definition
from exo5_rect import Rectangle

class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur) -> None:
        super().__init__(longueur, largeur)
        self.hauteur = hauteur

    def getVolume(self):
        return self.getAire() * self.hauteur
