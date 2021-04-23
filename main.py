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

# Création des instances de joueurs
player_1 = modules.Player("Magnus", "Carlsen", 1990, "male", 2847)
player_2 = modules.Player("Fabiano", "Caruana", 1992, "male", 2720)
player_3 = modules.Player("Ding ", "Liren", 1992, "male", 2691)
player_4 = modules.Player("Ian", "Nepomniachtchi", 1990, "male", 2589)

player_5 = modules.Player("Levron", "Aronian", 1982, "male", 2481)
player_6 = modules.Player("Aleksandr", "Grichtchouk", 1983, "male", 2377)
player_7 = modules.Player("Anish", "Giri", 1994, "male", 2276)
player_8 = modules.Player("Shakhriyar", "Mamedyarov", 1985, "male", 2170)


# Création d'une instance de tournois
tournament = modules.Tourney("Grand Chess Tour", "Londres", "June 06, 2021", 4)
print(tournament.location)

# Lister toutes les instances Player
list_of_players = modules.Player.LIST_OF_PLAYERS

# Trier les joueurs par ranking
sort_players_by_ranking = modules.sort_players_by_ranking(list_of_players)

# Séparer les joueurs en 2 et trier par classement, à mettre dans une classe.(?)
first_half_of_players = list_of_players[0:4]
sorted_first_half_of_players = modules.sort_players_by_ranking(first_half_of_players)

second_half_of_players = list_of_players[4:8]
sorted_second_half_of_players = modules.sort_players_by_ranking(second_half_of_players)

# Création du premier round, qui oppose le premier de chaque tableau, le deuxième etc..
# Algo des scores, Soit 1 gagnant et 1 perdant (1-0), soit égalité: 0.5 points
# Affichage des rounds du premier tour, boucle pour afficher tous les joueurs
rounds = []
for n in range(4):
	print("First round !")
	round_1 = {"Match 1": {},
			   "Match 2": {},
			   "Match 3": {},
			   "Match 4": {}}
	for i in range(4):
		# Génération des pairs de joueurs
		player_one = sorted_first_half_of_players[i]
		player_two = sorted_second_half_of_players[i]
		first_match = modules.show_opponents(player_one.first_name, 
											 player_two.first_name)
		first_round_result = modules.round_result()
		round_1[f"Match {i+1}"] = {player_one.first_name: first_round_result[0], 
								   player_two.first_name: first_round_result[1]}

	rounds.append(round_1)


print(rounds)
#----------------------------------------------------------------------------------------------------------------------------
# # Trier les joueurs par scores du premier round (tri par classement en 2eme prio déjà effectué)
# sorted_players_by_1st_round_scores = modules.sort_players_by_score(list_of_players)

# # Affichage test pour voir le classement des joueurs du premier round + leur classement initial
# print("Players ranking from the 1st round:")	

# for player in sorted_players_by_1st_round_scores:
# 	show_players_scores = modules.show_ranking_by_scores(player.first_name,
# 		player.score)

# # Condition test pour plus tard (3eme round et 4)
# # if not sorted_players_by_1st_round_scores[0].first_name and sorted_players_by_1st_round_scores[0].first_name in first_match:
# # 	print("Déjà joué")
# # else:
# # 	print("Pas joué")



# #----------------------------------------------------------------------------------------------------------------------------
# # 2eme round:
# print()
# print("Second Round !")
# x = 0; y = 1
# for pairs_of_players in range(4):

# 	# Génération des pairs de joueurs
# 	second_match = modules.show_opponents(sorted_players_by_1st_round_scores[x].first_name, 
# 										  sorted_players_by_1st_round_scores[y].first_name)

# 	second_round_result = modules.round_result()

# 	# Attribution des points pour chaque pairs de joueurs
# 	player_one_result = sorted_players_by_1st_round_scores[x].score + second_round_result[0][0]
# 	player_two_result = sorted_players_by_1st_round_scores[y].score + second_round_result[0][1]


# 	player_one = sorted_players_by_1st_round_scores[x]
# 	player_two = sorted_players_by_1st_round_scores[y]

# 	print(f"Results: \n\
# {player_one.first_name} - {player_one.score}\n\
# {player_two.first_name} - {player_two.score}")
# 	print()

# 	# Ajout des points du second round dans l'attribut score des joueurs
# 	setattr(player_one, 'score', player_one_result)
# 	setattr(player_two, 'score', player_two_result)

# 	x += 2; y += 2

# print()
# sorted_players_by_2nd_round_scores = modules.sort_players_by_score(list_of_players)
# print("Players ranking from the 2nd round:")	
# i = 0
# for number_of_players in range(8):
# 	show_players_scores = modules.show_ranking_by_scores(sorted_players_by_2nd_round_scores[i].first_name,
# 		sorted_players_by_2nd_round_scores[i].score)
# 	i += 1






