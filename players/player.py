
from chips.chip import Chip 
from hands.hand import Hand 

class Player(object):
	"""docstring for Player"""
	def __init__(self,name = 'Default Player'):
		super(Player, self).__init__()
		self.chip = Chip()
		self.hand = Hand()
		self.name = name 


	def __str__(self):
		return 'Chip: {0}'.format(self.chip.total)


		