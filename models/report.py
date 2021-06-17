

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



        