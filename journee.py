import datetime

class Journee:
    def __init__(self):
        self.minute = 0
        self.heure = 12
        self.indexJourSemaine = 0
        self.indexJourDuMois = 1
        self.tabJour = ("Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche")
        self.nomJourSemaine = self.tabJour[self.indexJourSemaine]
        self.annee = 1
        self.indexMois = 0  # janvier
        self.mois_de_l_annee = [
            "Janvier", "Février", "Mars", "Avril", "Mai", "Juin",
            "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"
        ]

        self.jourParMois = {
            "Janvier": 31, "Février": 28, "Mars": 31, "Avril": 30,
            "Mai": 31, "Juin": 30, "Juillet": 31, "Août": 31,
            "Septembre": 30, "Octobre": 31, "Novembre": 30, "Décembre": 31
        }

    def __str__(self):
        minute_str = f"{self.minute:02d}"
        return (f"📅 {self.nomJourSemaine} {self.indexJourDuMois} "
                f"{self.mois_de_l_annee[self.indexMois]}, année {self.annee} ⏰ {self.heure}:{minute_str}")

    def avanceMinute(self, minutes_a_ajouter):
        """Avance le temps avec des minutes"""
        self.minute += minutes_a_ajouter

        # Avancer les heures si minutes >= 60
        while self.minute >= 60:
            self.minute -= 60
            self.heure += 1

        # Avancer les jours si heures >= 24
        while self.heure >= 24:
            self.heure -= 24
            self.avanceJour()

    def avanceJour(self):
        """Avance le temps d'un jour complet"""
        # Gestion des jours
        self.indexJourDuMois += 1
        self.indexJourSemaine = (self.indexJourSemaine + 1) % 7
        self.nomJourSemaine = self.tabJour[self.indexJourSemaine]

        # Gestion des mois
        nom_mois = self.mois_de_l_annee[self.indexMois]
        if self.indexJourDuMois > self.jourParMois[nom_mois]:
            self.indexJourDuMois = 1
            self.indexMois += 1

            # Gestion des années
            if self.indexMois > 11:
                self.indexMois = 0
                self.annee += 1

    def avanceDatePrecise(self, annee: int, indexMois: int, jourDuMois: int, heure: int, minutes: int):
        """Avance la date à un jour bien précis. Le jour de la semaine est calculé automatiquement."""

        # Vérifications de base pour éviter les erreurs
        if not (0 <= indexMois < 12):
            raise ValueError("indexMois doit être entre 0 (Janvier) et 11 (Décembre)")
        nom_mois = self.mois_de_l_annee[indexMois]
        if not (1 <= jourDuMois <= self.jourParMois[nom_mois]):
            raise ValueError(f"{nom_mois} n'a que {self.jourParMois[nom_mois]} jours")
        if not (0 <= heure < 24):
            raise ValueError("heure doit être entre 0 et 23")
        if not (0 <= minutes < 60):
            raise ValueError("minutes doit être entre 0 et 59")

        # Affectation des valeurs principales
        self.indexJourDuMois = jourDuMois
        self.indexMois = indexMois
        self.annee = annee
        self.heure = heure
        self.minute = minutes

        # Calcul automatique du jour de la semaine (0 = Lundi, ..., 6 = Dimanche)
        mois_reel = indexMois + 1  # datetime attend 1 à 12 pour les mois
        jour_semaine = datetime.date(self.annee, mois_reel, jourDuMois).weekday()
        self.indexJourSemaine = jour_semaine
        self.nomJourSemaine = self.tabJour[self.indexJourSemaine]

    def dateDuJour(self) -> tuple:
        """Retourne la date sous forme de tuple (année, mois, jour, heure, minute)"""
        return (self.annee, self.indexMois, self.indexJourDuMois, self.heure, self.minute)

    def dateDuJourSansHeures(self) -> tuple:
        """Retourne uniquement (année, mois, jour) pour des comparaisons de date simple"""
        return (self.annee, self.indexMois, self.indexJourDuMois)


# --- Exemple d'utilisation ---
if __name__ == "__main__":

    # Dictionnaire des rendez-vous avec (année, mois, jour) comme clé
    rdvs = {
        (1, 5, 20): "Vaccin du bébé",
        (1, 5, 25): "Salle du royaume"
    }

    # Création de l'objet
    jour_test = Journee()
    
    # Avance à une date précise (le jour de la semaine sera automatiquement correct)
    jour_test.avanceDatePrecise(1, 5, 20, 10, 10)

    # Affiche la date du jour
    print(jour_test)

    # Vérifie s'il y a un événement
    if jour_test.dateDuJourSansHeures() in rdvs:
        print(f"📌 Événement aujourd’hui : {rdvs[jour_test.dateDuJourSansHeures()]}")
    else:
        print("Aucun évènement aujourd'hui")
