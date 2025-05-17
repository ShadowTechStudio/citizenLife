import random
from enum import Enum

class Genre(Enum):
    """Sexe du joueur"""
    HOMME = "Homme"
    FEMME = "Femme"
    AUTRE = "Autre"

class TypePersonne(Enum):
    """Type de personne en fonction de son age"""
    BEBE = "bébé"
    PETIT_ENFANT = "petit enfant"
    ENFANT = "enfant"
    ADOLESCENT = "adolescent"
    JEUNE_ADULTE = "jeune adulte"
    ADULTE = "adulte"
    SENIOR = "senior"
    PERSONNE_AGEE = "personne âgée"
    


class Genre(Enum):
    HOMME = "Homme"
    FEMME = "Femme"
    
class Joueur:
    def __init__(self, nom = "Paul", prenom = "Arnaud", sexe = Genre.HOMME):
        self.nom = nom
        self.prenom = prenom
        self.sexe = sexe
        self.age = 0
        self.type = self.assigneTypeDePersonne()
        self.sante = 100
        self.energie = 100
        self.faim = 50
        self.soif = 50
    
    def __str__(self):
        """Retourne par défaut la description de la classe si on fait un print"""
        return f"sexe: {self.sexeDuJoueur()}, nom: {self.nom}, prenom: {self.prenom}, age= {self.age} ans, ❤️  {self.sante}, ⚡ {self.energie}, 🥪 {self.faim}, 🥛 {self.soif}"
    
    def sexeDuJoueur(self):
        """Sexe du joueur"""
        if self.sexe == Genre.HOMME:
            return "♂️"
        else:
            return "♀️"
        
    def vieillir(self):
        """Le joueur viellit de 1 an"""
        self.age += 1
        print("Tu as grandi")
    
    def mourrir(self):
        """Le joueur meurt"""
        print(f"🪦: {self.prenom} {self.nom} est décédé à l'âge de {self.age} ans, c'était un {(self.typeDePersonneEnFonctionAge().value)}")
        
    def augmenteSante(self, sante):
        """Augmente la santé du joueur"""
        self.sante += sante
    
    def diminueSante(self, sante):
        """Diminue la santé du joueur"""
        self.sante -= sante
        if(self.sante <= 0):
            self.mourrir()
    
    def augmenteEnergie(self, energie):
        """Augmente l'énergie du joueur"""
        self.energie += energie
    
    def diminueEnergie(self, energie):
        """Diminue l'énergie du joueur"""
        self.energie -= energie
    
    def augmenteFaim(self, faim):
        """Augmente la faim du joueur"""
        self.faim += faim
    
    def diminueFaim(self, faim):
        """Diminue la faim du joueur"""
        self.faim -= faim
    
    def augmenteSoif(self, soif):
        """Augmente la soif du joueur"""
        self.soif += soif
    
    def diminueSoif(self, soif):
        """Diminue la soif du joueur"""
        self.soif -= soif
    
    def typeDePersonneEnFonctionAge(self) -> TypePersonne:
        """Renvoie le type de personne en fonction de son age"""
        if self.age < 3:
            return TypePersonne.BEBE
        elif self.age < 6:
            return TypePersonne.PETIT_ENFANT
        elif self.age < 12:
            return TypePersonne.ENFANT
        elif self.age < 18:
            return TypePersonne.ADOLESCENT
        elif self.age < 30:
            return TypePersonne.JEUNE_ADULTE
        elif self.age < 60:
            return TypePersonne.ADULTE
        elif self.age < 75:
            return TypePersonne.SENIOR
        else:
            return TypePersonne.PERSONNE_AGEE
    
    def assigneTypeDePersonne(self):
        """Assigne lee type de personne en fonction de l'age et de son vieillissement"""
        if self.age < 3:
            self.type = TypePersonne.BEBE.value
        elif self.age < 6:
            self.type =  TypePersonne.PETIT_ENFANT.value
        elif self.age < 12:
            self.type =  TypePersonne.ENFANT.value
        elif self.age < 18:
            self.type =  TypePersonne.ADOLESCENT.value
        elif self.age < 30:
            self.type =  TypePersonne.JEUNE_ADULTE.value
        elif self.age < 60:
            self.type =  TypePersonne.ADULTE.value
        elif self.age < 75:
            self.type =  TypePersonne.SENIOR.value
        else:
            self.type =  TypePersonne.PERSONNE_AGEE.value
        
        

# si le fichier est exécuté directement depuis ce scrip, alors __name__ vaut "__main__".
if __name__== "__main__":
    print("debut du jeu")
    #nomJoueur = input("Choisissez un nom: ")
    #prenomJoueur = input("Choisissez un prénom: ")
    
    joueur = Joueur()
    
    print(f"{joueur.prenom} est né aujourd'hui, un beau bébé de {random.randrange(1,5)} kg")
    print(joueur)
    joueur.vieillir()
    joueur.diminueSante(100)
    print(joueur)
    



        
        
        