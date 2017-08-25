import random

class Card:
	# Properties of a card
	def __init__(self,suit,rank):
		self.suit = suit
		self.rank = rank

	def __str__(self):
		return self.suit + self.rank

	def get_suit:
		return self.suit

	def get_rank:
		return self.rank

class Deck:
	# Logic for dealing and shuffling
	def __init__(self):
		self.deck = []

		suits = ('S','C','H','D')
		ranks = ('A','2','3','4','5','6','7','8','9','10','J','Q','K')
		card_value = ('A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10)

		# To-Do: Is there a product method equiv in Python?
		for suit in suits:
			for rank in ranks:
				self.deck.append(Card(suit,rank))

	def shuffle(self):
		random.shuffle(self.deck)

	def deal(self):
		top_card = self.deck.pop()
		return top_card
	
class Hand:
	def __init__(self):
		self.cards = []
		self.value = 0
		self.ace = False

	def __str__(self):
		hand = ""

		for card in self.cards:
			card_name = card.__str__()
			hand += " " + card_name

		return 'The hand is %s' %hand

	def add_card(self,card):
		self.cards.append(card)

		if card.rank == 'A':
			self.ace == True
		self.value += card_value[card.rank]

	def calc_hand_val(self):
		if (self.ace == True and self.value < 12)
			return self.value + 10
		else:
			return self.value

	def draw(self,hidden):
		if hidden == True and your_turn == True:
			first_card = 1
		else:
			first_card = 0

		for x in range(first_card,len(self.cards)):
			self.cards[x].draw()

class Player():
	def __init__(self, player,purse=100):
		self.player = player
		self.purse = purse

	def bet():
		global bet
		bet = 0
		
		print 'Enter bet (as whole integer)'

		while bet == 0
			bet_check = int(raw_input())

			if bet_check >= 1 and bet_check <= purse:
				bet = bet_check
			else:
				print 'Invalid bet, you only have ' + str(purse) + "left."

	def hit():
		if your_turn:
			current_hand = player_hand.calc_hand_val()
			if current_hand <= 21:
				player_hand.add_card(deck.deal())

				print "Player's hand is %s" %player_hand
			elif current_hand > 21:
				result = 'Bust'

				purse -= bet
				your_turn = False
			else:
				result = "Can't hit"

			show_table()


	def stand():
		if your_turn == False
			player_score = player_hand.calc_hand_val()
			dealer_score = dealer_hand.calc_hand_val()

			if player_score > 0:
				result = 'You have to hit'
		else:
			# Soft 17
			while dealer_score < 17:
				dealer_hand.add_card(deck.deal())
			# Dealer bust
			if dealer_score > 21:
				result = 'Dealer bust. You win.'
				purse += bet
				your_turn = False
			# Player win
			elif dealer_score < player_score:
				result = 'You beat the dealer. You win.'
				purse += bet
				your_turn = False
			# Push
			elif dealer_score == player_score:
				result = 'Push'
				your_turn == False
			# Dealer wins
			else:
				result = 'Dealer wins.'
				purse -= bet
				your_turn = False

		show_table()

class Game():

	global move,your_turn,deck,player_hand,dealer_hand,purse,bet

	def __init__(self):
		self.dealer = Player()
		self.player = Player()

	def play():
		deck = Deck()
		deck.shuffle()

		players.bet()

		player_hand = Hand()
		dealer_hand = Hand()

		player_hand.add_card(deck.deal())
		player_hand.add_card(deck.deal())

		dealer_hand.add_card(deck.deal())
		dealer_hand.add_card(deck.deal())

		move = 'Hit or Stand? h/s'

		if your_turn == True:
			print 'Fold'
			purse -= bet

		your_turn = True
		show_table()

	def show_table():
		print ("Player's hand is: ")
		player_hand.draw(hidden = False)
		print "Player's hand total is: " + str(player_hand.calc_hand_val())

		print ("Dealer's hand is: ")
		dealer_hand.draw(hidden = True)
		print "Dealer's hand total is: " + str(dealer_hand.calc_hand_val())

		if your_turn == False:
			print 'For a total of ' + str(dealer_hand.calc_hand_val())
			print 'Chip total: ' = str(purse)
		else:
			print ' with another card hidden'

		print result

	def player_input():
		chomp = raw_input().lower()

		if chomp == 'h':
			hit()
		elif chomp == 's':
			stand()
		elif chomp == 'd':
			deal()
		elif chomp == 'q':
			exit_game()
		else:
			print 'Invalid input. Enter h, s, d or q.'

	def exit_game():
		exit()
