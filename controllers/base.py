"""Gives methods for the display of the global ranking after each rounds."""
from models.player import Player
from models.tourney import Tourney
from views.base import View
from pprint import pprint

class Controller:

    def __init__(self, view):
        self.view = view
        
    def add_scores(scores):
        # Tourney
        """"""
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
        # Tourney
        """"""

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

    def run():
        #Generates a tournament instance.
        #tournament = View.prompt_tournament()

        tournament = Tourney("Grand Chess Tour", "London", "June 06, 2021", 4)
        print(f"{tournament.name} \nLocation: {tournament.location}\nDate: {tournament.date}\nNumber of rounds: {tournament.number_of_rounds}\n")

        # Generate players.
        list_of_players = Player.generates_player(Player)
        serialize_players = Player.serialize_player(list_of_players)
        print(serialize_players)
        #list_of_players = View.generate_player()

        # # Initialize the objects for every rounds.    
        # number_of_rounds = tournament.number_of_rounds
        ranks = Player.get_player_name_ranking(list_of_players)
        rounds = Tourney.generate_round(tournament.number_of_rounds)
        round_1 = Tourney.build_first_round(list_of_players, rounds)

        # Executes the matchs for each rounds.
        for matchs in range(tournament.number_of_rounds):
            print(f"\nRound {matchs+1}")
            pprint(rounds[matchs])
            round_result = Tourney.get_round_result(rounds[matchs])
            print("\nRound result:")
            pprint(round_result)
            sum_rounds = Controller.add_scores(rounds)
            sorted_sum_rounds = Controller.sort_scores(sum_rounds)
            global_rank = Controller.display_global_ranking(ranks, sorted_sum_rounds)
            players = Player.get_players_from_ranking(global_rank)
            pair_players = Player.create_pairs_of_players(players)
            split_players = Player.split_pairs_of_players(pair_players)
            print("\nGlobal ranking:")
            pprint(global_rank)
            print()
            try:
                rounds[matchs+1] = Tourney.build_next_round(players, pair_players, split_players)
            except IndexError:
                print("Tournament ended !")
                break