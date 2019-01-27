import game
import naive_ai as n

ai_list = [n.NaiveAI("Adam"), n.NaiveAI("Bethea"), n.NaiveAI("Catherine"), n.NaiveAI("David")]
sevens = game.Game(ai_list)
wins = {}
for i in range(0,10000):
    sevens.reset()
    winner = sevens.play_game()
    if winner in wins:
        wins[winner] += 1
    else:
        wins[winner] = 1

print(wins)