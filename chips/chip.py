class Chip(object):
	"""docstring for Chip"""
	def __init__(self):
		super(Chip, self).__init__()
		self.total = 100
		self.bet = 0

	def win_bet(self):
		previous = self.total
		return (self.total + self.bet) - previous
		

	def lose_bet(self):
		if self.bet > self.total:
			print('You do not have enough to cover: {0}'.format(self.total))
			return self.total
		else:
			self.total -= self.bet
			return self.bet

	def bet_amount(self, amount):
		if self.total > amount:
			self.total -= amount
			return amount
		else:
			print('You only have {0} left'.format(self.total))
			return self.total
		