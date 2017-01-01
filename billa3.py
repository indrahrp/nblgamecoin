import time
class Player(object):
	def __init__(self,name):
		name=name
	def takecoins(self,totalleft):
		self.coinstotake=raw_input('\nenter how many coins to take : ')
		print "Taking " + self.coinstotake + " coins "
		return int(self.coinstotake)

class Computer(Player):
	def __init__(self,name):
		Player.__init__(self,name)
		
	def takecoins(self,totalleft):
		print " \n\n\nComputer turn now , thinking ..."
		time.sleep(2)
		if totalleft % 3 == 0:
			print "Taking 2 coins "
			return 2
		else:
			print "Taking 1 coins "
			return 1

	def __str__ (self):
		return "Computer"
		
class Human(Player):
	def __init__ (self,name):
		Player.__init__(self,name)
	
	def takecoins(self,totalleft):
		print "\n\n\nHuman turn now "
		return Player.takecoins(self,totalleft)
		
	def __str__ (self):
		return "Human"
	
	
class GameControl(object):
	
	def __init__(self,name):
		self.name=name
		self.computer=Computer('supercomputer')
		self.human=Human('person')
		
	def startgame(self):
		self.gameboard=GameBoard("Coins Game"," &",23)
		print "\nStart the game ..."
		
	def showingboard(self):
		self.gameboard.printboardgame()
	
	def updatecoinsleft(self,coinstaken):
		self.gameboard.updatecoinsleft(coinstaken)
		
	def askingwhofirst(self):
		whofirst=raw_input("\n\nenter who will play first 'human' Or 'computer' : ")
		if  whofirst== 'computer':
			self.whoseturn=self.computer
		else:
			self.whoseturn=self.human
			    	
	
	def activate(self):
		
			coinstaken=self.whoseturn.takecoins(self.gameboard.totalcoins)
			self.updatecoinsleft(int(coinstaken))
			self.showingboard()
			if self.gameboard.totalcoins == 0:
				self.wholost = str(self.whoseturn)	
			elif str(self.whoseturn) == 'Computer':
				self.whoseturn=self.human
			else:
				self.whoseturn=self.computer
	

class GameBoard(object):
	def __init__(self,name,coinspicture,totalcoins):
		self.coinspicture=coinspicture
		self.totalcoins=totalcoins
	def updatecoinsleft(self,coinstaken):
		self.totalcoins=self.totalcoins - coinstaken	
	def printboardgame(self):
		print "\nTotal Coins Left " + str( self.totalcoins)+ " ==> " + self.coinspicture * self.totalcoins
		
gc=GameControl("Coin Game")
gc.startgame()
gc.showingboard()
gc.askingwhofirst()
while gc.gameboard.totalcoins > 0:
	gc.activate()
print "Who is lost " + gc.wholost

