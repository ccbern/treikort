import time
import copy

players = []
available_calls = ['Grand', 'No Low', 'Color', 'Spades']
suits = ['Spades', 'Hearts', 'Clubs', 'Diamonds']

dict_available_calls = {}
player_call = None
round_num = 0
hand_num = 0

player_1_running_score = 0
player_2_running_score = 0
player_3_running_score = 0

final_scores = []

print('\n')
print('Let\'s play Treikort!')
print('\n')

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

# OR

# {
# 	Calls: 'Grand','No Low', 'Color', 'Spades']
# 	player_1: [][x][][x]
# 	player_2: [x][][][]
# 	player_3: [][][x][]
# }

print('\n')
print('OK!  The players are %s, %s, and %s...  Let\'s begin!' % (player_1, player_2, player_3))
print('\n')

# Game is over after 4 rounds
while round_num < 4:
	
	round_num += 1
	print('- - - - - Round %s - - - - -' % round_num)

###### CALLS #####
	for player in players:
		print('\n')
		print("It's %s's turn." % player)
		print('\n')

		if round_num == 4:
			print('%s must play %s!' % (player,dict_available_calls[player][0]))

			player_call = dict_available_calls[player][0]

		else:
			print("%s's available calls are: " % player)

			for call in dict_available_calls[player]:
				print(call)

			print('\n')

			player_call = input('Make a call: ') 

			while player_call not in dict_available_calls[player]:
				print('Please make an available call: ')
				print("Available calls are: ")
				
				for call in dict_available_calls[player]:
					print(call)

				print('\n')

				player_call = input('Make a call: ') 

		if player_call == 'Color':
			print('\n')
			suit_pick = input('Pick a suit: ')

			while suit_pick not in suits:
				print('\n')
				print('Invalid entry.  Please pick a suit.')
				print('\n')

				suit_pick = input('Pick a suit: ')

			if player == player_1:
				player_1_suit_pick = suit_pick

			elif player == player_2:
				player_2_suit_pick = suit_pick

			else:
				player_3_suit_pick = suit_pick

		dict_available_calls[player].remove(player_call)

##### DECLARING THRESHOLDS #####
		
		print('\n')

		if player_call == 'No Low':
			print('%s can only take 4 tricks; the others can take 6.' % player)

		else:
			print('%s needs to take at least 8 tricks; the others need to take 4.' % player)

###### SCORING ######
		
		player_1_round_score = 1
		player_2_round_score = 1
		player_3_round_score = 1

		round_score_sum = player_1_round_score + player_2_round_score + player_3_round_score

		print('\n')

		while round_score_sum != 0:
			player_1_round_tricks = int(input('How many tricks did %s take?: ' % player_1))

### Potential validation code ###
		# try:
		# 	val = int(player_1_round_score)
		# except:
		# 	print('Please enter an integer.')

			player_2_round_tricks = int(input('How many tricks did %s take?: ' % player_2))
		
			player_3_round_tricks = int(input('How many tricks did %s take?: ' % player_3))

			if player_call == 'No Low':
				caller_score_for_zero = 4
				non_caller_score_for_zero = 6

				if player == player_1:
					player_1_round_score = caller_score_for_zero - player_1_round_tricks
					player_2_round_score = non_caller_score_for_zero - player_2_round_tricks
					player_3_round_score = non_caller_score_for_zero - player_3_round_tricks

				elif player == player_2:
					player_1_round_score = non_caller_score_for_zero - player_1_round_tricks
					player_2_round_score = caller_score_for_zero - player_2_round_tricks
					player_3_round_score = non_caller_score_for_zero - player_3_round_tricks

				else:
					player_1_round_score = non_caller_score_for_zero - player_1_round_tricks
					player_2_round_score = non_caller_score_for_zero - player_2_round_tricks
					player_3_round_score = caller_score_for_zero - player_3_round_tricks

			else:
				caller_score_for_zero = 8
				non_caller_score_for_zero = 4

			
				if player == player_1:
					player_1_round_score = player_1_round_tricks - caller_score_for_zero
					player_2_round_score = player_2_round_tricks - non_caller_score_for_zero
					player_3_round_score = player_3_round_tricks - non_caller_score_for_zero

				elif player == player_2:
					player_1_round_score = player_1_round_tricks - non_caller_score_for_zero
					player_2_round_score = player_2_round_tricks - caller_score_for_zero
					player_3_round_score = player_3_round_tricks - non_caller_score_for_zero

				else:
					player_1_round_score = player_1_round_tricks - non_caller_score_for_zero
					player_2_round_score = player_2_round_tricks - non_caller_score_for_zero
					player_3_round_score = player_3_round_tricks - caller_score_for_zero

			round_score_sum = player_1_round_score + player_2_round_score + player_3_round_score

			if round_score_sum != 0:
				print('\n')
				print('Invalid sum.  Please recount.')
				print('\n')

		player_1_running_score = player_1_running_score + player_1_round_score
		player_2_running_score = player_2_running_score + player_2_round_score
		player_3_running_score = player_3_running_score + player_3_round_score 

	if round_num < 4:
		print('\n')
		print('Current scores after Round %s: ' % round_num)
		print('%s: %s' % (player_1, player_1_running_score))
		print('%s: %s' % (player_2, player_2_running_score))
		print('%s: %s' % (player_3, player_3_running_score))
		print('\n')

print('\n')
print('- - - - - GAME OVER - - - - -')
print('\n')
print('Final scores: ')
print('%s: %s' % (player_1, player_1_running_score))
print('%s: %s' % (player_2, player_2_running_score))
print('%s: %s' % (player_3, player_3_running_score))
print('\n')

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
	print ('%s and %s tie for the win!' % (player_1, player_2))

elif player_1_running_score == player_3_running_score:
	print ('%s and %s tie for the win!' % (player_1, player_3))

elif player_2_running_score == player_3_running_score:
	print ('%s and %s tie for the win!' % (player_2, player_3))

print('\n')
print('\n')

##### Suit Check #####
# print('%s played %s' % (player_1,player_1_suit_pick))
# print('%s played %s' % (player_2,player_2_suit_pick))
# print('%s played %s' % (player_3,player_3_suit_pick))

#### Dict for scores and find max? ####
# else:
# 	winning_score = max(final_scores)

# 	for score in final_scores:
# 		if score == winning_score



# Play again?
