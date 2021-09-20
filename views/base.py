"""Base view."""

from models.tourney import Tourney
from models.player import Player


class View:
    """
    Chess tournament view.
    """

    def start_program(self):
        """
        Display the main menu.
        """

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

        return input("Choose your option: ")

    def ask_continue(self):
        """
        Ask the user to start the next round or stop the program.

        Return:
            input (str)
        """

        while True:
            ask = input("\nStart the next round ? [Y/N] ").upper()
            if ask != "y".upper() and ask != "n".upper():
                print("Invalid input.")
            elif ask == "y".upper():
                break
            elif ask == "n".upper():
                exit()

        return ask

    def prompt_data(self):
        """
        Report menu.
        """

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
        """
        Input from the user to manually create players for a tournament.

        Return:
            List of players.
        """

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
        """
        Display all players from a tournament in the report menu.
        """

        print("\nList of every players competing:")
        for player in players:
            print(
                f"{players.index(player)+1}: {player.get('last_name')} {player.get('name')}\
- ID: {player.get('player_id')} - Rank: {player.get('ranking')}"
            )

    def display_all_tournaments(self, tournaments):
        """
        Display all tournaments in the report menu.
        """

        print("\nList of every tournaments:")
        # Utiliser l'ID de la table
        for tourneys in tournaments:
            print(
                f"{tournaments.index(tourneys)+1}: {tourneys.get('name')} - {tourneys.get('location')}\
- {tourneys.get('date')} - Rounds: {tourneys.get('current_round')}"
            )

    def display_players_by_tournaments(self, tournaments):
        """
        Display the participants of each tournament in the report menu.
        """

        print(repr(tournaments))
        for tourneys in tournaments:
            print("=================================================\n")
            print(f"{tourneys.get('name')}")
            for player in tourneys["all_players"]:
                print(player["name"])
            print("=================================================\n")

    def first_pairs(self, players):
        """
        Display the pairing matchs for the first round.

        Param:
            player (list) every Player object
        """

        # x = second half of players, pairing first half index versus second half index player.
        x = 4
        for i in range(4):
            print(f"Match {i+1}: {players[i].first_name} VS {players[x].first_name}")
            x += 1
        print()

    def next_pairs(self, players):
        """
        Display the pairing matchs for the next rounds.

        Param:
            player (list) of player tuples.
        """

        print("\nNext round:")
        i = 0
        for player in players:
            print(f"Match {i+1}: {player[0]} VS {player[1]}")
            i += 1

    def first_round_result(self, player):
        """
        Ask the user to enter the player's score (1, 0 or 0.5).

        Param:
            player (list) every Player object
        """

        while True:
            player_result = input(
                (f"Enter the score for:\n{player.ID}: {player.first_name}: ")
            )
            if player_result != "1" and player_result != "0.5" and player_result != "0":
                print("Invalid input, choose between 1, 0.5 or 0.")
            else:
                return float(player_result)

    def next_round_result(self, player):
        """
        Ask the user to enter the player's score.

        Param:
            player (Player object)
        """

        while True:
            player_result = input((f"Enter the score for:\n{player}: "))
            if player_result != "1" and player_result != "0.5" and player_result != "0":
                print("Invalid input, choose between 1, 0.5 or 0.")
            else:
                return float(player_result)

    def update_ranks(self, players):
        """
        Update the ranking attribute from the players.

        Param:
            players (Player objects)
        Return:
            update (float) input from the user
        """

        update = float(
            input(f"Update rank for: {players.first_name}, rank: {players.ranking}\t+ ")
        )

        return update

    def confirm_update(self, players):
        """
        Confirm the ranking update.

        Param:
            players (Player objects)
        """

        print(f"New player's rank -> {players.ranking}")

    def display_tournament_info(self, tournament):
        """
        Display tournament name, location, date and number of rounds.
        NEED TO ADD FORMAT (blitz, bullet...).

        Param:
            tournament (Tourney object)
        """

        print(f"\nThe '{tournament.name}' tournament has started !")
        print(f"Number of rounds: {tournament.number_of_rounds}\n")

    def display_players_ranks(self, players):
        """
        Enumerates each players sorted by their ranks.

        Param:
            players (list) every players
        """

        print("Participants:")
        for player in enumerate(players, 1):
            print(player)
        print("\nInitializing the first round...")

    def display_round_result(self, rounds):
        """
        Display the scores from each players.

        Param:
            rounds (dicts) every matchs
        """

        print("\nRounds result:")
        print(
            str(rounds)
            .replace("{", "")
            .replace("}", "")
            .replace("'", "")
            .replace(",", " -")
        )
        print()

    def display_tournament_ranking(self, global_ranking):
        """
        Display each player's results from the tournament, sorted by scores and ranks

        Param:
            global_ranking (List of tuples) Player, scores and ranks
        """

        print("\nTournament ranking:")
        for player in enumerate(global_ranking, 1):
            print(player)
        print()

    def display_tournament_over(self, tournament):
        """
        Display that the tournament is over if the user tries to load the previous tournament from the main menu.

        Param:
            tournament (Tourney object)
        """

        print(
            f"\n{tournament.name} - Rounds: {tournament.current_round}/{tournament.number_of_rounds}\
                \nThis tournament is over !\n"
        )

    def ask_to_load(self, tournament):
        """
        Display the tournament informations and ask the user to load it.
        """

        print("\nTournament info:")
        print(
            f"{tournament.name} - Location: {tournament.location} - Started: {tournament.date}\
 - Rounds: {tournament.current_round}/{tournament.number_of_rounds}"
        )
        while True:
            ask = input("\nLoad this tournament ? [Y/N] ").upper()
            if ask != "y".upper() and ask != "n".upper():
                print("Invalid input, press 'y' or 'n'")
            elif ask == "y".upper():
                break
            elif ask == "n".upper():
                exit()
