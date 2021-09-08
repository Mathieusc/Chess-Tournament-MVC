from tinydb import TinyDB

# Jason file used for TinyDB
db = TinyDB("db.json")


class Data:
    """"""

    def __init__(self):
        pass

    def get_all_players(self):
        # Returns the table with all participants
        player_table = db.table("all_players")

        return player_table.all()

    def get_tournament(self):
        tournaments = db.table("tournament")

        return tournaments.all()

    def get_tournaments_players(self):
        tournaments = db.table("tournament")
        tournament = tournaments.all()
        players = []
        for player in tournament:
            players.append(player.get("players"))

        return players
