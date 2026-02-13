name = input("Enter player's name: ")
games_played = int(input("Number of games played: "))
total_score = int(input("Total score achieved: "))
average_score = total_score/games_played
print(f"{name}\n {games_played}\n {total_score}\n {average_score:.2f}")