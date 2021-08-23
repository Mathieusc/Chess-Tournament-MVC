"""Gives methods for the display of the global ranking after each rounds."""
from models.datadb import Data
from models.player import Player
from models.tourney import Tourney
from views.base import View
from tinydb import TinyDB
from pprint import pprint

class Controller:

    def __init__(self, view):
        self.view = view
        
    def add_scores(scores):
        """param: list of dict (match results + empty matchs)
        return: only one dict with results-> player: score"""
        score_list = {}

        for rnd in scores:
            for matchs in rnd.values():
                for key in matchs.keys():
                    if key not in score_list:
                        score_list[key] = matchs.get(key)
                    else:
                        score_list[key] += matchs.get(key)

        return score_list

    def sort_scores(scores):
        """param: list of dict player: result
        return: list of tuples (player, result) sorted by scores"""

        global_ranking = sorted(scores.items(), key=lambda item: item[1], reverse=True)

        return global_ranking

    def display_global_ranking(rank_list, score_list):
        # Tourney
        rank_list = dict(rank_list)
        score_list = dict(score_list)
        for key, value in rank_list.items():
            if key in score_list:
                score_list[key] = [score_list[key], value]
        score_list = sorted(score_list.items(), key=lambda item: item[1], reverse=True)
        # Removes the ranking each time for better visibility when displaying the results
        # for player, score_rank in score_list:
        #     del score_rank[1]

        # Displays everything:
        # for player, score_rank in score_list:
        #     print(f"Player: {player}, score: {score_rank[0]}, ranking: {score_rank[1]}")

        return score_list

    def load_ranking_data():
        """"""

        load_tourney = Tourney.get_tournament_data()
        tournament = Tourney.deserialize_tournament(load_tourney[-1])
        ROUNDS = tournament.rounds
        serialize_tournament = Tourney.get_tournament_table()
        load_players = tournament.players
        players = Player.deserialize_players(load_players)

        Player.change_player_ranking(players, ROUNDS, serialize_tournament)

    def run():
        View.start_program()

    def load_tournament_data():
        # Tournament data
        load_tourney = Tourney.get_tournament_data()
        tournament = Tourney.deserialize_tournament(load_tourney[-1])
        if tournament.current_round == 4:
            print(f"{tournament.name}, rounds done: {tournament.current_round} / {tournament.number_of_rounds}\nThis tournament is over !")
            View.start_program()
        ROUNDS = tournament.rounds
        print(f"\nRounds from previous tournament:\n{ROUNDS}")
        # Players
        load_players = tournament.players
        players = Player.deserialize_players(load_players)
        # Global ranking data
        player_ranks = Player.get_player_name_ranking(players)
        get_round_result = Controller.add_scores(ROUNDS)
        sorted_round_result = Controller.sort_scores(get_round_result)
        global_ranking = Controller.display_global_ranking(player_ranks, sorted_round_result)

        Controller.run_tournament(tournament, players, ROUNDS, global_ranking)

    def setup_tournament():
        #tournament = View.prompt_tournament()
        tournament = Tourney("Grand Chess Tour", "London", "November 06, 2021", 4)
        tournament.current_round = 1
        print(f"\nTournament:\n{tournament}")

        #players = View.prompt_players()
        players = Player.generates_player(Player)
        print(f"\nPlayers:\n{players}")
        player_ranks = Player.get_player_name_ranking(players)
        print(f"\nRanks:\n{player_ranks}")
        
        # Rounds                
        setup_rounds = Tourney.generate_round(tournament.number_of_rounds)
        print(f"\nSetup_rounds:\n{setup_rounds}")
        ROUNDS = Tourney.build_first_round(setup_rounds, players)
        print(f"\nRounds:\n{ROUNDS}")
        
        get_round_result = Controller.add_scores(ROUNDS)
        print(f"\nRounds results:\n{get_round_result}")
        sorted_round_result = Controller.sort_scores(get_round_result)
        print(f"\nSorted rounds results:\n{sorted_round_result}")
        global_ranking = Controller.display_global_ranking(player_ranks, sorted_round_result)
        print("\nGlobal ranking:")
        for every_player in enumerate(global_ranking, 1):
            print(every_player)
        
        # TINYDB
        serialize_tournament = Tourney.serialize_tournament(tournament)
        serialize_tournament.update({'rounds': ROUNDS}, doc_ids=[len(serialize_tournament)])
        convert = Player.convert_to_dict(players)
        serialize_tournament.update({'players': convert}, doc_ids=[len(serialize_tournament)])

        View.ask_continue()
        Controller.run_tournament(tournament, players, ROUNDS, global_ranking)

    def run_tournament(tournament, players, ROUNDS, global_ranking):
        """"""

        rounds_left = tournament.number_of_rounds - tournament.current_round
        player_ranks = Player.get_player_name_ranking(players)
        serialize_tournament = Tourney.get_tournament_table()
        print("\nNEXT ROUND, serialize tournament:")
        print(serialize_tournament)
        for matchs in range(rounds_left):
            get_round_result = Controller.add_scores(ROUNDS)
            print(f"\nRounds results:\n{get_round_result}")
            sorted_round_result = Controller.sort_scores(get_round_result)
            print(f"\nSorted rounds results:\n{sorted_round_result}")
            global_ranking = Controller.display_global_ranking(player_ranks, sorted_round_result)
            print("\nGlobal ranking:")
            for every_player in enumerate(global_ranking, 1):
                print(every_player)
            player_name = Player.get_players_from_ranking(global_ranking)
            pair_players = Player.create_pairs_of_players(player_name)
            split_players = Player.split_pairs_of_players(pair_players)
            try:
                ROUNDS[tournament.current_round] = Tourney.build_next_round(player_name, split_players)
                serialize_tournament.update({'rounds': ROUNDS}, doc_ids=[len(serialize_tournament)])
                tournament.current_round += 1
                print(f"\nRounds: {tournament.current_round}\n:{ROUNDS}")
                serialize_tournament.update({'current_round': tournament.current_round}, doc_ids=[len(serialize_tournament)])
                if tournament.current_round != 4:
                    View.ask_continue()
            except IndexError:
                print("No more matchs to be found !")
                exit()
        if tournament.current_round == 4:
            View.ask_ranking_change(players, ROUNDS, serialize_tournament)
