"""Base view."""

from models.tourney import Tourney
from models.player import Player


class View:
    """Chess tournament view."""

    def start_program(self):
        """"""

        print(
            "*******************************************************************************************"
        )
        print(
            "#                                 WELCOME TO CHESS MANAGER                                #"
        )
        print(
            "*******************************************************************************************\n"
        )
        print("Tournament settings: ")
        print("[1] Start tournament.")
        print("[2] Load tournament.")
        print("[3] Update players ranking.")
        print("[4] Add players to Database")
        print("[5] Report menu.")
        print("[0] Main menu.")
        menu = input("Choose your option: ")

        return menu

    def menu_start(self):
        # Manual function needs to be done + respect MVC
        for i in range(90):
            print("-", end="")
        print("\nStarting new tournament:")
        print("[1] Manually instanciate players and tournament data.")
        print("[2] Load players and tournament data.")
        while True:
            menu = input("Choose your option: ")
            if menu == "1":
                pass
            if menu == "2":
                pass

    def ask_continue(self):
        while True:
            ask = input("\nStart the next round ? [Y/N] ").upper()
            if ask != "y".upper() and ask != "n".upper():
                print("Invalid input.")
            elif ask == "y".upper():
                break
            elif ask == "n".upper():
                exit()

        return ask

    def prompt_ranking(self, players):
        for i in range(len(players)):
            update_rank = int(
                input(
                    f"Update rank for: {players[i].first_name}, rank: {players[i].ranking}\t+ "
                )
            )

        return update_rank

    def generate_tournament(self):
        # Peut mettre dans Tourney
        tournament_name = input("Entrez le nom du tournois: ")
        Tourney.name = tournament_name
        tournament_location = input("Entrez le lieu du tournois: ")
        Tourney.location = tournament_location
        tournament_date = input(
            "Entrez la date du tournois: (en format Mois/Jour/Année)"
        )
        Tourney.date = tournament_date
        tournament_rounds = int(input("Entrez le nombre de rounds: "))
        Tourney.number_of_rounds = tournament_rounds
        tournament = Tourney(
            tournament_name, tournament_location, tournament_date, tournament_rounds
        )
        return tournament

    def prompt_tournament(self):
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

    def prompt_players(self):
        for i in range(90):
            print("-", end="")
        print(
            "\nPlayers settings: (if you selected Load tournament before, please use option 2 again)"
        )
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

    def prompt_data(self):

        for i in range(90):
            print("-", end="")
        print("\nReport: ")
        print("[1] Display all players by ranking")
        print("[2] Display all players in alphabetical order.")
        print("[3] Display every tournaments.")
        print("[4] Display players from tournaments (ranking).")
        print("[5] Display players from tournaments (alphabetical)")
        print("[6] Display matchs from Round 2")
        print("[7] Display matchs from Round 3")
        print("[8] Display matchs from Round 4")
        print("[0] Exit the program.")
        menu = input("Choose your option: ")

        return menu

    def add_players_info(self):
        # Renvoie list de joueurs que le controlleur mets dans la DB

        players = []
        player_first_name = str(input("Enter the player's first name: "))
        player_last_name = input(f"Enter {player_first_name}'s last name': ")
        player_dob = int(
            input(f"Enter {player_first_name}'s year of birth (ex: 1992)': ")
        )
        player_genre = input(
            f"Enter {player_first_name}'s' genre [Male/Female/Other] ? "
        )
        player_rank = int(input(f"Enter {player_first_name}'s ranking: "))
        player_id = int(input(f"Enter {player_first_name}'s ID: "))
        player = Player(
            player_first_name,
            player_last_name,
            player_dob,
            player_genre,
            player_rank,
            player_id,
        )
        players.append(player)

        return players

    def display_all_players(self, players):
        print("\nList of every players competing:")
        for player in players:
            print(
                f"{players.index(player)+1}: {player.get('last_name')} {player.get('name')}\
- ID: {player.get('player_id')} - Rank: {player.get('ranking')}"
            )

    def display_all_tournaments(self, tournaments):
        print("\nList of every tournaments:")
        # Utiliser l'ID de la table
        for tourneys in tournaments:
            print(
                f"{tournaments.index(tourneys)+1}: {tourneys.get('name')} - {tourneys.get('location')}\
- {tourneys.get('date')} - Rounds: {tourneys.get('current_round')}"
            )

    def display_players_by_tournaments(self, tournaments):
        print(repr(tournaments))
        for tourneys in tournaments:
            print("=================================================\n")
            print(f"{tourneys.get('name')}")
            for player in tourneys["players"]:
                print(player["name"])
            print("=================================================\n")
