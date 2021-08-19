"""Defines the players."""
from tinydb import TinyDB, Query

class Player:

    LIST_OF_PLAYERS = []
    # ID = 0
    players_created = 0

    def __init__(self, first_name, last_name, year_of_birth, gender, ranking, ID):
        # first_name = Prénom, last_name = Nom
        self.first_name = first_name
        self.last_name = last_name
        self.year_of_birth = year_of_birth # YEAR format
        self.gender = gender
        self.ranking = ranking
        self.ID = ID
        # type(self).ID += 1
        # self.ID = self.ID
        # Accessing the class attributes (not instance attribute)
        self.LIST_OF_PLAYERS.append(self)
        Player.players_created += 1

    def get_players_from_ranking(ranking):
        # Player
        """"""

        return [players[0] for players in ranking]

    def sort_players_by_ranking(players):
        # Tourney
        """"""

        return sorted(players, key=lambda player: player.ranking, reverse=True)

    def create_pairs_of_players(players):
        # Tourney
    
        return [players[i]+"_"+ players[i+1] for i in range(0, len(players), 2)]

    def split_pairs_of_players(pairs_of_players):
        # Tourney
        return [elements.split("_") for elements in pairs_of_players]

    def get_player_name_ranking(player):
        # Player
        sorted_dict = {}
        for players in player:
            sorted_dict[players.first_name] = players.ranking

        return sorted(sorted_dict.items(), key=lambda item: item[1], reverse=True)

    def generates_player(Player):
        player_1 = Player("Magnus", "Carlsen", 1990, "Male", 2847, 1)
        player_2 = Player("Yifan", "Hou", 1994, "Female", 2720, 2)
        player_3 = Player("Ding ", "Liren", 1992, "Male", 2691, 3)
        player_4 = Player("Aleksandra", "Goryachkina", 1998, "Female", 2589, 4)
        player_5 = Player("Levron", "Aronian", 1982, "Male", 2481, 5)
        player_6 = Player("Koneru", "Humpy", 1987, "Female", 2377, 6)
        player_7 = Player("Anish", "Giri", 1994, "Male", 2276, 7)
        player_8 = Player("Wenjun", "Ju", 1991, "Female", 2170, 8)
        list_of_players = Player.LIST_OF_PLAYERS

        return list_of_players

    def serialize_player(player):
        players_list = []
        db = TinyDB('db.json')
        players_table = db.table('players')
        players_table.truncate() # clear the table first
        for players in player:
            serializerd_player = {
                'name': players.first_name,
                'last_name': players.last_name,
                'year_of_birth': players.year_of_birth,
                'gender': players.gender,
                'ranking': players.ranking,
                'player_id': players.ID,
            }
            players_list.append(serializerd_player)
            players_table.insert(serializerd_player)

        return players_table

    def deserialize_players(players_data):
        """"""
        player_list = []
        for players in players_data:
            name = players.get('name')
            print(name)
            last_name = players.get('last_name')
            print(last_name)
            year_of_birth = players.get('year_of_birth')
            print(year_of_birth)
            gender = players.get('gender')
            ranking = players.get('ranking')
            print(ranking)
            ID = players.get('player_id')
            print(ID)
            player_ = Player(name, last_name, year_of_birth, gender, ranking, ID)
            player_list.append(player_)
        print("Player 1 and 8 + ID + ranking:")
        print(player_list[0].first_name, player_list[0].ID, player_list[0].ranking, player_list[0].last_name)
        print(player_list[7].first_name, player_list[7].ID, player_list[7].ranking, player_list[7].last_name)
        return player_list

    def get_player_data():
        db = TinyDB('db.json')
        players = db.table('players')
        print("\nCHECKPOINT:")

        # return table


        return players.all()