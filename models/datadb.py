"""
Using TinyDB module as a document oriented database.
Every data from each tournament are stored into a 'db.json' file.

More info: https://tinydb.readthedocs.io/en/latest/
"""

from tinydb import TinyDB

# Jason file used for TinyDB
db = TinyDB("db.json")


class Data:
    """
    Send the document table from Tinydb requested from the controller.
    """

    def get_all_players(self):
        """
        Return the table of every player.
        """

        player_table = db.table("all_players")

        return player_table.all()

    def get_tournament(self):
        """
        Return the table of every tournament.
        """

        tournaments = db.table("tournament")

        return tournaments.all()

    def get_tournaments_players(self):
        """
        Return a list of every player from every tournament.
        """

        tournaments = db.table("tournament")
        tournament = tournaments.all()
        players = []

        for player in tournament:
            players.append(player.get("players"))

        return players
