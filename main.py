class Player:
	def __init__(self):
		pass

class Places:
	def __init__(self, descr, dirs):
		self.descr = descr
		self.dir = dirs

class Weapons:
	def __init__(self, dmg):
		self.dmg = dmg

class Items:
	def __init__(self, name):
		self.name = name

class Monsters:
	def __init__(self, name, atk):
		self.name = name
		self.atk = atk

place = {
	'house': Places("Your home", ['street']),
	'street': Places("The main street of town that splits up to the forest beyond and to the marketplace", ['home', 'forest', 'market']),
	'market': Places("THe place you can get all the items you need for your journey", ['general store', 'weapon store', 'street']),
	'general store': Places("Buy your consumable items here", ['market']),
	'weapon store': Places("Buy your weapons here", ['market']),
	'forest': Places("A forest filled with monsters", ['river','cave']),
	'river': Places("A river full of fish", ['forest']),
	'cave': Places("A small cave", ['forest'])
}



