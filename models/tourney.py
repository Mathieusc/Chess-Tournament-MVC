"""Defines a tournament."""

from models.player import Player
from models.datadb import db


class Tourney:
    def __init__(self, name, location, date, number_of_rounds):
        self.name = name
        self.location = location
        self.date = date
        self.number_of_rounds = number_of_rounds

    def match_format(self):
        """
        Bullet = 1 à 2 minutes par joueurs
        Blitz = 3, 5 ou 10 minutes par joueurs (pour tous les tours)
        Speed chess = 15 à 60 minutes par joueurs
        """
        pass

    def director_description(self):
        # Remarques du directeur
        pass

    def generate_round(self, rounds):
        # Tourney
        round_history = []
        round_1 = {"match_1": {},
                   "match_2": {},
                   "match_3": {},
                   "match_4": {}}
                    
        for i in range(rounds):
            next_round = round_1.copy()
            round_history.append(next_round)

        return round_history

    def add_scores(self, scores):
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

    def sort_scores(self, scores):
        """param: list of dict player: result
        return: list of tuples (player, result) sorted by scores"""

        global_ranking = sorted(scores.items(), key=lambda item: item[1], reverse=True)

        return global_ranking

    def display_global_ranking(self, rank_list, score_list):
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

    def build_first_round(self, rounds, players_list):

        players = sorted(players_list, key=lambda player: player.ranking, reverse=True)
        first_half = players[0:4]
        second_half = players[4:8]
        for i in range(4):
            rounds[0][f"match_{i+1}"] = {first_half[i].first_name: self.first_round_result(first_half[i]),
                                        second_half[i].first_name: self.first_round_result(second_half[i])}

        return rounds

    def first_round_result(self, player):
        """"""
        player_result = input((f"Enter the score from the following player:\n{player.ID}: {player.first_name}: "))
        
        return float(player_result)

    def build_next_round(self, split_players):

        next_round = {"match_1": {},
                      "match_2": {},
                      "match_3": {},
                      "match_4": {}}

        for i in range(4):
            pairs = split_players[i]
            print(f"{pairs[0]} VS {pairs[1]}")
            next_round[f"match_{i+1}"] = {pairs[0]: self.next_round_result(pairs[0]),
                                         pairs[1]: self.next_round_result(pairs[1])}

        return next_round

    def next_round_result(self, player):
        """Compared to first_round_result(), param= str('player_name'), not player object"""
        player_result = input((f"Enter the score from the following player:\n{player}: "))
            
        return float(player_result)
#-------------------------------------MANUAL SCORE INPUT-----------------------------------------------------------------------
    def get_round_result(self, scores):
        # Tourney
        """ """

        ranking = {**scores["match_1"],
                   **scores["match_2"],
                   **scores["match_3"],
                   **scores["match_4"]}
        sort_matchs = sorted(ranking.items(), key=lambda item: item[1], reverse=True)

        return sort_matchs

    def change_player_ranking(self, players, ROUNDS, serialize_tournament):
        """"""

        player_ranks = Player.get_player_name_ranking(players)
        get_round_result = self.add_scores(ROUNDS)
        sorted_round_result = self.sort_scores(get_round_result)
        global_ranking = self.display_global_ranking(player_ranks, sorted_round_result)
        print("Global ranking from the last tournament:")
        for scores in enumerate(global_ranking, 1):
            print(scores)
        for i in range(len(players)):
            update_rank = float(input(f"Update rank for: {players[i].first_name}, rank: {players[i].ranking}\t+ "))
            players[i].ranking += update_rank
            print(f"New player's rank -> {players[i].ranking}")
        convert = Player.convert_to_dict(players)
        serialize_tournament.update({'players': convert}, doc_ids=[len(serialize_tournament)])
        
        exit()

    def serialize_tournament(self, tournament):
        """"""
        tournament_table = db.table('tournament')
        serialize_tournament = {
            'name': tournament.name,
            'location': tournament.location,
            'date': tournament.date,
            'number_of_rounds': tournament.number_of_rounds,
            'current_round': tournament.current_round
            }
        tournament_table.insert(serialize_tournament)

        return tournament_table

    def get_tournament_table(self):
        tournament_table = db.table('tournament')

        return tournament_table

    def update_tournament(tournament):
        """"""
        tournament_table = db.table('tournament')
        serialize_tournament = {
            'name': tournament.name,
            'location': tournament.location,
            'date': tournament.date,
            'number_of_rounds': tournament.number_of_rounds,
            'current_round': tournament.current_round,
            'rounds': tournament.rounds
            }

        tournament_table.update(serialize_tournament)
        return tournament_table

    def update_rounds_table():

        tournament_table = db.table('tournament')
        rounds_table = db.table('rounds')
        tournament_table.insert({'rounds': rounds_table})

        return tournament_table

    def deserialize_tournament(tournament_data):
        """"""

        name = tournament_data.get('name')
        location = tournament_data.get('location')
        date = tournament_data.get('date')
        number_of_rounds = tournament_data.get('number_of_rounds')
        rounds = tournament_data.get('rounds')
        tournament = Tourney(name, location, date, number_of_rounds)
        tournament.current_round = tournament_data.get('current_round')
        tournament.rounds = rounds
        players = tournament_data.get('players')
        tournament.players = players

        return tournament

    def check_previous_rounds():
        Round = db.table('Rounds')
        print("TinyDB:")
        print(Round.all())

        return Round.all()

    def get_previous_rounds():
        table = db.table('tournament')
        rounds = table['Rounds']
        print(rounds)

    def get_tournament_data():
        tournament = db.table('tournament')

        return tournament.all()

    def get_round_number():
        round_number = db.table('round_number')

        return round_number.all()

    def deserialize_round_number(round_table):
        """"""

        rnd = round_table.get('rnd_number')

        return rnd

    def get_previous_rounds_data(round_list, table, current_round, total_round):

        round_left = total_round - current_round
        for i in range(round_left):
            table.append(round_list[0])

        return table

    def clear_round_table():
        rounds_table = db.table('Rounds')
        rounds_table.truncate()

    def clear_current_round_table():
        current_round_table = db.table('round_number')
        current_round_table.truncate()

    def clear_new_rounds():
        new_rounds = db.table('new_rounds')
        new_rounds.truncate()

    def clear_player_table():
        players = db.table('players')
        players.truncate()

    def update_rounds_from_tournament(tournament_table, roundz):
        current_table = tournament_table.doc_id=len(tournament_table)
        update_dict = {
            'current_round': roundz.get('current_round'),
            'rounds': roundz.get('rounds')
        }
        tournament_table.update({'current_round': roundz.get('current_round')})

        return current_table

    def get_current_table(tournament_table):
        current_table = tournament_table.get(doc_id=len(tournament_table))

        return current_table

    def serialize_new_rounds(ronde):
        rounds_table = db.table('new_rounds')
        for key, value in ronde.items():
            serializerd_round = {key: value}
            rounds_table.insert(serializerd_round)

        return rounds_table
