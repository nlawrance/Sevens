import game
import naive_ai as n

wins = {}
ai_list = [n.NaiveAI("Adam"), n.NaiveAI("Bethea"), n.NaiveAI("Catherine"), n.NaiveAI("David")]
for ai in ai_list:
    wins[ai.get_name()] = 0
sevens = game.Game(ai_list)

for i in range(0,10000):
    sevens.rotate_ai()
    sevens.reset()
    winner = sevens.play_game()
    wins[winner] += 1

print(wins)