import random

# Instantiate the deck
suits = ('S','C','H','D')
ranks = ('A','2','3','4','5','6','7','8','9','10','J','Q','K')
# To-Do: handle Ace 11 points
card_value = ('A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10)

class Card:
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
	def __init__(self):
		self.deck = []
		# To-Do: Is there a product method equiv in Python?
		for suit in suits:
		for rank in ranks:
			self.deck.append(Card(suit,rank))

	def shuffle(self):
		random.shuffle(self.deck)

	def deal(self):
		first_card = self.deck.pop()
		return first_card
	
class Hand:
	pass


# Game play
# Create a Deck
# Shuffle it
# Give hands to players
# Hitting and Standing