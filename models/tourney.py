"""Defines a tournament."""
import random


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
        round_1 = {"Match 1": {},
                "Match 2": {},
                "Match 3": {},
                "Match 4": {}}
                    
        for x in range(rounds):
            next_round = round_1.copy()
            round_history.append(next_round)

        return round_history

    def build_first_round(players_list, rounds_list):
        # Tourney
        players = sorted(players_list, key=lambda player: player.ranking, reverse=True)
        first_half = players[0:4]
        second_half = players[4:8]
        result = Tourney.round_result()
        for i in range(4):
            rounds_list[0][f"Match {i+1}"] = {first_half[i].first_name: result[0], 
                                            second_half[i].first_name: result[1]}

        return rounds_list

    def round_result():
        # Tourney
        """Returns a list containing the scores (integer) from the player's match.

        USING RANDOM BUT NEEDS TO BE AN INPUT FROM THE USER LATER
        """

        win_match_1 = [1, 0]
        win_match_2 = [0, 1]
        draw_match = [0.5, 0.5]
        match_variables = [win_match_1, win_match_2, draw_match]

        return random.sample(match_variables, 1)[0]

    def get_round_result(scores):
        # Tourney
        """ """

        ranking = {**scores["Match 1"],
                **scores["Match 2"],
                **scores["Match 3"],
                **scores["Match 4"]}
        sort_matchs = sorted(ranking.items(), key=lambda item: item[1], reverse=True)

        return sort_matchs

    def build_next_round(players, pair_players, split_players):
        # Tourney
        next_round = {"Match 1": {},
                    "Match 2": {},
                    "Match 3": {},
                    "Match 4": {}}

        for i in range(4):
            pairs = split_players[i]
            round_results = Tourney.round_result()
            next_round[f"Match {i+1}"] = {pairs[0]: round_results[0],
                                        pairs[1]: round_results[1]}

        return next_round