#Defining Scrabble board
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
#Creating a dict for the board
letters_to_points = {x:y for x,y in zip(letters, points)}

letters_to_points[" "] = 0
#Defining a function to calculate the score
def score_word(word):
  point_total = 0
  for i in word:
    point_total += letters_to_points.get(i)
  return (point_total)
#Creating a mock scenario
player_to_words = {"player1" : ["BLUE", "TENNIS", "EXIT"], "wordNerd" : ["EARTH", "EYES", "MACHINE"], "Lexi Con" : ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]} 

player_to_points = {}

for player,words in player_to_words.items():
  player_points = 0
  for word in words:
    player_points += score_word(word)
  player_to_points[player] = [player_points]

print(player_to_points)