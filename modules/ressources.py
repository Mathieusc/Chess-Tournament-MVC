import gc

class Player:
    def __init__(self, first_name, last_name, date_of_birth, gender, ranking):
        # first_name = Prénom, last_name = Nom
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth # YEAR format
        self.gender = gender

        self.ranking = ranking # Séparer ranking de la classe ?

class Ranking:
    # Doit être un entier positif
    def __init__(self, ranking):
        self.ranking = ranking

class Tourney:
    def __init__(self, name, location, date, turns):
        self.name = name
        self.location = location
        self.date = date
        self.turns = turns

    def list_of_players(self):
        """This function will create an empty list and append to it all the instances of players with
        their attributes created from the Player class."""

        list_of_players = []
        for obj in gc.get_objects():
            if isinstance(obj, Player):
                list_of_players.append(obj)

        return list_of_players

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

class Matchs:
    def __init__(self, pair_of_players):
        self.pair_of_players = pair_of_players

    def score(self):
        """
        Gagnant = 1 point
        Perdant = 0 point
        Match nul = 1/2 point
        """
        pass

    def single_match_result(self):
        """Doit être stocké sous un tuple contenant 2 listes;
        chacune contenant 2 éléments: une référence à une instance de joueur
                                      un score
        Les matchs multiples doivent être stockés sous forme de liste sur l'instance du tour.
        """
        pass

    def multiple_match_result(self):
        pass

    def rounds(self):
        """Une instance du tour doit contenir: un champ de nom 'Round 1'...
                                               un champ Date et heure de début et de fin
        tout deux automatiquement remplis lorsque l'utilisateur créer un tour et indique
        qu'il est terminé.
        Les instances de rounds doivent être stockées dans une liste
        sur l'instance de tournoi à laquelle elles appartiennent.
        """
        pass

class GeneratePairsOfPlayers:
    """Système suisse, en gros, séparer en deux les joueurs et mettre le premier du tableau 1
    contre le premier du tableau 2 (joueur 1 vs joueur 5, 2vs6, etc)."""
    def __init__(self, player, ranking):
        self.player = Player()
        self.ranking = Ranking()

    def assign_color(self):
        """Blanc ou noir, équilibrage pas nécessaire mais en échec dans un tournois un joueur 
        ne devrait pas jouer 2 fois la même couleur de suite dans un tournois."""
        pass

class Report:
    """Doit afficher/lister les rapports suivants, pouvoix exporter ultérieurement (si possible).
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



        