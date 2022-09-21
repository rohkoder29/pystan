# creer une classe GestionCptB qui se definit par:
# un numero de compte nCompte

from random import uniform


class GestionCptB:
    def __init__(self, idCompte, nomClient) -> None:
        self.idCompte =  idCompte
        self.nomClient = nomClient
        self.soldeCompte = round(uniform(1_000.00, 5_000.00), 2)

    def getSoldeCompte(self):
        return self.soldeCompte

    def versement(self, montant: float) -> float:
        self.soldeCompte += montant
        return self.soldeCompte

    def retrait(self, montant: float) -> float:
        self.soldeCompte -= montant
        return self.soldeCompte

    def affichageInfo(self):
        return f"""
    ID du compte : {self.idCompte.upper()}
    Titulaire    : {self.nomClient.title()}
    Solde Actuel : ${round(self.soldeCompte, 2)}"""

def main():
    """ """
    while True:
        try:
            num_cpt = input("Inserer le numero du compte: ")
            assert len(num_cpt) >= 4
        except AssertionError:
            print("Le numero du compte est compose d'au moins 4 caracteres.")
            continue
        else:
            break
    nom_titu = input("Inserer votre nom de client: ")
    faux_cpt = GestionCptB(num_cpt, nom_titu)
    print(faux_cpt.affichageInfo())
    while True:
        op = input("\nFaire une operation: [1] Versement ou [2] Retrait: ")
        if  op == "1":
            somme = float(input("Saisissez le montant a verser: "))
            faux_cpt.versement(somme)
            break
        elif op == "2":
            while True:
                somme = float(input("Saisissez le montant a retirer: "))
                if faux_cpt.getSoldeCompte() < somme:
                    print("Operation impossible. Pas assez d'argent sur le compte.")
                    continue
                faux_cpt.retrait(somme)
                break
            break
        else:
            print("SVP choisissez une option valide.")
    print("\nEtat du compte apres operation:")
    print(faux_cpt.affichageInfo())
    

if __name__ == "__main__":
    main()
