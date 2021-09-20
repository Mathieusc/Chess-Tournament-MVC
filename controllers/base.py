"""Base controller."""

from models.datadb import Data, db
from models.player import Player
from models.tourney import Tourney


class Controller:
    """
    Tournament controller.

    Param:
        View class.
    """

    def __init__(self, view):
        self.view = view

    def run(self):
        """
        Main menu of the program.
        """

        while True:
            main_menu = self.view.start_program()
            if main_menu == "1":
                self.setup_tournament()
            elif main_menu == "2":
                self.load_tournament_data()
            elif main_menu == "3":
                self.load_ranking_data()
            elif main_menu == "4":
                list_players = self.view.add_players_info()
                Player.add_players_to_data(list_players)
                self.run()
            elif main_menu == "5":
                self.run_report()
            elif main_menu == "0":
                exit()
            else:
                print("Invalid input, please try again.")

    def run_report(self):
        """
        Report menu.
        """

        data = Data()
        while True:
            main_menu = self.view.prompt_data()
            if main_menu == "1":
                all_players = data.get_all_players()
                list_players = sorted(
                    all_players, key=lambda player: player.get("ranking"), reverse=True
                )
                self.view.display_all_players(list_players)
                continue
            if main_menu == "2":
                all_players = data.get_all_players()
                list_players = sorted(
                    all_players, key=lambda player: player.get("last_name")
                )
                self.view.display_all_players(list_players)
                continue
            if main_menu == "3":
                tournaments = data.get_tournament()
                self.view.display_all_tournaments(tournaments)
                continue
            if main_menu == "4":
                tournaments = data.get_tournament()
                self.view.display_players_by_tournaments(tournaments)
                continue
            if main_menu == "5":
                tournaments = data.get_tournaments_players()
                continue
            if main_menu == "6":
                Data.display_matchs_2()
                continue
            if main_menu == "7":
                Data.display_matchs_3()
                continue
            if main_menu == "8":
                Data.display_matchs_4()
                continue
            if main_menu == "9":
                Data.main_table()
                continue
            if main_menu == "0":
                break
            else:
                print("INVALID input, please try again.")

    def load_ranking_data(self):
        """
        Load the last tournament data.

        Runs the tournament function that updates the player's ranks.
        """

        load_tourney = Data.get_tournament(db)
        tournament = Tourney.deserialize_tournament(load_tourney[-1])
        rounds = tournament.rounds
        players = Player.get_all_players()
        Players = Player.deserialize_players(players)

        tournament.change_player_ranking(
            Players,
            rounds,
            self.view.display_tournament_ranking,
            self.view.update_ranks,
            self.view.confirm_update,
        )

    def load_tournament_data(self):
        """
        Load the last tournament data.

        Runs the tournament function to continue (if undone) the last tournament.
        """

        load_tourney = Data.get_tournament(db)
        tournament = Tourney.deserialize_tournament(load_tourney[-1])
        if tournament.current_round == 4:
            self.view.display_tournament_over(tournament)
            self.run()
        rounds = tournament.rounds
        # Players
        # load_players = tournament.players
        player_table = Player.get_all_players()
        players = Player.deserialize_players(player_table)
        # Global ranking data
        player_ranks = Player.get_player_name_ranking(players)
        print("player ranks object")
        print(player_ranks)
        print(type(player_ranks))
        get_round_result = tournament.add_scores(rounds)
        sorted_round_result = tournament.sort_scores(get_round_result)
        global_ranking = tournament.display_global_ranking(
            player_ranks, sorted_round_result
        )

        self.view.ask_to_load(tournament)
        self.run_tournament(tournament, players, rounds, global_ranking)

    def setup_tournament(self):
        """
        Initialize the objects to start a tournament.

        Runs the tournament function to execute each rounds and pair players accordingly.
        """

        # Tournament
        tournament = Tourney("Grand Chess Tour", "London", "November 06, 2021")
        tournament.current_round = 1
        serialize_tournament = tournament.serialize_tournament(tournament)
        self.view.display_tournament_info(tournament)

        # To manually create players:
        # players = self.view.prompt_players()
        players = Player.generates_player()
        player_ranks = Player.get_player_name_ranking(players)
        Player.serialize_players(players)
        self.view.display_players_ranks(player_ranks)

        # Generate Rounds
        setup_rounds = tournament.generate_round(tournament.number_of_rounds)
        rounds = tournament.build_first_round(
            setup_rounds, players, self.view.first_pairs, self.view.first_round_result
        )
        get_round_result = tournament.add_scores(rounds)
        self.view.display_round_result(get_round_result)
        sorted_round_result = tournament.sort_scores(get_round_result)
        global_ranking = tournament.display_global_ranking(
            player_ranks, sorted_round_result
        )
        self.view.display_tournament_ranking(global_ranking)

        # TinyDB (save tournament data)
        serialize_tournament.update(
            {"rounds": rounds}, doc_ids=[len(serialize_tournament)]
        )

        self.view.ask_continue()
        self.run_tournament(tournament, players, rounds, global_ranking)

    def run_tournament(self, tournament, players, rounds, global_ranking):
        """
        Execute each rounds and pair players for the tournament previously initialized.

        Param:
            tournament (Tourney object) from the Tourney class.
            players (Player object): List of players objects from the Player class.
            rounds (list of dicts): Dictionaries of every rounds [{Match_x:{player_1: score_1, player_2: score_2}}]
            global_ranking (list of tuples): Players sorted by scores and ranks[("Player",(score, ranking))]

        When the tournament ends, runs the tournament function to update the player's ranks.
        """

        # Get matchs already played from each rounds:
        match_played = tournament.get_matchs_played(rounds)
        # Clean empty matchs.
        matchs_played = tournament.remove_empty(match_played)

        # Data from the current/previous tournament.
        rounds_left = tournament.number_of_rounds - tournament.current_round
        player_ranks = Player.get_player_name_ranking(players)
        serialize_tournament = tournament.get_tournament_table()

        # Run each matchs for every rounds.
        for matchs in range(rounds_left):
            get_round_result = tournament.add_scores(rounds)
            self.view.display_round_result(get_round_result)
            sorted_round_result = tournament.sort_scores(get_round_result)
            global_ranking = tournament.display_global_ranking(
                player_ranks, sorted_round_result
            )
            self.view.display_tournament_ranking(global_ranking)
            player_name = Player.get_players_from_ranking(global_ranking)
            # Swiss tournament pairing algorithm
            pair_players = tournament.pairs_swiss_system(player_name, matchs_played)
            split_players = Player.split_pairs_of_players(pair_players)
            # Build next round:
            try:
                rounds[tournament.current_round] = tournament.build_next_round(
                    split_players, self.view.next_pairs, self.view.next_round_result
                )
                serialize_tournament.update(
                    {"rounds": rounds}, doc_ids=[len(serialize_tournament)]
                )
                tournament.current_round += 1
                serialize_tournament.update(
                    {"current_round": tournament.current_round},
                    doc_ids=[len(serialize_tournament)],
                )
                if tournament.current_round != 4:
                    self.view.ask_continue()
            except IndexError:
                print("No more matchs to be found !")
                exit()
        if tournament.current_round == 4:
            tournament.change_player_ranking(
                players,
                rounds,
                self.view.display_tournament_ranking,
                self.view.update_ranks,
                self.view.confirm_update,
            )
