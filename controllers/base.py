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
        View.start_program()

    def start_tournament():
        #Generates a tournament instance.
        tournament = tournament = Tourney("Grand Chess Tour", "London", "November 06, 2021", 4)
        tournament.current_round = 1
        print("Tournament: \n")
        print(tournament)

        # Generate players.
        list_of_players = Player.generates_player(Player)
        serialize_players = Player.serialize_player(list_of_players)
        print(serialize_players)  
        ranks = Player.get_player_name_ranking(list_of_players)
        
        # Generate the objects for each rounds.
        round_list = Tourney.generate_round(tournament.number_of_rounds)
        ROUNDS = Tourney.build_round(round_list, list_of_players)
        Tourney.clear_round_table()
        number_of_rounds = tournament.number_of_rounds
        serialize_tournament = Tourney.serialize_tournament(tournament)
        print("Tournament: \n")
        print(serialize_tournament)

        # Executes the matchs for each rounds, using either new data or data from the last tournament.
        for matchs in range(number_of_rounds):
            print()
            print(f"ROUNDS: \n{ROUNDS}")
            print(f"\nRound {tournament.current_round}")
            print(ROUNDS[matchs]) 
            # round_result = Tourney.get_round_result(ROUNDS[matchs])
            # print("\nRound result:")
            # pprint(round_result)
            sum_rounds = Controller.add_scores(ROUNDS)
            sorted_sum_rounds = Controller.sort_scores(sum_rounds)
            global_rank = Controller.display_global_ranking(ranks, sorted_sum_rounds)
            players = Player.get_players_from_ranking(global_rank)
            pair_players = Player.create_pairs_of_players(players)
            split_players = Player.split_pairs_of_players(pair_players)
            print("\nGlobal ranking:")
            pprint(global_rank)
            print()
            serialize_rounds = Tourney.serialize_round(ROUNDS[matchs])
            print(serialize_rounds)
            print(serialize_rounds.all())
            try:
                tournament.current_round += 1
                serialize_tournament.update({'rounds': serialize_rounds.all()})
                View.ask_continue()
                serialize_tournament.update({'current_round': tournament.current_round})
                ROUNDS[matchs+1] = Tourney.build_next_round(players, split_players)
                #serialize_tournament = Tourney.update_rounds_table()
                print(f"Current round: {tournament.current_round}")
            except IndexError:
                print("Tournament ended !")
                exit()

    def load_tournament():
        # Generates a tournament instance.
        tournament_table = Tourney.get_tournament_data()
        print(tournament_table)
        for tourneys in tournament_table:
            if tourneys['current_round'] == tourneys['number_of_rounds']:
                print("\nThis tournament is done !\n")
                View.start_program()

        print("HELP ME")
        for tourney in tournament_table:
            print(tourney['rounds'])
        save = tourney['rounds']

        View.prompt_load_tourney(tournament_table)
        tournament = Tourney.deserialize_tournament(tournament_table)
        serialize_tournament = Tourney.update_tournament(tournament)
        print("Tournament: \n")
        print(tournament)
        current_round = tournament.current_round
        number_of_rounds = tournament.number_of_rounds
        rounds_left = number_of_rounds - current_round
        # Players, NEEDS TO BE DONE WITH DB.JSON
        list_of_players = Player.generates_player(Player)
        serialize_players = Player.serialize_player(list_of_players)
        print(serialize_players)

        # Initialize the objects for every rounds.    
        ranks = Player.get_player_name_ranking(list_of_players)


        # save = Tourney.check_previous_rounds()
        # print("Previous rounds:\n")
        # pprint(save)

        round_list = Tourney.generate_round(number_of_rounds)
        print()
        print(f"Round_list: {round_list}")
        ROUNDS = Tourney.get_previous_rounds_data(round_list, save, current_round, number_of_rounds)
        print()
        print("ROUNDS ITEM:")
        print(ROUNDS)
        for matchs in range(rounds_left):
            sum_rounds = Controller.add_scores(ROUNDS)
            sorted_sum_rounds = Controller.sort_scores(sum_rounds)
            global_rank = Controller.display_global_ranking(ranks, sorted_sum_rounds)
            players = Player.get_players_from_ranking(global_rank)
            pair_players = Player.create_pairs_of_players(players)
            split_players = Player.split_pairs_of_players(pair_players)
            print("\nGlobal ranking:")
            pprint(global_rank)
            print()
            try:
                View.ask_continue()
                ROUNDS[matchs+1] = Tourney.build_next_round(players, split_players)
                serialize_rounds = Tourney.serialize_round(ROUNDS[matchs+1])
                print(serialize_rounds)
                print(serialize_rounds.all())
                tournament.current_round += 1
                # update_tourney = Tourney.update_tournament(tournament_table)
                # update_tourney.update({'current_round': tournament.current_round})
                # update_tourney.update({'rounds': serialize_rounds.all()})
                serialize_tournament.update({'current_round': tournament.current_round})
                print(f"Current round: {tournament.current_round}")
            except IndexError:
                print("Tournament ended !")
                exit()
        if tournament.current_round == tournament.number_of_rounds:
            print("Tournament ended !")
            exit()

    def run_tournament():
        tournament = View.prompt_tournament()
        players = View.prompt_players()
        # list_of_players =
        # ranks =
        # ROUNDS = 
        pass