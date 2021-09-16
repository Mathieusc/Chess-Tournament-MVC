"""Defines and run a tournament."""

from models.player import Player
from models.datadb import db
import itertools

class Tourney:
    """
    Class used to represent a tournament.

    Param:
        name (str)
        location (str)
        date (str)
        number_of_rounds (int) - default value = 4
    """
    def __init__(self, name, location, date, number_of_rounds=4):
        self.name = name
        self.location = location
        self.date = date
        self.number_of_rounds = number_of_rounds

    def match_format(self):
        """
        Bullet = 1 to 2 minutes per player
        Blitz = 3, 5 or 10 minutes per player each turn
        Speed chess = 15 to 60 minutes per player
        """
        pass

    def director_description(self):
        # Director's feedback
        pass

    def generate_round(self, rounds):
        """
        Setup empty dicts for match 1 to 4.

        Return:
             List of dict.
        """
        round_history = []
        round_1 = {"match_1": {}, "match_2": {}, "match_3": {}, "match_4": {}}

        for i in range(rounds):
            next_round = round_1.copy()
            round_history.append(next_round)

        return round_history

    def add_scores(self, scores):
        """
        Add scores from a round to the previously generated dicts of matchs.

        Param: 
            List of dicts (match results + empty matchs)
        Return: 
            Dict with results -> player: score
        """
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
        """
        Sort player by scores from a round.

        Param: 
            List of dicts - player: result
        Return: 
            List of tuples (player, result) sorted by scores.
        """
        global_ranking = sorted(scores.items(), key=lambda item: item[1], reverse=True)

        return global_ranking

    def display_global_ranking(self, rank_list, score_list):
        """
        Add player's scores and ranking and sort them by each.

        Param:
            rank_list (List of tuples (player, rank))
            score_list (List of dicts (player, score))
        Return:
            List of tuples with (Players, (scores, ranks)) sorted by scores and ranks.
        """
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
        """
        Generate the first round, sort players, split them in half and pairs them.

        Param:
            rounds (List of dicts) Generated matchs
            players_list (List of players)
        Return:
            List of dicts [{"Match_x":{"player_1": score_1, "player_2": score_2}}...]
        """
        players = sorted(players_list, key=lambda player: player.ranking, reverse=True)
        first_half = players[0:4]
        second_half = players[4:8]
        for i in range(4):
            rounds[0][f"match_{i+1}"] = {
                first_half[i].first_name: self.first_round_result(first_half[i]),
                second_half[i].first_name: self.first_round_result(second_half[i]),
            }

        return rounds

    def first_round_result(self, player):
        """
        Ask the user to enter the player's score.
        View ?
        """
        player_result = input(
            (
                f"Enter the score from the following player:\n{player.ID}: {player.first_name}: "
            )
        )

        return float(player_result)

    def build_next_round(self, split_players):
        """
        Pair each players for the next rounds.

        Param:
            split_players (list of tuples) Pairs of players
        """
        next_round = {"match_1": {}, "match_2": {}, "match_3": {}, "match_4": {}}

        for i in range(4):
            pairs = split_players[i]
            print(f"{pairs[0]} VS {pairs[1]}")
            next_round[f"match_{i+1}"] = {
                pairs[0]: self.next_round_result(pairs[0]),
                pairs[1]: self.next_round_result(pairs[1]),
            }

        return next_round

    def next_round_result(self, player):
        """
        Ask the user to enter the player's score.

        Param:
            player (Player object)
        """
        player_result = input(
            (f"Enter the score from the following player:\n{player}: ")
        )

        return float(player_result)

    def get_round_result(self, scores):
        # Tourney
        """Sort each matchs from player's scores.

        Param:
            scores (dict)
        Return:
            List of dicts of each matchs sorted by scores.
        """
        ranking = {
            **scores["match_1"],
            **scores["match_2"],
            **scores["match_3"],
            **scores["match_4"],
        }
        sort_matchs = sorted(ranking.items(), key=lambda item: item[1], reverse=True)

        return sort_matchs

    def change_player_ranking(self, players, rounds, serialize_tournament):
        """
        Update the ranking from every player of a tournament.

        Param:
            players (Player objects) List of every players
            rounds (dict) List of every matchs from every rounds
            serialize_tournament (Tinydb doc) Saved data from the tournament.
        """

        player_ranks = Player.get_player_name_ranking(players)
        get_round_result = self.add_scores(rounds)
        sorted_round_result = self.sort_scores(get_round_result)
        global_ranking = self.display_global_ranking(player_ranks, sorted_round_result)
        print("Global ranking from the last tournament:")
        for scores in enumerate(global_ranking, 1):
            print(scores)
        for i in range(len(players)):
            update_rank = float(
                input(
                    f"Update rank for: {players[i].first_name}, rank: {players[i].ranking}\t+ "
                )
            )
            players[i].ranking += update_rank
            print(f"New player's rank -> {players[i].ranking}")
        convert = Player.convert_to_dict(players)
        serialize_tournament.update({"all_players": convert})

        exit()

    def serialize_tournament(self, tournament):
        """
        Serialize a tournament object into a json file.

        Param:
            tournament (Tourney object)
        Return:
            TinyDB document table.
        """
        tournament_table = db.table("tournament")
        serialize_tournament = {
            "name": tournament.name,
            "location": tournament.location,
            "date": tournament.date,
            "number_of_rounds": tournament.number_of_rounds,
            "current_round": tournament.current_round,
        }
        tournament_table.insert(serialize_tournament)

        return tournament_table

    def get_tournament_table(self):
        """
        Return:
            Table document used to serialize the data from the tournament.
        """
        tournament_table = db.table("tournament")

        return tournament_table

    def deserialize_tournament(tournament_data):
        """
        Deserialize tournament's data into a Tourney object.

        Param:
            tournament_data (json dict)
        """

        name = tournament_data.get("name")
        location = tournament_data.get("location")
        date = tournament_data.get("date")
        number_of_rounds = tournament_data.get("number_of_rounds")
        rounds = tournament_data.get("rounds")
        tournament = Tourney(name, location, date, number_of_rounds)
        tournament.current_round = tournament_data.get("current_round")
        tournament.rounds = rounds

        return tournament

    def get_previous_rounds_data(round_list, table, current_round, total_round):

        round_left = total_round - current_round
        for i in range(round_left):
            table.append(round_list[0])

        return table

    def clear_player_table():
        players = db.table("players")
        players.truncate()

    def get_current_table(tournament_table):
        current_table = tournament_table.get(doc_id=len(tournament_table))

        return current_table

    def get_matchs_played(self, rounds):
        """
        Get the pairs of players that already played versus each other.
        Param:
            rounds (list of dicts) every matchs from the current tournament
        Return:
            List of tuples ('Player_1', 'Player_2')
        """
        match_played = []
        for dicts in rounds:
            for matchs in dicts.items():
                match_played.append(tuple(matchs[1].keys()))

        return match_played

    def remove_empty(self, tuples):
        """
        Remove empty tuples from the list of matchs already played
        Return:
            List of tuples
        """
        remove_blanks = [matchs for matchs in tuples if matchs]

        return remove_blanks

    def pairs_swiss_system(self, players, matchs_played):
        """
        Create pairs of players that did not played against each other in the tournament (if possible).
        Using itertools module with the zip and reapeat methods.
        Param:
            player_name (list) - Every players
            matchs_played (list of tuples) Matchs already played
        Return:
            List of pairs of players.
        """
        for player_1, player_2 in zip(itertools.repeat(players[0]), players[1:]):
            # Compare if each players already played against each other
            if (player_1, player_2) not in matchs_played and (player_2, player_1) not in matchs_played:
                matchs = (player_1, player_2)
                # Remove players from the initial list
                players.remove(player_1)
                players.remove(player_2)
                # Add the new matchs to the 'already played' list
                matchs_played.append(matchs)
                # Recursive call until the list of players is empty
                try:
                    self.pairs_swiss_system(players, matchs_played)
                except IndexError as msg:
                    msg = "List of players empty"
                return ["_".join(player) for player in matchs_played[-4:]]
                    