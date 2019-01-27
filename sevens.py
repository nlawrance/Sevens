import game

sevens = game.Game()
wins = {}
for i in range(0,10000):
    sevens.reset()
    winner = sevens.play_game()
    if winner in wins:
        wins[winner] += 1
    else:
        wins[winner] = 1

print(wins)