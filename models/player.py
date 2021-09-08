"""Defines the players."""
from models.datadb import db


class Player:
    """"""

    LIST_OF_PLAYERS = []

    def __init__(self, first_name, last_name, year_of_birth, gender, ranking, ID):
        # First_name = Prénom(fr), last_name = Nom(fr)
        self.first_name = first_name
        self.last_name = last_name
        # YEAR format
        self.year_of_birth = year_of_birth
        self.gender = gender
        self.ranking = ranking
        self.ID = ID
        self.LIST_OF_PLAYERS.append(self)

    def generates_player(self):
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

    def add_players_to_data(player):
        players_list = []
        players_table = db.table("all_players")
        # players_table.truncate()  # Clear the table first
        for players in player:
            serializerd_player = {
                "name": players.first_name,
                "last_name": players.last_name,
                "year_of_birth": players.year_of_birth,
                "gender": players.gender,
                "ranking": players.ranking,
                "player_id": players.ID,
            }
            players_list.append(serializerd_player)
            players_table.insert(serializerd_player)

    def sort_players_by_ranking(players):
        # Tourney
        """"""

        return sorted(players, key=lambda player: player.ranking, reverse=True)

    def get_players_from_ranking(ranking):
        # Player
        """"""

        return [players[0] for players in ranking]

    def create_pairs_of_players(players):
        # Tourney

        return [players[i] + "_" + players[i + 1] for i in range(0, len(players), 2)]

    def split_pairs_of_players(pairs_of_players):
        # Tourney
        return [elements.split("_") for elements in pairs_of_players]

    def get_player_name_ranking(player):
        # Player
        sorted_dict = {}
        for players in player:
            sorted_dict[players.first_name] = players.ranking

        return sorted(sorted_dict.items(), key=lambda item: item[1], reverse=True)

    def serialize_players(player):
        players_list = []
        players_table = db.table("all_players")
        players_table.truncate()  # clear the table first
        for players in player:
            serializerd_player = {
                "name": players.first_name,
                "last_name": players.last_name,
                "year_of_birth": players.year_of_birth,
                "gender": players.gender,
                "ranking": players.ranking,
                "player_id": players.ID,
            }
            players_list.append(serializerd_player)
            players_table.insert(serializerd_player)

    def deserialize_players(players_data):
        """"""
        player_list = []
        for players in players_data:
            name = players.get("name")
            last_name = players.get("last_name")
            year_of_birth = players.get("year_of_birth")
            gender = players.get("gender")
            ranking = players.get("ranking")
            ID = players.get("player_id")
            player_ = Player(name, last_name, year_of_birth, gender, ranking, ID)
            player_list.append(player_)

        return player_list

    def get_player_data():
        players = db.table("players")

        return players.all()

    def convert_to_dict(players):
        player_list = []
        playerz = {}
        for player in players:
            playerz = {
                "name": player.first_name,
                "last_name": player.last_name,
                "year_of_birth": player.year_of_birth,
                "gender": player.gender,
                "ranking": player.ranking,
                "player_id": player.ID,
            }
            player_list.append(playerz)

        return player_list

    def get_all_players():
        all_players = db.table("all_players")

        return all_players.all()
