import itertools

played = [("Magnus", "Alexandra"), ("Yifan", "Magnus"), ("Levron", "Anish"), ("Wenjun", "Koneru")]

joueurs = ["Magnus", "Alexandra", "Yifan", "Ding", "Levron", "Anish", "Wenjun", "Koneru"]


def test(joueurs, played):
    match = []
    print("Liste de joueurs avant début fonction: ")
    print(joueurs)
    for player1, player2 in zip(itertools.repeat(joueurs[0]), joueurs[1:]):
        print(player1, player2)
        if (player1, player2) not in played and (player2, player1) not in played:
            match = (player1, player2)
            print("NEXT MATCH")
            print(match)
            # Supprimer les joueurs de ma liste trié
            joueurs.remove(player1)
            joueurs.remove(player2)
            print("List de joueurs après remove: ")
            print(joueurs)
            # Ajouter le match dans la liste déjà joués
            played.append(match)
            print("Matchs déjà joués:")
            print(played)

            try:
                test(joueurs, played)
            except IndexError:
                print("Fin de liste")
            return played

w = test(joueurs, played)
print("Liste des matchs nouveaux matchs ajoutés:")
print(w)
