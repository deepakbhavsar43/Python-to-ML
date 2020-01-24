from abc import ABC, abstractmethod

class Vehicle(ABC):
	def fule(self):
		pass

	def transmission(self):
		pass


class Maruti(Vehicle):
	def fule(self):
		fule1 = "Petrol"
		print("Has petrol engine.")

	def transmission(self):
		transmission_type = "Automatic"
		print("Has auto transmission.")

class Toyota(Vehicle):
	def fule(self):
		fule1 = "Diesel"
		print("Has diesel engine.")

	def transmission(self):
		transmission_type = "Manual"
		print("Has manual transmission.")



Baleno = Maruti()
Fortuner = Toyota()
print("Baleno has following features : ")
Baleno.fule()
Baleno.transmission()

print("\nFortuner has following features : ")
Fortuner.fule()
Fortuner.transmission()
# print("Baleno has {} engine and {} transmission.",format(Baleno.fule, Baleno.transmission_type)
# print(Fortuner.transmission_type)