import time
import copy
import csv
import os.path
from datetime import datetime

replay = ''
final_scores = []
winner_list = []

while replay != 'N':
	full_board = {}
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

### GAME BOARD SETUP ###
	def game_builder(players):
	
		for player in players:
			full_board[player] = {'score':0,'available_calls':[],'used_calls':[], 'rivalry_score':0}
			full_board[player]['available_calls'] = copy.deepcopy(available_calls)
	
		return full_board
	
	### INITIAL INPUTS ###
	print('\n')
	print('~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~')
	print('Let\'s play Treikort!')
	print('~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~')
	print('\n')
	
	player_1 = input('Player 1: ')
	players.append(player_1)
	
	player_2 = input('Player 2: ')
	players.append(player_2)
	
	player_3 = input('Player 3: ')
	players.append(player_3)

##################################
	# global game_number
##################################

	### CHECK IF REMATCH ###
	def check_rematch(player_1, player_2, player_3):
		past_games_file_exists = os.path.exists('./past_treikort_games.csv')

		if not past_games_file_exists:
			new_file = open('past_treikort_games.csv', 'w', encoding='utf-8-sig')
			writer = csv.writer(new_file)
			writer.writerow(['game_number','date','player_1','player_1_score','player_2','player_2_score','player_3','player_3_score','winner'])
			new_file.close()
			print('\n')
			print('Created file: "past_treikort_games"')
		
		past_games_file = open('past_treikort_games.csv', "r+", encoding='utf-8-sig')
		reader = csv.DictReader(past_games_file)

		rematch = False
		rematch_count = 0
		rematch_games = []
		rematch_winners = []
	
		for row in reader:
			player_count = 0
			for player in (player_1, player_2, player_3):
				if player in (row['player_1'], row['player_2'],row['player_3']):
					player_count += 1
	
			if player_count == 3:
				rematch = True
				rematch_count += 1
				rematch_games.append(row['game_number'])
##################################
		# 	max_game_number = int(row['game_number'])
		# 	print('MGN Set!')

		# try:
		# 	game_number = max_game_number + 1
		# 	print(max_game_number)
		# 	print('Added!')

		# except:
		# 	game_number = 1
		# 	print('defaulting to 1')

		# print('Game number: %s' % game_number)
