"""Defines a tournament."""
import random

from tinydb.table import Document
from models.player import Player
from tinydb import TinyDB
from tinydb.operations import delete

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

    def generate_round(rounds):
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

    # def build_first_round(players_list, rounds_list):
    #     # Tourney
    #     players = sorted(players_list, key=lambda player: player.ranking, reverse=True)
    #     first_half = players[0:4]
    #     second_half = players[4:8]
    #     result = Tourney.round_result()
    #     for i in range(4):
    #         rounds_list[0][f"match_{i+1}"] = {first_half[i].first_name: result[0], 
    #                                          second_half[i].first_name: result[1]}

    #     return rounds_list
#-----------------------------------------------------------------------
    # def build_next_round(players, split_players):
    #     # Tourney
    #     next_round = {"match_1": {},
    #                   "match_2": {},
    #                   "match_3": {},
    #                   "match_4": {}}

    #     for i in range(4):
    #         pairs = split_players[i]
    #         round_results = Tourney.round_result()
    #         next_round[f"match_{i+1}"] = {pairs[0]: round_results[0],
    #                                      pairs[1]: round_results[1]}

    #     return next_round
#-----------------------------------------------------------------------
    # def round_result():
    #     # Tourney
    #     """Returns a list containing the scores (integer) from the player's match.

    #     USING RANDOM BUT NEEDS TO BE AN INPUT FROM THE USER LATER
    #     """

    #     win_match_1 = [1, 0]
    #     win_match_2 = [0, 1]
    #     draw_match = [0.5, 0.5]
    #     match_variables = [win_match_1, win_match_2, draw_match]

    #     return random.sample(match_variables, 1)[0]
