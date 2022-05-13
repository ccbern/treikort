import time
import copy

players = []
available_calls = ['Grand', 'No Low', 'Color', 'Spades']
suits = ['Spades', 'Hearts', 'Clubs', 'Diamonds']

dict_available_calls = {}
player_call = None
round_num = 0

player_1_running_score = 0
player_2_running_score = 0
player_3_running_score = 0

final_scores = []


print('Let\'s play Treikort!')

# time.sleep(1)

player_1 = input('Player 1: ')
players.append(player_1)

player_2 = input('Player 2: ')
players.append(player_2)

player_3 = input('Player 3: ')
players.append(player_3)

# OBJECT TO BUILD: dict_available_calls ?
# {
# 	player_1: ['Grand','No Low','Color','Spades'],
# 	player_2: ['Grand','No Low','Color','Spades'],
# 	player_3: ['Grand','No Low','Color','Spades']
# }

for player in players:
	dict_available_calls[player] = copy.deepcopy(available_calls)

print(dict_available_calls)


# OR

# {
# 	Calls: 'Grand','No Low', 'Color', 'Spades']
# 	player_1: [][x][][x]
# 	player_2: [x][][][]
# 	player_3: [][][x][]
# }

print('OK!  The players are %s, %s, and %s...' % (player_1, player_2, player_3))
print('Let\'s play!')

# Game is over after 12 rounds
while round_num < 3:
	player_1_round_score = 1
	player_2_round_score = 1
	player_3_round_score = 1

	round_score_sum = player_1_round_score + player_2_round_score + player_3_round_score


	round_num += 1
	print('- - - - - Round %s - - - - -' % round_num)

# ###### FIRST ATTEMPT OF CALLS #####
# 	for player in players:
# 		print("It's %s's turn." % player)
# 		print("%s's options are: " % player)

# 		for call in dict_available_calls[player]:
# 			print(call)

# 		player_call = input('Make a call: ') 

# 		while player_call not in dict_available_calls[player]:
# 			print('Please make an available call: ')
# 			print("Available options are: ")
# 			print(dict_available_calls[player])

# 			player_call = input('Make a call: ') 

# 		print(type(dict_available_calls[player]))

# 		dict_available_calls[player].remove(player_call)
# 		print(player_call)
# 		print(dict_available_calls)
# 		print(dict_available_calls[player])

####### SECOND ATTEMPT ######
	# for k in dict_available_calls.keys():
	# 	print("It's %s's turn." % k)
	# 	print("%s's options are: " % k)

	# 	for call in dict_available_calls[k]:
	# 		print(call)

	# 	player_call = input('Make a call: ') 

	# 	# while player_call not in dict_available_calls[player]:
	# 	# 	print('Please make an available call: ')
	# 	# 	print("Available options are: ")
	# 	# 	print(dict_available_calls[player])

	# 	# 	player_call = input('Make a call: ') 

	# 	dict_available_calls[player].remove(player_call)
	# 	print(player_call)
	# 	print(dict_available_calls)
	# 	print(dict_available_calls[k])

#### SCORING ####
#### NEED TO COME BACK AND VALIDATE FOR INTEGER ######
	while round_score_sum != 0:
		player_1_round_score = int(input("Please enter %s\'s score: " % player_1))

### Potential validation code ###
		# try:
		# 	val = int(player_1_round_score)
		# except:
		# 	print('Please enter an integer.')

		player_2_round_score = int(input("Please enter %s\'s score: " % player_2))
		
		player_3_round_score = int(input("Please enter %s\'s score: " % player_3))

		round_score_sum = player_1_round_score + player_2_round_score + player_3_round_score

		if round_score_sum != 0:
			print('Invalid sum.  Please recount.')

	player_1_running_score = player_1_running_score + player_1_round_score
	player_2_running_score = player_2_running_score + player_2_round_score
	player_3_running_score = player_3_running_score + player_3_round_score 

	if round_num < 3:
		print('Current scores after Round %s: ' % round_num)
		print('%s: %s' % (player_1, player_1_running_score))
		print('%s: %s' % (player_2, player_2_running_score))
		print('%s: %s' % (player_3, player_3_running_score))

print('- - - - - GAME OVER - - - - -')
print('Final scores: ')
print('%s: %s' % (player_1, player_1_running_score))
print('%s: %s' % (player_2, player_2_running_score))
print('%s: %s' % (player_3, player_3_running_score))

final_scores.extend((player_1_running_score, player_2_running_score, player_3_running_score))

#### Determine Winner ####
if player_1_running_score == player_2_running_score == player_3_running_score:
	print("0's all around... Everyone wins!  Or loses?")

elif player_3_running_score < player_1_running_score > player_2_running_score:
	print ('%s wins!' % player_1)

elif player_3_running_score < player_2_running_score > player_1_running_score:
	print ('%s wins!' % player_2)

elif player_1_running_score < player_3_running_score > player_2_running_score:
	print ('%s wins!' % player_3)

elif player_1_running_score == player_2_running_score:
	print ('%s and %s win!' % (player_1, player_2))

elif player_1_running_score == player_3_running_score:
	print ('%s and %s win!' % (player_1, player_3))

elif player_2_running_score == player_3_running_score:
	print ('%s and %s win!' % (player_2, player_3))


#### Dict for scores and find max? ####
# else:
# 	winning_score = max(final_scores)

# 	for score in final_scores:
# 		if score == winning_score



# Play again?
