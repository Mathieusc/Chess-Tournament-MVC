"""Base view."""
from models.tourney import Tourney
from models.player import Player
from models.datadb import Data
from tinydb import TinyDB, Query
import controllers.base as control

class View:
    """Chess tournament view."""
    def __init__(self):
        pass

    def generate_tournament():
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
        print("[3] Update players ranking.")
        print("[4] Report - Displays all data.")
        print("[0] Exit the program.")

        while True:
            menu = input("Choose your option: ")
            if menu == "1":
                #View.menu_start()
                control.Controller.setup_tournament()
            elif menu == "2":
                #control.Controller.load_tournament()
                control.Controller.load_tournament_data()
            elif menu == "3":
                control.Controller.load_ranking_data()
            elif menu == "4":
                report = View.prompt_data()
            elif menu == "0":
                exit()
            else:
                print("Invalid input, please try again.")

    def menu_start():
        for i in range(90):
            print("-", end="")
        print("\nStarting new tournament:")
        print("[1] Manually instanciate players and tournament data.")
        print("[2] Load players and tournament data.")
        while True:
            menu = input("Choose your option: ")
            if menu == "1":
                # Manual function needs to be done
                control.Controller.start_tournament()
            if menu == "2":
                control.Controller.start_tournament()
                

    def start():
        start_tournament = True
        return start_tournament

    def load():
        load_tournament = True
        return load_tournament

    def ask_continue():
        while True:
            ask = input("\nStart the next round ? [Y/N] ").upper()
            if ask != "y".upper() and ask != "n".upper():
                print("Invalid input.")
            elif ask == "y".upper():
                break
            elif ask == "n".upper():
                exit()

        return ask

    def prompt_ranking(players):
        for i in range(len(players)):
            update_rank = int(input(f"Update rank for: {players[i].first_name}, rank: {players[i].ranking}\t+ "))
        
        return update_rank

    def ask_ranking_change(players, global_ranking, serialize_tournament):
        while True:
            ask = input("Tournament done, update player's ranking ? [Y/N] ").upper()
            if ask != "y".upper() and ask != "n".upper():
                print("Invalid input.")
            elif ask == "y".upper():
                Player.change_player_ranking(players, global_ranking, serialize_tournament)
            elif ask == "n".upper():
                exit()

    def prompt_load_tourney(table):
        while True:
            print("\nData from the previous tournament:")
            #print(table)
            ask = input("Load data ? [Y/N] ").upper()
            if ask != "y".upper() and ask != "n".upper():
                print("Invalid input.")
            elif ask == "y".upper():
                break
            elif ask == "n".upper():
                exit()

    def prompt_tournament():
        for i in range(90):
            print("-", end="")
        print("\nTournament settings:")
        print("[1] Manually create tournament data.")
        print("[2] Load the previous tournament.")
        print("[3] Use the tournament data from file.")
        while True:
            menu = input("Choose your option: ")
            if menu == "1":
                pass
            if menu == "2":
                pass
            if menu == "3":
                pass

    def prompt_players():
        for i in range(90):
            print("-", end="")
        print("\Players settings: (if you selected Load tournament before, please use option 2 again)")
        print("[1] Manually instanciate players.")
        print("[2] Load players from the previous tournament.")
        print("[3] Select players from the databse.")
        while True:
            menu = input("Choose your option: ")
            if menu == "1":
                pass
            if menu == "2:":
                pass
            if menu == "3":
                pass

    def prompt_data():
        table = TinyDB('db.json')
        for i in range(90):
            print("-", end="")
        print("\nReport: ")
        print("[1] Show all.")
        print("[2] Display tournament.")
        print("[3] Display players.")
        print("[4] Display rounds.")
        print("[5] Display matchs from Round 1")
        print("[6] Display matchs from Round 2")
        print("[7] Display matchs from Round 3")
        print("[8] Display matchs from Round 4")
        print("[0] Main menu.")
        while True:
            menu = input("Choose your option: ")
            if menu == "1":
                Data.display_every_tournaments(table)
            if menu == "2":
                Data.display_tournament(table)
            if menu == "3":
                Data.display_players(table)
            if menu == "4":
                Data.display_rounds(table)
            if menu == "5":
                Data.display_matchs_1(table)
            if menu == "6":
                Data.display_matchs_2(table)
            if menu == "7":
                Data.display_matchs_3(table)
            if menu == "8":
                Data.display_matchs_4(table)
            if menu == "9":
                Data.main_table(table)
            if menu == "0":
                View.start_program()
