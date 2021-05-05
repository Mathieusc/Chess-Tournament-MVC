import modules
import random

def sort_players_by_ranking(players):
	"""This function will return the sorted method for the list of players in the function's parameter (players)
		using the reverse=True option to apply a descending sort (we are sorting players by their ranking)."""

	return sorted(players, key=lambda player: player.ranking, reverse=True)

def sort_players_by_score(players):
	"""doc"""

	return sorted(players, key=lambda player: player.score, reverse=True)

def show_ranking_by_scores(players, scores):
	"""doc"""

	print(players, scores)

def round_result():
	"""This function will return a list containing the scores (integer) from the player's round.

	USING RANDOM BUT NEEDS TO BE AN INPUT FROM THE USER LATER
	"""

	win_match_1 = [1, 0]
	win_match_2 = [0, 1]
	draw_match = [0.5, 0.5]
	match_variables = [win_match_1, win_match_2, draw_match]

	return random.sample(match_variables, 1)[0]

def show_opponents(player_one, player_two):
	"""doc"""

	# player_one = str(player_one)
	# player_two = str(player_two)
	print(player_one, "VS", player_two)

def set_player_score(player, score):
	"""doc"""

	setattr(player, 'score', score)

def get_ranking(scores):
	""" """

	ranking = {**scores["Match 1"],
			   **scores["Match 2"],
			   **scores["Match 3"],
			   **scores["Match 4"]}
	sort_matchs = sorted(ranking.items(), key=lambda item: item[1], reverse=True)

	return sort_matchs

def get_players_from_ranking(ranking):
	""""""

	return [players[0] for players in ranking]

def create_pairs_of_players(players):

	return [players[i]+"_"+ players[i+1] for i in range(0, len(players), 2)]

def split_pairs_of_players(pairs_of_players):

	return [elements.split("_") for elements in pairs_of_players]

def build_next_round(ranking, players, pair_players, split_players):
	""""""
	next_round = {"Match 1": {},
	              "Match 2": {},
	              "Match 3": {},
	              "Match 4": {}}

	for i in range(4):
	    pairs = split_players[i]
	    round_result = modules.round_result()
	    next_round[f"Match {i+1}"] = {pairs[0]: round_result[0],
	     	                                pairs[1]: round_result[1]}

	return next_round