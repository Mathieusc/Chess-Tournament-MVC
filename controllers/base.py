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

    def run():
        View.start_program()

    def load_tournament_data():
        load_tourney = Tourney.get_tournament_data()
        print("\nLoad tourney data:")
        print(load_tourney)
        tournament = Tourney.deserialize_tournament(load_tourney[-1])
        print("\nCurrent tournament data: ")
        print(tournament)
        load_players = Player.get_player_data()
        print("\nLoaded players:")
        print(load_players)
        players = Player.deserialize_players(load_players)
        print("\nList of players:")
        print(players)
        ROUNDS = tournament.rounds 
        print(f"\nRounds:{ROUNDS}")

        Controller.run_tournament(tournament, players, ROUNDS)

    def start_tournament():
        #Generates a tournament instance.
        tournament = Tourney("Grand Chess Tour", "London", "November 06, 2021", 4)
        #tournament = View.generate_tournament()
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
        ROUNDS = Tourney.build_first_round(round_list, list_of_players)
        print("\nROUNDS")
        print(ROUNDS)
        Tourney.clear_round_table()
        Tourney.clear_current_round_table()
        number_of_rounds = tournament.number_of_rounds
        serialize_tournament = Tourney.serialize_tournament(tournament)
        print("\nSerialized tournament:\t", serialize_tournament)
        print(type(serialize_tournament))
        TOURNAMENT = Tourney.get_current_table(serialize_tournament)
        print("TOURNAMENT ITEM")
        print(TOURNAMENT)

        # Executes the matchs for each rounds.
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
            print("\nserialize rounds............")
            print(serialize_rounds)
            print(serialize_rounds.all())
            try:
                TOURNAMENT.update({'rounds': serialize_rounds.all()})
                serialize_tournament.update({'rounds': TOURNAMENT.get('rounds')}, doc_ids=[len(serialize_tournament)])
                print()
                print("serialize tournament updated")
                print(serialize_tournament)
                print("NEW TOURNAMENT ITEM")
                print(TOURNAMENT)
                print(type(TOURNAMENT))
                View.ask_continue()
                ROUNDS[matchs+1] = Tourney.build_next_round(players, split_players)
                tournament.current_round += 1
                TOURNAMENT.update({'current_round': tournament.current_round})
                serialize_tournament.update({'current_round': TOURNAMENT.get('current_round')}, doc_ids=[len(serialize_tournament)])
                TOURNAMENT.update({'number_of_round': tournament.current_round})
                print(f"Current round: {tournament.current_round}")
            except IndexError:
                print("Tournament ended !")
                exit()

    def load_tournament():
        # Generates a tournament instance.
        load_tourney = Tourney.get_tournament_data()
        print("SERIALIZE TOURNAMENT")
        print(type(load_tourney))

        tournament = Tourney.deserialize_dic_tournament(load_tourney[-1])
        print("\nTournament:")
        print(tournament)

        # round_number = Tourney.get_round_number()
        # print(round_number)
        # rnd = round_number[-1]['current_round']
        # print(rnd)
        # print(type(rnd))

        print(load_tourney[-1])
        tournament_table = load_tourney[-1]
        print(tournament_table)
        View.prompt_load_tourney(tournament_table)

        # for tourneys in tournament_table:
        #     if tourneys['current_round'] == tourneys['number_of_rounds']:
        #         print("\nThis tournament is done !\n")
        #         View.start_program()
        
        # if tournament_table.get('current_round') == tournament_table.get('number_of_rounds'):
        #     print("\nThis tournament is done !\n")
        #     View.start_program()

        # for tourney in tournament_table:
        #     print(tourney['rounds'])
        # save = tourney['rounds']
        Tourney.clear_new_rounds()

        save = tournament_table.get('rounds')
        print(save)

        serialize_tournament = Tourney.serialize_new_tournament()
        print("\nserialize_tournament:")
        print(serialize_tournament)
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


        TOURNAMENT = tournament_table.copy()
        print("TOURNAMENT ITEM")
        print(TOURNAMENT)
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
                print("ROUNDS AFTER CONTINUE")
                print(ROUNDS)
                serialize_rounds = Tourney.serialize_new_rounds(ROUNDS[matchs+1])
                test = []
                test.append(TOURNAMENT.get('rounds'))
                test.append(serialize_rounds.all())
                print("\ntest")
                print(test)
                print("\nserialize_rounds..............")
                print(serialize_rounds)
                print(serialize_rounds.all())

                tournament.current_round += 1
                print("\nTOURNAMENT BEFORE UPDATE")
                print(TOURNAMENT)
                TOURNAMENT.update({'current_round': tournament.current_round})
                TOURNAMENT.update({'rounds': serialize_rounds.all()})
                print("\nTOURNAMENT AFTER UPDATE")
                print(TOURNAMENT)
                serialize_tournament.update({'current_round': TOURNAMENT.get('current_round')}, doc_ids=[len(serialize_tournament)])
                serialize_tournament.update({'rounds': TOURNAMENT.get('rounds')}, doc_ids=[len(serialize_tournament)])
                print(f"Current round: {tournament.current_round}")
            except IndexError:
                print("Tournament ended !")
                exit()
        if tournament.current_round == tournament.number_of_rounds:
            print("Tournament ended !")
            exit()

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
        
        setup_rounds = Tourney.generate_round(tournament.number_of_rounds)
        print(f"\nSetup_rounds:\n{setup_rounds}")

        ROUNDS = Tourney.build_first_round(setup_rounds, players)
        print(f"\nRounds:\n{ROUNDS}")
        
        get_round_result = Controller.add_scores(ROUNDS)
        print(f"\Rounds results:\n{get_round_result}")
        sorted_round_result = Controller.sort_scores(get_round_result)
        print(f"\nSorted rounds results:\n{sorted_round_result}")
        global_ranking = Controller.display_global_ranking(player_ranks, sorted_round_result)
        print("\nGlobal ranking:")
        for every_player in enumerate(global_ranking, 1):
            print(every_player)
        
        # TINYDB
        serialize_tournament = Tourney.serialize_tournament(tournament)
        print("\nFirst round, serialize tournament:")
        print(serialize_tournament)
        serialize_players = Player.serialize_player(players)
        serialize_tournament.update({'rounds': ROUNDS}, doc_ids=[len(serialize_tournament)])
        
        # SPLIT RUN TOURNAMENT
        Controller.run_tournament(tournament, players, ROUNDS)

    def run_tournament(tournament, players, ROUNDS):
        """"""
        rounds_left = tournament.number_of_rounds - tournament.current_round
        player_ranks = Player.get_player_name_ranking(players)
        serialize_tournament = Tourney.get_tournament_table()
        print("\nNEXT ROUND, serialize tournament:")
        print(serialize_tournament)
        # print(rounds_left)
        # print(tournament)
        # print(players)
        # print(ROUNDS)
        for matchs in range(rounds_left):
            get_round_result = Controller.add_scores(ROUNDS)
            print(f"\Rounds results:\n{get_round_result}")
            sorted_round_result = Controller.sort_scores(get_round_result)
            print(f"\nSorted rounds results:\n{sorted_round_result}")
            global_ranking = Controller.display_global_ranking(player_ranks, sorted_round_result)
            print("\nGlobal ranking:")
            for every_player in enumerate(global_ranking, 1):
                print(every_player)
            player_name = Player.get_players_from_ranking(global_ranking)
            print(f"\nPlayer_name:\n{player_name}")
            pair_players = Player.create_pairs_of_players(player_name)
            print(f"\nPaired_players:\n{pair_players}")
            split_players = Player.split_pairs_of_players(pair_players)
            print(f"\nSplit_players:\n{split_players}")
            try:
                ROUNDS[matchs+1] = Tourney.build_next_round(player_name, split_players)
                print(f"\nRounds:\n:{ROUNDS}")
                serialize_tournament.update({'rounds': ROUNDS}, doc_ids=[len(serialize_tournament)])
                tournament.current_round += 1
                serialize_tournament.update({'current_round': tournament.current_round}, doc_ids=[len(serialize_tournament)])
                # Increment current_round, 
                # Save and update with TinyDB, 
                # ask for next round or stop and G fucking G maguy
            except IndexError:
                tournament.current_round += 1
                serialize_tournament.update({'current_round': tournament.current_round}, doc_ids=[len(serialize_tournament)])
                print("Tournament ended !")
                exit()
        print("Tournament ended !")