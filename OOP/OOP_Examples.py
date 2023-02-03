class Fruit:
	def __init__(self):
		self.name="apple"
		self.colour="red"


myFruit=Fruit()

myFruit.colour="green"
myFruit.name="kiwi"

print(myFruit.colour)
print(myFruit.name)

##################

class Fruit2:
	def __init__ (self, name, clr):
		self.name=name
		self.colour=clr

apple = Fruit2("apple","red")
orange = Fruit2("orange","orange")
pineapple = Fruit2("pineapple","yellow")
