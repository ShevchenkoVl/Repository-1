class Ship:
	date_creat = "2015"

	def ship_info(self):
		print(f"\nDate of creation is {self.date_creat}") 

class WarShip(Ship):
	country = "UK"
	
	def war_ship_info(self):
		self.ship_info
		print(f"\nCountry is {self.country}")

class CivilShip(Ship):
	size = "Big"
	
	def civil_ship_info(self):
		self.ship_info
		print(f"\nSize is {self.size}")

class AircraftCarrier(WarShip):
	number_of_airplanes = 50
	
	def aircraft_info(self):
		self.ship_info
		self.war_ship_info
		print(f"\nNum is {self.number_of_airplanes}")

class Cruiser(WarShip):
	kind = "Heavy"

	def cruiser_info(self):
		self.ship_info
		self.war_ship_info
		print(f"\nIt is {self.kind} cruiser" )

class Destroyer(WarShip):
	weapon = "12 Cannons"

	def destroyer_info(self):
		self.ship_info
		self.war_ship_info
		print(f"\nDestroyer have {self.weapon}" )	

class TechnicalShip(CivilShip):
	appointment = "Repair"
	
	def tship_info(self):
		self.ship_info
		self.civil_ship_info
		print(f"\nIt is {self.appointment} ship" )	

class IndustrialShip(CivilShip):
	type_of_ship = "oil production"
	
	def indship_info(self):
		self.ship_info
		self.civil_ship_info
		print(f"\nIt is {self.type_of_ship} ship" )	

class PassengerShip(CivilShip):
	number_of_passengers = 2000
	
	def pship_info(self):
		self.ship_info
		self.civil_ship_info
		print(f"\nNumber Of Passengers {self.number_of_passengers}" )	

class CargoShip(CivilShip):
	lifting_capacity = "20T"
	
	def cargoship_info(self):
		self.ship_info
		self.civil_ship_info
		print(f"\nLifting capacity {self.lifting_capacity}" )

ship=Ship()
ship.ship_info()

warship=WarShip()
warship.war_ship_info()

civilship=CivilShip()
civilship.civil_ship_info()

aircraft=AircraftCarrier()
aircraft.aircraft_info()

cruiser=Cruiser()
cruiser.cruiser_info()

destroyer=Destroyer()
destroyer.destroyer_info()

tship=TechnicalShip()
tship.tship_info()

iship=IndustrialShip()
iship.indship_info()

pship=PassengerShip()
pship.pship_info()

cargoship=CargoShip()
cargoship.cargoship_info()