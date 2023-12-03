total_games = []
extracted_games = []

# Read in lines to list
infile = open("02_cube_conundrum/input.txt", "r")
for game in infile:
  total_games.append(game.strip()) # Ensures no newline characters
infile.close()

# Look at every set of each game and extract the rgb values
for game in total_games:
  current_game = []
  current_set = [0, 0, 0]
  if (game[7] != ":") and (game[7] != " "):
    string = game[10:]
  elif game[6] != ":":
    string = game[9:]
  else:
    string = game[8:]
  temp_num = ""
  for char in string:
    if char == ";":
      current_game.append(current_set)
      current_set = [0, 0, 0]
    elif char.isdigit():
      temp_num += char
    elif char != " ":
      if char == "r" and temp_num != "":
        current_set[0] = int(temp_num)
        temp_num = ""
      elif char == "g":
        current_set[1] = int(temp_num)
        temp_num = ""
      elif char == "b":
        current_set[2] = int(temp_num)
        temp_num = ""
  current_game.append(current_set)
  extracted_games.append(current_game)


# Print to ensure correct extractions
# Show powers of each game to check for correct behavior
power_sum = 0
for game in extracted_games:
  max_vals = [0, 0, 0]
  power = 0
  for game_set in game:
    if game_set[0] > max_vals[0]:
      max_vals[0] = game_set[0]
    if game_set[1] > max_vals[1]:
      max_vals[1] = game_set[1]
    if game_set[2] > max_vals[2]:
      max_vals[2] = game_set[2]
  power = max_vals[0] * max_vals[1] * max_vals[2]
  print("Game", extracted_games.index(game) + 1, "Power: ", power)
  power_sum += power


print()
print("Power Sum: ", power_sum)
