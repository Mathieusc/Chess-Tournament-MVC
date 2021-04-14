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

	return random.sample(match_variables, 1)

def show_opponents(player_one, player_two):
	"""doc"""

	# player_one = str(player_one)
	# player_two = str(player_two)
	print(player_one.capitalize(), "VS", str(player_two))

def set_player_score(player, score):
	"""doc"""

	setattr(player, 'score', score)
