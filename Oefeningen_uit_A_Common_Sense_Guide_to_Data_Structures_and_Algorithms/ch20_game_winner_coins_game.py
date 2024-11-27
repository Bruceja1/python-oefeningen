def game_winner(number_of_coins, current_player="you"):
    if number_of_coins <= 0:
        return current_player
    
    if current_player == "you":
        next_player = "them"
    elif current_player == "them":
        next_player = "you"

    if game_winner(number_of_coins - 1, next_player) == current_player or game_winner(number_of_coins - 2, next_player) == current_player:
        return current_player
    
    else:
        return next_player
    
print(game_winner(2))