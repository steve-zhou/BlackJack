import random
from decks.cards.card import Card

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

class Deck(object):
	"""docstring for Deck"""
	def __init__(self):
		super(Deck, self).__init__()
		self.deck = []
		global suits
		global ranks
		for suit in suits:
			for rank in ranks:
				self.deck.append(Card(rank,suit))

	def __str__(self):
		for card in self.deck:
			print('{0}'.format(card))

	


