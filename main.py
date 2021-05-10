"""Déroulement du tournoi:
1. Créer un nouveau tournoi
2. Ajouter 8 joueurs
3. L'ordinateur génère des paires de joueurs pour le premier tour.
4. Lorsque le tour est terminé, entrez les résultats.
5. Répétez les étapes 3 et 4 pour les tours suivants jusqu'à ce que tous les tours soient joués,
 et que le tournoi soit terminé.

 Pour les joueurs, utiliser TinyDB, cf doc.
 Flake8: longueur ligne maximal = 119
 """
import modules
from pprint import pprint
# Création des instances de joueurs
player_1 = modules.Player("Magnus", "Carlsen", 1990, "male", 2847)
player_2 = modules.Player("Yifan", "Hou", 1994, "female", 2720)
player_3 = modules.Player("Ding ", "Liren", 1992, "male", 2691)
player_4 = modules.Player("Aleksandra", "Goryachkina", 1998, "female", 2589)

player_5 = modules.Player("Levron", "Aronian", 1982, "male", 2481)
player_6 = modules.Player("Koneru", "Humpy", 1987, "female", 2377)
player_7 = modules.Player("Anish", "Giri", 1994, "male", 2276)
player_8 = modules.Player("Wenjun", "Ju", 1991, "female", 2170)


# Création d'une instance de tournois
tournament = modules.Tourney("Grand Chess Tour", "Londres", "June 06, 2021", 4)
print(tournament.name)

# Lister toutes les instances Player
list_of_players = modules.Player.LIST_OF_PLAYERS

sort_players_by_ranking = modules.sort_players_by_ranking(list_of_players)

# Séparer les joueurs en 2 et trier par classement, à mettre dans une classe.(?)
first_half_of_players = list_of_players[0:4]
sorted_first_half_of_players = modules.sort_players_by_ranking(first_half_of_players)
second_half_of_players = list_of_players[4:8]
sorted_second_half_of_players = modules.sort_players_by_ranking(second_half_of_players)

# Création du premier round, qui oppose le premier de chaque tableau, le deuxième etc..
# Algo des scores, Soit 1 gagnant et 1 perdant (1-0), soit égalité: 0.5 points
# Affichage des rounds du premier tour, boucle pour afficher tous les joueurs
round_history = []
round_1 = {"Match 1": {},
		   "Match 2": {},
		   "Match 3": {},
		   "Match 4": {}}
round_2 = round_1.copy()

for i in range(4):
	# Generates the pairs of players
	player_one = sorted_first_half_of_players[i]
	player_two = sorted_second_half_of_players[i]
	# first_match = modules.show_opponents(player_one.first_name, 
	# 									 player_two.first_name)
	first_round_result = modules.round_result()
	round_1[f"Match {i+1}"] = {player_one.first_name: first_round_result[0], 
							   player_two.first_name: first_round_result[1]}
	if i == 3:
		ranking = modules.get_ranking(round_1)
		print("Ranking")
		pprint(ranking)
		players = modules.get_players_from_ranking(ranking)
		print("\nPlayers:")
		print(players)
		pair_players = modules.create_pairs_of_players(players)
		print("\nPairs: ")
		print(pair_players)
		split_players = modules.split_pairs_of_players(pair_players)
		print("\nSplit:")
		print(split_players)
		round_2 = modules.build_next_round(ranking, players, pair_players, split_players)


round_history.append(round_1)
round_history.append(round_2)
#print(round_history)
print("\nRound 1:")
pprint(round_1)
print("\nRound 2:")
pprint(round_2)
print("\nRanking:")
pprint(ranking)
print()

print(round_history)
for matchs in round_history:
	print(matchs.items())
