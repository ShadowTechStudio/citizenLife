import os

class Menu:

    def showMenu(self):
        """Affiche le menu principal."""
        self.efface_ecran()
        while True:
            print("\n ==== Menu Principal ====")
            print("1. Nouvelle partie")
            print("2. Charger une partie")
            print("3. Options")
            print("4. Crédits")
            print("5. Quitter le jeu")
            
            choice = input("\nChoisissez une option : ")
            
            if choice == '1':
                self.nouvelle_partie()
            elif choice == '2':
                self.charger_partie()
            elif choice == '3':
                self.options()
            elif choice == '4':
                self.credits()
            elif choice == '5':
                self.efface_ecran()
                print("Merci d'avoir joué à bientôt 👋")
                break
            else:
                print("Choix invalide. Veuillez réessayer.")
    
    def nouvelle_partie(self):
        """Lance une nouvelle partie"""
        self.efface_ecran()
        print("Lancement du jeu...")

    def charger_partie(self):
        """Affiche les instructions du jeu."""
        self.efface_ecran()
        print("Aucune partie enregistrée, veuillez créer une nouvelle partie")
        self.appuyer_pour_revenir_menu()


    def options(self):
        """Permet de modifier les options du jeu."""
        self.efface_ecran()
        print("Modification des options...")
        self.appuyer_pour_revenir_menu()


    def credits(self):
        """Affiche les crédits."""
        self.efface_ecran()
        print("Crédits :")
        print("Développé par Shadow Tech Studio © 2025")
        self.appuyer_pour_revenir_menu()

    
    def appuyer_pour_revenir_menu(self):
        """retour au menu principal avec un message"""
        input("\nAppuyer sur Entrée pour revenir au menu principal...")

        self.efface_ecran()
        self.showMenu()
    
    def efface_ecran(self):
        if os.name == "nt":
            (os.system("cls"))
        

# Exemple d'utilisation de la classe Menu
if __name__ == "__main__":
    
    menu = Menu()
    menu.showMenu()
    