##################################

		print('\n')
		if rematch:
			print('Rematch! Games played: %s' % rematch_count)
			print('\n')
			print('<><><> Rematch Scoreboard <><><>')
			past_games_file.seek(0)
			for row in reader:
				if row['game_number'] in rematch_games:
					rematch_winners.append(row['winner'].split(','))
	
			for player in (player_1, player_2, player_3):
				player_winner_count = 0
				for winner in rematch_winners:
					if player in winner:
						player_winner_count += 1
				print('%s: %s' % (player, player_winner_count))
	
		else:
			print('New match up!')
	
	check_rematch(player_1, player_2, player_3)

	### BUILD ###
	game_builder(players)
	
	### BEGIN GAME ###
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
				print('%s must play %s!' % (player,full_board[player]['available_calls'][0]))
	
				player_call = full_board[player]['available_calls'][0]
	
			else:
				print("%s's available calls are: " % player)
	
				for call in full_board[player]['available_calls']:
					print(call)
	
				print('\n')
	
				player_call = input('Make a call: ') 
	
				while player_call not in full_board[player]['available_calls']:
					print('\n')
					print('Please make an available call.')
					print('\n')
					print("Available calls are: ")
					
					for call in full_board[player]['available_calls']:
						print(call)
	
					print('\n')
	
					player_call = input('Make a call: ') 
	
			if player_call == 'Color':
				print('\n')
				suit_pick = input('Pick a suit: ')
	
				while suit_pick not in suits:
					print('\n')
					# print(suits)
					suit_pick = input('Invalid entry.  Please pick a suit: ')
					# print(suit_pick)

				full_board[player]['used_calls'].append({player_call:suit_pick})
	
					# suit_pick = input('Pick a suit: ').upper()
	
				# if player == player_1:
				# 	player_1_suit_pick = suit_pick
	
				# elif player == player_2:
				# 	player_2_suit_pick = suit_pick
	
				# else:
				# 	player_3_suit_pick = suit_pick

			else:
				full_board[player]['used_calls'].append(player_call)

	
			full_board[player]['available_calls'].remove(player_call)
				
	
	##### DECLARING THRESHOLDS #####
	
			print('\n')
	
			if player_call == 'No Low':
				print('%s can only take 4 tricks; the others can take 6.' % player)
	
			else:
				print('%s needs to take at least 8 tricks; the others need to take 4.' % player)
	
			print('\n')
			print('You say, you play!  %s starts.' % player)
	
	###### SCORING ######
			
			# player_1_round_score = 1
			# player_2_round_score = 1
			# player_3_round_score = 1
	
			# round_score_sum = player_1_round_score + player_2_round_score + player_3_round_score

			round_score_sum = None
	
			print('\n')
	
			while round_score_sum != 0:
				### Integer Validation ###
				score_int = None
				try:
					player_1_round_tricks = int(input('How many tricks did %s take?: ' % player_1))

					score_int = True
					
				except:
					while not score_int:
						print('\n')
						try:
							print('Please enter a valid number.')
							print('\n')
							player_1_round_tricks = int(input('How many tricks did %s take?: ' % player_1))
							score_int = True
						
						except:
							pass
	
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
	
				else:
					for player in players:
						if player == player_1:
							full_board[player]['score'] = full_board[player]['score'] + player_1_round_score
	
						elif player == player_2:
							full_board[player]['score'] = full_board[player]['score'] + player_2_round_score
	
						else:
							full_board[player]['score'] = full_board[player]['score'] + player_3_round_score

				# print(full_board)
	
		if round_num < 4:
			print('\n')
			print('Current scores after Round %s: ' % round_num)

			for player in full_board:
				print('%s: %s' % (player,full_board[player]['score']))
			
			print('\n')
	
	print('\n')
	print('- - - - - GAME OVER - - - - -')
	print('\n')
	print('Final scores: ')
	
	for player in full_board:
		print('%s: %s' % (player,full_board[player]['score']))

	
	final_scores.extend((player_1_running_score, player_2_running_score, player_3_running_score))
	
	#### Determine Winner ####

	# Lowest possible score is -80 #
	max_score = -80 
	
	for player in players:
		if full_board[player]['score'] > max_score:
			max_score = full_board[player]['score']
			winner_list = [player]
	
		elif full_board[player]['score'] == max_score:
			winner_list.append(player)
	
		else:
			pass
	
	print('\n')

	if len(winner_list) == 1:
		print('%s wins!' % winner_list[0])
	
	elif len(winner_list) == 2:
		print('{0} and {1} tie for the win!'.format(*winner_list))
	
	else:
		print("0's all around... Everyone wins!  Or loses?")
	
	print('\n')

	### GET GAME NUMBER ###
	past_games_file_again = open('past_treikort_games.csv', "r+", encoding='utf-8-sig')
	pgf_reader = csv.DictReader(past_games_file_again)

	if sum(1 for row in pgf_reader) == 0:
		game_number = 1
	else:
		total_game_numbers = []
		past_games_file_again.seek(0)
		for row in pgf_reader:
			print('TGN')
			print(total_game_numbers)
			print('RGN')
#### WHY IS THIS PRINTING OUT THE KEY ?? ####
			print(row['game_number'])
#### WHY IS THIS PRINTING OUT THE KEY ?? ####			
			total_game_numbers.append(row['game_number'])
			print('EOL')

		print('TGNA')
		print(total_game_numbers)
		game_number = int(total_game_numbers[-1]) + 1

	print('GAME NUMBER IS: %s' % game_number)


	### ADD SCORE TO PAST SCORES FILE ###
	winner_list_string = ','.join(winner_list)

	past_scores_file = open('past_treikort_games.csv', 'a', encoding='utf-8-sig')
	p_s_writer = csv.writer(past_scores_file)
	p_s_writer.writerow([game_number,datetime.today().strftime('%Y-%m-%d %H:%M:%S'),player_1,full_board[player_1]['score'],player_2,full_board[player_2]['score'],player_3,full_board[player_3]['score'],winner_list_string])
	past_scores_file.close()
	
	### ASK IF REPLAY ###
	replay = input('Play again?  "Y" or "N": ').upper()
	
	while replay not in ['Y','N']:
		replay = (input('Please choose "Y" or "N": ').upper())