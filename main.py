class Player:
	def __init__(self, name):
		self.name - name
		self.gold = 100
		self.items = []

class Place:
	def __init__(self, descr, dirs):
		self.descr = descr
		self.dir = dirs

class Weapon:
	def __init__(self, dmg):
		self.dmg = dmg

class Item:
	def __init__(self, name):
		self.name = name

class Monster:
	def __init__(self, name, atk):
		self.name = name
		self.atk = atk

places = {
	'house': Place("Your home", ['street']),
	'street': Place("The main street of town that splits up to the forest beyond and to the marketplace", ['home', 'forest', 'market']),
	'market': Place("THe place you can get all the items you need for your journey", ['general store', 'weapon store', 'street']),
	'general store': Place("Buy your consumable items here", ['market']),
	'weapon store': Place("Buy your weapons here", ['market']),
	'forest': Place("A forest filled with monsters", ['river','cave']),
	'river': Place("A river full of fish", ['forest']),
	'cave': Place("A small cave", ['forest'])
}

place = places['house']
def move():
	while True:
		print(place.descr)
		while True:
			print("-"*35)
			print("You can go to: " +(', '.join(places.dirs)))
			to=input("Where do you want to go? ")
			if to in places.dirs:
				break
			print("Invalid location")
		place=places[to]
		print("-"*35)

