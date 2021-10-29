# pour encore plus documenter votre code utilisez les annotations
from typing import *


class Sommet:
    def __init__(self, nom: Union[int, str]) -> "Sommet":
        """ un sommet à plusieurs attributs:
        nom : entier ou str (IntStr) qui doit être unique c'est le nom du sommet
        voisin : dictionnaire dont les clés sont les voisins et les valeurs la longueur de l'arête
        visited : flag qui permet de marquer qu'un sommet à été visité
        predeceseur : Sommet predecesseur du sommet (utile pour dijkstra)
        distance : distance du sommet à son predecesseur (utile pour dijkstra)"""
        self.nom = nom
        self.voisins: dict["Sommet"] = {}
        self.predecesseur: Union["Sommet", None] = None
        self.visited: bool = False

    def add_voisin(self, voisin: "Sommet", distance: int = 1) -> None:
        """Ajoute un Sommet "voisin" au dictionnaire des voisins et ajoute self au voisin de
        Sommet """
        if isinstance(voisin,Sommet):
            self.voisins[voisin] = distance
            voisin.voisins[self] = distance
        else:
            raise TypeError

    def change_distance_voisin(self, voisin: "Sommet", distance: int = 1) -> None:
        """Change la distance à un voisin s'il existe"""
        if self.voisins.get(voisin) is not None:
            self.add_voisin(voisin, distance)
        else:
            raise ValueError

    def del_voisin(self, voisin: "Sommet") -> None:
        """Supprime s'il existe un Sommet "voisin" au dictionnaire des voisins et supprime self des voisins de "voisin" """
        sommet_voisin: "Sommet" = self.voisins.get(voisin)
        if sommet_voisin is not None:
            del self.voisins[sommet_voisin]
            del sommet_voisin.voisins[self]

    def __str__(self) -> str:
        """Retourne le nom du sommet sous la forme d'une chaine de caractères"""
        return str(self.nom)

    def __len__(self):
        """retourne le degré d'un sommet"""
        return len(self.voisins)

    def voisins_str(self) -> str:
        """retourne la liste des voisins sous la forme d'une chaîne de caractères
        [voisin1, voisin2, ....]"""
        s = "["
        if len(self) == 0:
            return "[]"
        for v in self.voisins.keys():
            s += f"({v},{self.voisins[v]}), "
        s = s[:-2] + "]"
        return s


def main():
    s0 = Sommet(0)
    s1 = Sommet(1)
    s2 = Sommet(2)
    # test __str__
    print("test __str__")
    print(s0, s1, s2)
    assert s0.__str__() == "0" and s1.__str__() == "1" and s2.__str__() == "2"
    print("test __str__ OK")
    # test add_voisin
    print("\ntest add_voisin")
    s0.add_voisin(s1)
    assert s1 in s0.voisins and s0 in s1.voisins
    s0.add_voisin(s2, 4)
    assert s2 in s0.voisins and s0.voisins[s2] == 4 and s0 in s2.voisins and s2.voisins[s0] == 4
    try:
        s0.add_voisin(1)
        raise ValueError
    except:
        pass
    print("test add_voisin OK\n")
    print("test change_distance_voisin")
    s0.change_distance_voisin(s1, 3)
    assert s0.voisins[s1] == 3 and s1.voisins[s0] == 3
    print("test change_distance_voisin OK\n")
    print("test voisins__str__")
    print(f"voisins de {s0.nom} : {s0.voisins_str()}")
    assert s0.voisins_str() == "[(1, 3), (2, 4)]"
    print(f"voisins de {s1.nom} : {s1.voisins_str()}")
    assert s1.voisins_str() == "[(0, 3)]"
    print(f"voisins de {s2.nom} : {s2.voisins_str()}")
    assert s2.voisins_str() == "[(0, 4)]"
    print("test voisins__str__ OK\n")
    print("test del_voisin")
    s0.del_voisin(s1)
    assert s1 not in s0.voisins and s0 not in s1.voisins
    print(f"voisins de {s0.nom} : {s0.voisins_str()}")
    print(f"voisins de {s1.nom} : {s1.voisins_str()}")
    print(f"voisins de {s2.nom} : {s2.voisins_str()}")
    print("test del_voisin OK\n")
    print("Votre classe Sommet a passée les tests avec succès!!!")


if __name__ == '__main__':
    main()
