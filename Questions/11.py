# Q11. Ask number of games played in a tournament. 
# Ask the user number of games won and number of games loss. 
# Calculate number of tie and total Points. ( 1win = 4 points, 1 tie =2 points)

games_played = int(input(("Enter the number of games played in the tournament: ")))
games_won = int(input(("Enter the number of games won in the tournament: ")))
games_loss = int(input(("Enter the number of games loss in the tournament: ")))

games_tie = games_played - games_won - games_loss
print (f"Games tied = {games_tie}")

total_points=(games_won*4)+(games_tie*2)
print(f"Total points : {total_points}")


