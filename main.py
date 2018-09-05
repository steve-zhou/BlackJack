import math
from theGame import BlackJackGame


playersStand = []
counter = 0

while True:
	print("Welcome to the Black Jack Game !")
	myGame = BlackJackGame(5)
	myGame.createPlayer(myGame.players)
	myGame.shuffle()
	
	for i in range(0,2):
		myGame.dealer.hand.add_card(myGame.deal())

	for player in myGame.totalPlayers:
		for i in range(0,2):
			player.hand.add_card(myGame.deal())
		counter += 1
		player.name = '{0}'.format(counter)


	for player in myGame.totalPlayers:
		amount = None 
		while not isinstance(amount, int):
			try:
				amount = int(input("Player #{} Enter a bet amount<Max 100>: ".format(player.name)))

				if amount > 100:
					player.chip.bet = 100
				else:
					player.chip.bet = int(amount)
			except Exception as e:
				continue
		

	for player in myGame.totalPlayers:
		myGame.show_all(player)

	myGame.show_some(myGame.dealer)

	for player in myGame.totalPlayers:
		while True:
			message = ""
			while message not in ('h', 's'):
				message = input("Player #{}, Do you want to Hit or Stand < h / s >: ".format(player.name))
			if message == 'h'.lower():
				myGame.hit(player)
				if myGame.busts(player):
					player.chip.total -= player.chip.bet
					print("Player #{} is Busted".format(player.name))
					myGame.show_all(player)
					break
				else:
					myGame.show_all(player)
			else:
				playersStand.append(player)
				break


	for player in playersStand:
		while myGame.dealer.hand.value < player.hand.value:
			myGame.hit(myGame.dealer)
		if myGame.busts(myGame.dealer):
			myGame.dealer.chip.total -= player.chip.bet
			player.chip.total += player.chip.bet
			print("player {0} Win!".format(player.name))
			myGame.show_all(player)
			myGame.show_all(myGame.dealer)
		else:
			myGame.dealer.chip.total += player.chip.bet
			player.chip.total -= player.chip.bet
			print("Dealer Win!")
			myGame.show_all(myGame.dealer)
			myGame.show_all(player)

	again = ""
	while again not in ('y', 'n'):
		again = input("Do  you want to play again: Y / N : ")
	if again == 'n'.lower():
		print("Thanks for playing the game!")
		break
	else:
		counter = 0
		playersStand = []






