class Card(object):
	"""docstring for Card"""
	def __init__(self, rank, suit):
		super(Card, self).__init__()
		self.values = {'Two':2, 'Three':3, 'Four':4, 'Five':5 , 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}
		self.rank = rank
		self.suit = suit

	def __str__(self):
		return "{0}".format(self.values[self.rank])
