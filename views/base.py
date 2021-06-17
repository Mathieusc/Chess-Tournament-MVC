"""Base view."""
from models.tourney import Tourney


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