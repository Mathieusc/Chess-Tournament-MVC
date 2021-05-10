import modules

class Player:

    LIST_OF_PLAYERS = []
<<<<<<< HEAD
    ID = 0
=======
>>>>>>> 717fc5dccd47faaadc5690535b33be3811137fc2

    def __init__(self, first_name, last_name, date_of_birth, gender, ranking, score=0):
        # first_name = Prénom, last_name = Nom
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth # YEAR format
        self.gender = gender
<<<<<<< HEAD
=======

        self.ranking = ranking # Séparer ranking de la classe ?

        # Accessing the class attributes (not instance attribute)
        self.LIST_OF_PLAYERS.append(self)

class Ranking:
    # Doit être un entier positif
    def __init__(self, ranking):
>>>>>>> 717fc5dccd47faaadc5690535b33be3811137fc2
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
<<<<<<< HEAD

=======

    def build_first_round(player_1, player_2, score_1, score_2):

        
        round_history = {
                        "Match 1": {player_1:score_1,
                                    player_2:score_2},
                        "Match 2": {player_1:score_1,
                                    player_2:score_2},
                        "Match 3": {player_1:score_1,
                                    player_2:score_2},
                        "Match 4": {player_1:score_1,
                                    player_2:score_2}
        }

        yield round_history

>>>>>>> 717fc5dccd47faaadc5690535b33be3811137fc2

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



        