from tinydb import TinyDB, Query
from tinydb.table import Document


class Data:
    """"""

    def __init__(self):
        pass

    def main_table(self):
        pass

    def display_tables(self):
        print(self.tables())

    def display_all(self):
        tables = self.table()
        print(tables.all())

    def display_tournament(self):
        tournament = self.table('tournament')
        print(tournament.all())

    def display_players(self):
        players = self.table('players')
        print(players.all())

    def display_rounds(self):
        rounds = self.table('rounds')
        print(rounds.all())

    def display_matchs_1(self):
        rounds_table = self.table('rounds')
        print('Round 1:')
        print(rounds_table.get(doc_id=1))
        print(rounds_table.get(doc_id=2))
        print(rounds_table.get(doc_id=3))
        print(rounds_table.get(doc_id=4))

    def display_matchs_2(self):
        rounds_table = self.table('rounds')
        print('Round 2:')
        print(rounds_table.get(doc_id=5))
        print(rounds_table.get(doc_id=6))
        print(rounds_table.get(doc_id=7))
        print(rounds_table.get(doc_id=8))

    def display_matchs_3(self):
        rounds_table = self.table('rounds')
        print('Round 3:')
        print(rounds_table.get(doc_id=9))
        print(rounds_table.get(doc_id=10))
        print(rounds_table.get(doc_id=11))
        print(rounds_table.get(doc_id=12))

    def display_matchs_4(self):
        rounds_table = self.table('rounds')
        print('Round 4:')
        print(rounds_table.get(doc_id=13))
        print(rounds_table.get(doc_id=14))
        print(rounds_table.get(doc_id=15))
        print(rounds_table.get(doc_id=16))