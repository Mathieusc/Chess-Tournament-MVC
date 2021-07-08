"""Base view."""
from models.tourney import Tourney
from models.player import Player
import controllers.base as control

class View:
    """Chess tournament view."""
    def __init__(self):
        pass

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

    def start_program():
        print("*******************************************************************************************")
        print("#                                 WELCOME TO CHESS MANAGER                                #")
        print("*******************************************************************************************\n")
        print("Tournament settings: ")
        print("[1] Start a new tournament.")
        print("[2] Load the previous tournament.")
        print("[0] Exit the program.")

        while True:
            menu = input("Choose your option: ")
            if menu == "1":
                View.menu_start()

            elif menu == "2":
                control.Controller.load_tournament()
            elif menu == "0":
                exit()
            else:
                print("Invalid input, please try again.")

    def menu_start():
        print("\n-----------------------------------------------------------------------------------------")
        print("Starting new tournament:")
        print("[1] Manually instanciate players and tournament data.")
        print("[2] Load players and tournament data.")
        while True:
            menu = input("Choose your option: ")
            if menu == "1":
                tournament = View.prompt_tournament()
                View.loading()
                return tournament 
            if menu == "2":
                # tournament = Tourney("Grand Chess Tour", "London", "June 06, 2021", 4)
                # print(f"{tournament.name} \nLocation: {tournament.location}\nDate: {tournament.date}\nNumber of rounds: {tournament.number_of_rounds}\n")
                # return tournament

                control.Controller.start_tournament()
                

    def start():
        start_tournament = True
        return start_tournament

    def load():
        load_tournament = True
        return load_tournament

    def ask_continue():
        while True:
            ask = input("\nRound done, start the next round ? [Y/N] ").upper()
            if ask != "y".upper() and ask != "n".upper():
                print("Invalid input.")
            elif ask == "y".upper():
                break
            elif ask =="n".upper():
                exit()

        return ask