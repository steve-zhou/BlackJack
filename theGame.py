import random
from chips.chip import Chip 
from hands.hand import Hand 
from decks.deck import Deck 
from players.player import Player

 
class BlackJackGame(object):
	"""docstring for BlackJackGame"""
	totalMoneyPool = 0
	gameDeck = Deck()


	def __init__(self, players = 1):
		super(BlackJackGame, self).__init__()
		self.players = players
		self.totalPlayers = []
		self.dealer = Player("Dealer")


	def createPlayer(self, number):
		for i in range(0,number):
			self.totalPlayers.append(Player())
		

	def shuffle(self):
		random.shuffle(self.gameDeck.deck)

	def deal(self):
		value = self.gameDeck.deck.pop(0)
		return value

	def wins(self,player, dealer):
		if player.hand.value == 21 and dealer.hand.value == 21:
			return 1
		elif player.hand.value == 21 or dealer.hand.value > 21:
			return 2

	def busts(self,player):
		return player.hand.value > 21 

	def hit_or_stand(self, choice):
		return choice == 'h'.lower()


	def show_all(self,player):
		print("name: {0}, {1}, cards: ({2})".format(player.name, str(player), player.hand.current_hand_of_cards()))

	def show_some(self, player):
		if player.name == "Dealer":
			print("name: {0}, {1}, cards: ({2})".format(player.name, str(player), player.hand.dealerHand()))

	def hit(self,player):
		card = self.gameDeck.deck[0]
		print("Card that is being added: {0}".format(card))
		player.hand.add_card(self.gameDeck.deck.pop(0))

		
		



		



