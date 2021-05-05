import modules

class Player:

    LIST_OF_PLAYERS = []
    ID = 0

    def __init__(self, first_name, last_name, date_of_birth, gender, ranking, score=0):
        # first_name = Prénom, last_name = Nom
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth # YEAR format
        self.gender = gender
        self.ranking = ranking
        type(self).ID += 1
        self.ID = self.ID
        # Accessing the class attributes (not instance attribute)
        self.LIST_OF_PLAYERS.append(self)


class Tourney:
    def __init__(self, name, location, date, number_of_rounds):
        self.name = name
        self.location = location
        self.date = date
        self.number_of_rounds = number_of_rounds


    def match_format(self):
        """
        Bullet = 1 à 2 minutes par joueurs
        Blitz = 3, 5 ou 10 minutes par joueurs (pour tous les tours)
        Speed chess = 15 à 60 minutes par joueurs
        """
        pass

    def director_description(self):
        # Remarques du directeur
        pass

class Report:
    """Doit afficher/lister les rapports suivants, pouvoir exporter ultérieurement (si possible).
    Réfléchir si fonction ou classe."""
    def __init__(self, actors, player, tourney, rounds, matchs):
        self.actors = actors
        self.player = Player()
        self.tourney = Tourney()
        self.rounds = Matchs.rounds()
        self.matchs = Matchs.single_match_result()

    def sort(self):
        # Trier les acteurs et les joueurs par ordre alphabétique et par classement.
        pass


def save_load_data(self):
    # Sauvegarder et charger l'état du programme entre 2 actions de l'utilisateur.
    # Utiliser TinyDB ou juste un dictionnaire Python
    pass



        