#--------------I AM HERE MANUAL SCORE INPUT-----------------------------------------------------------------
    def build_first_round(rounds, players_list):
        players = sorted(players_list, key=lambda player: player.ranking, reverse=True)
        first_half = players[0:4]
        second_half = players[4:8]
        for i in range(4):
            rounds[0][f"match_{i+1}"] = {first_half[i].first_name: Tourney.first_round_result(first_half[i]),
                                        second_half[i].first_name: Tourney.first_round_result(second_half[i])}

        return rounds

    def first_round_result(player):
        """"""
        #for players in player:
        player_result = input((f"Enter the score from the following player:\n{player.ID}: {player.first_name}: "))
        
        return float(player_result)

    def build_next_round(players, split_players):
        # Tourney
        next_round = {"match_1": {},
                      "match_2": {},
                      "match_3": {},
                      "match_4": {}}

        for i in range(4):
            pairs = split_players[i]
            #print(f"Build next round function\nPairs:{pairs}")
            next_round[f"match_{i+1}"] = {pairs[0]: Tourney.next_round_result(pairs[0]),
                                         pairs[1]: Tourney.next_round_result(pairs[1])}

        return next_round

    def next_round_result(player):
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
        #for key, value in scores.items():
            
        sort_matchs = sorted(ranking.items(), key=lambda item: item[1], reverse=True)

        return sort_matchs

    def serialize_round(ronde):
        db = TinyDB('db.json')
        rounds_table = db.table('Rounds')
        for key, value in ronde.items():
            serializerd_round = {key: value}
            rounds_table.insert(serializerd_round)
        return rounds_table

    def update_round(round):
        db = TinyDB('db.json')
        rounds_table = db.table('Rounds')
        for key, value in round.items():
            updated_round = {'match_':{key: value}}
            rounds_table.update(updated_round)

        return rounds_table

    def serialize_tournament(tournament):
        """"""
        db = TinyDB('db.json')
        tournament_table = db.table('tournament')
        print("TOURNAMENT TABLE:")
        print(tournament_table)
        tables = tournament_table.get(doc_id=len(tournament_table))
        print("CURRENT TABLE")
        print(tables)
        #tournament_table.truncate()
        #tourney_list = []
        serialize_tournament = {
            'name': tournament.name,
            'location': tournament.location,
            'date': tournament.date,
            'number_of_rounds': tournament.number_of_rounds,
            'current_round': tournament.current_round
            }
        #tourney_list.append(serialize_tournament)
        #tournament_table.insert({'tournament_data': tourney_list})
        tournament_table.insert(serialize_tournament)
        return tournament_table

    def get_tournament_table():
        db = TinyDB('db.json')
        tournament_table = db.table('tournament')

        return tournament_table

    def serialize_current_round(current_round):
        db = TinyDB('db.json')
        round_number_table = db.table('round_number')
        serialize_round_number = {
            'rnd_number': current_round
        }
        round_number_table.insert(serialize_round_number)
        return round_number_table

    def update_tournament(tournament):
        """"""
        db = TinyDB('db.json')
        tournament_table = db.table('tournament')
        #tournament_table.truncate()
        #tourney_list = []
        serialize_tournament = {
            'name': tournament.name,
            'location': tournament.location,
            'date': tournament.date,
            'number_of_rounds': tournament.number_of_rounds,
            'current_round': tournament.current_round,
            'rounds': tournament.rounds
            }
        #tourney_list.append(serialize_tournament)
        #tournament_table.insert({'tournament_data': tourney_list})

        tournament_table.update(serialize_tournament)
        return tournament_table

    def update_rounds_table():

        db = TinyDB('db.json')
        tournament_table = db.table('tournament')
        rounds_table = db.table('rounds')
        tournament_table.insert({'rounds': rounds_table})

        return tournament_table

    # def deserialize_tournament(tournament_table):
    #     """"""
    #     for tournament_infos in tournament_table:
    #         name = tournament_infos['name']
    #         location = tournament_infos['location']
    #         date = tournament_infos['date']
    #         number_of_rounds = tournament_infos['number_of_rounds']
    #         rounds = tournament_infos['rounds']
    #         tournament = Tourney(name, location, date, number_of_rounds)
    #         tournament.current_round = tournament_infos['current_round']
    #         tournament.rounds = rounds

    #     return tournament

    # def deserialize_tournament(tournament_table):
    #     """"""

    #     name = tournament_table.get('name')
    #     location = tournament_table.get('location')
    #     date = tournament_table.get('date')
    #     number_of_rounds = tournament_table.get('number_of_rounds')
    #     rounds = tournament_table.get('rounds')
    #     tournament = Tourney(name, location, date, number_of_rounds)
    #     tournament.current_round = tournament_table.get('current_round')
    #     tournament.rounds = rounds

    #     return tournament

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
        db = TinyDB('db.json')
        Round = db.table('Rounds')
        print("TinyDB:")
        print(Round.all())

        return Round.all()

    def get_previous_rounds():
        db = TinyDB('db.json')
        table = db.table('tournament')
        rounds = table['Rounds']
        print(rounds)

    def get_tournament_data():
        db = TinyDB('db.json')
        tournament = db.table('tournament')

        return tournament.all()

    def get_round_number():
        db = TinyDB('db.json')
        round_number = db.table('round_number')
        return round_number.all()

    def deserialize_round_number(round_table):
        """"""

        rnd = round_table.get('rnd_number')
        return rnd

    def get_previous_rounds_data(round_list, table, current_round, total_round):
        # print("TABLE")
        # print(table)
        # print(type(table))
        # print(len(table))
        round_left = total_round - current_round
        for i in range(round_left):
            table.append(round_list[0])
            # print(round_list[0])

        return table

    def clear_round_table():
        db = TinyDB('db.json')
        rounds_table = db.table('Rounds')
        rounds_table.truncate()

    def clear_current_round_table():
        db = TinyDB('db.json')
        current_round_table = db.table('round_number')
        current_round_table.truncate()

    def clear_new_rounds():
        db = TinyDB('db.json')
        new_rounds = db.table('new_rounds')
        new_rounds.truncate()

    def clear_player_table():
        db = TinyDB('db.json')
        players = db.table('players')
        players.truncate()

    def update_rounds_from_tournament(tournament_table, roundz):
        db = TinyDB('db.json')
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
        db = TinyDB('db.json')
        rounds_table = db.table('new_rounds')
        for key, value in ronde.items():
            serializerd_round = {key: value}
            rounds_table.insert(serializerd_round)
        return rounds_table
