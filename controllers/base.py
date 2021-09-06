""""""

from models.datadb import Data
from models.player import Player
from models.tourney import Tourney
from tinydb import TinyDB


class Controller:
    
    def __init__(self, view):
        self.view = view

    def run(self):

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
                report = self.run_report()
            elif main_menu == "0":
                exit()
            else:
                print("Invalid input, please try again.")

    def run_report(self):
        # Doit avoir une variable à chaque request de Data et l'envoyer à la vue pour afficher le report, Data ne doit rien print !!
        data = Data()
        while True:
            main_menu = self.view.prompt_data()
            if main_menu == "1":
                all_players = data.get_all_players()
                list_players = sorted(all_players, key=lambda player: player.get('ranking'), reverse=True)
                self.view.display_all_players(list_players)
                continue
            if main_menu == "2":
                all_players = data.get_all_players()
                list_players = sorted(all_players, key=lambda player: player.get('last_name'))
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
        """"""

        load_tourney = Tourney.get_tournament_data()
        tournament = Tourney.deserialize_tournament(load_tourney[-1])
        rounds = tournament.rounds
        serialize_tournament = Tourney.get_tournament_table()
        load_players = tournament.players
        players = Player.deserialize_players(load_players)

        tournament.change_player_ranking(players, rounds, serialize_tournament)

    def load_tournament_data(self):
        # Tournament data
        load_tourney = Tourney.get_tournament_data()
        tournament = Tourney.deserialize_tournament(load_tourney[-1])
        if tournament.current_round == 4:
            print(f"{tournament.name}, rounds done: {tournament.current_round} / {tournament.number_of_rounds}\nThis tournament is over !")
            self.run()
        rounds = tournament.rounds
        print(f"\nRounds from previous tournament:\n{rounds}")
        # Players
        load_players = tournament.players
        players = Player.deserialize_players(load_players)
        # Global ranking data
        player_ranks = Player.get_player_name_ranking(players)
        get_round_result = tournament.add_scores(rounds)
        sorted_round_result = tournament.sort_scores(get_round_result)
        global_ranking = tournament.display_global_ranking(player_ranks, sorted_round_result)

        self.run_tournament(tournament, players, rounds, global_ranking)

    def setup_tournament(self):
        #tournament = View.prompt_tournament()
        tournament = Tourney("Grand Chess Tour", "London", "November 06, 2021", 4)
        tournament.current_round = 1

        #players = View.prompt_players()
        players = Player.generates_player(Player)
        player_ranks = Player.get_player_name_ranking(players)
        print(f"\nPlayer ranks:\n{player_ranks}")
        
        # Rounds                
        setup_rounds = tournament.generate_round(tournament.number_of_rounds)
        rounds = tournament.build_first_round(setup_rounds, players)
        get_round_result = tournament.add_scores(rounds)
        # Appeler la vue pour afficher les matchs, pas de prints dans tourney
        print(f"\nRounds results:\n{get_round_result}")
        sorted_round_result = tournament.sort_scores(get_round_result)
        global_ranking = tournament.display_global_ranking(player_ranks, sorted_round_result)
        print("\nGlobal ranking:")
        for every_player in enumerate(global_ranking, 1):
            print(every_player)
        
        # TINYDB
        serialize_tournament = tournament.serialize_tournament(tournament)
        Player.serialize_players(players)
        serialize_tournament.update({'rounds': rounds}, doc_ids=[len(serialize_tournament)])
        convert = Player.convert_to_dict(players)
        serialize_tournament.update({'players': convert}, doc_ids=[len(serialize_tournament)])

        self.view.ask_continue()
        self.run_tournament(tournament, players, rounds, global_ranking)

    def run_tournament(self, tournament, players, rounds, global_ranking):
        """"""

        # Data from the current/previous tournament
        rounds_left = tournament.number_of_rounds - tournament.current_round
        player_ranks = Player.get_player_name_ranking(players)
        serialize_tournament = tournament.get_tournament_table()

        # run each matchs for every rounds
        for matchs in range(rounds_left):
            get_round_result = tournament.add_scores(rounds)
            print(f"\nRounds results:\n{get_round_result}")
            sorted_round_result = tournament.sort_scores(get_round_result)
            global_ranking = tournament.display_global_ranking(player_ranks, sorted_round_result)
            print("\nGlobal ranking:")
            for every_player in enumerate(global_ranking, 1):
                print(every_player)
            player_name = Player.get_players_from_ranking(global_ranking)
            print("Get players from ranking:")
            print(player_name)
            # Aglo suisse ici avant ou après player_name

            pair_players = Player.create_pairs_of_players(player_name)
            split_players = Player.split_pairs_of_players(pair_players)

            try:
                rounds[tournament.current_round] = tournament.build_next_round(split_players)
                serialize_tournament.update({'rounds': rounds}, doc_ids=[len(serialize_tournament)])
                tournament.current_round += 1
                serialize_tournament.update({'current_round': tournament.current_round}, doc_ids=[len(serialize_tournament)])
                if tournament.current_round != 4:
                    self.view.ask_continue()
            except IndexError:
                print("No more matchs to be found !")
                exit()
        if tournament.current_round == 4:
            tournament.change_player_ranking(players, rounds, serialize_tournament)