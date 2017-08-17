import random

# Instantiate the deck
suits = ('S','C','H','D')
ranks = ('A','2','3','4','5','6','7','8','9','10','J','Q','K')
# To-Do: handle Ace 11 points
card_value = ('A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10)

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
		if hidden == True and playing == True:
			first_card = 1
		else:
			first_card = 0

		for x in range(first_card,len(self.cards)):
			self.cards[x].draw()



# Game play
def deal_cards():
	deck = Deck()
	deck.shuffle()

	player_hand = Hand()
	dealer_hand = Hand()

	player_hand.add_card(deck.deal())
	player_hand.add_card(deck.deal())

	dealer_hand.add_card(deck.deal())
	dealer_hand.add_card(deck.deal())

# Hitting and Standing
def hit():
	pass

def stand():
	pass