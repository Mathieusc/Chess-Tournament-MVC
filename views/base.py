"""Base view."""
from models.tourney import Tourney
from models.player import Player


class View:
    """Chess tournament view."""

    def prompt_tournament():
        tournament_name = input("Entrez le nom du tournois: ")
        Tourney.name = tournament_name
        tournament_location = input("Entrez le lieu du tournois: ")
        Tourney.location = tournament_location
        tournament_date = input("Entrez la date du tournois: (en format Mois/Jour/Année)")
        Tourney.date = tournament_date
        tournament_rounds = int(input("Entrez le nombre de rounds: "))
        Tourney.number_of_rounds = tournament_rounds
        tournament = Tourney(tournament_name, tournament_location, tournament_date, tournament_rounds)
        return tournament

    def generate_player():
        players = []
        player_1_name = input("Entrez le prénom du joueur 1: ")
        player_1_last_name = input(f"Entrez le nom de {player_1_name}: ")
        player_1_dob = int(input(f"Entrez l'année de naissance de {player_1_name}: "))
        player_1_genre = input(f"Quel est le genre de {player_1_name} (ex: Homme/Femme) ? ")
        player_1_rank = int(input(f"Entrez le classement de {player_1_name}: "))
        player_1 = Player(player_1_name, player_1_last_name, player_1_dob, player_1_genre, player_1_rank)
        players.append(player_1)

        return players