from tires.tires import Tires


class CarriganTires(Tires):
	def __init__(self, tire_wear_sensor):
		self.tire_wear_sensor = tire_wear_sensor
		
	def needs_service(self): # Needs service when any value in wear sensor array >= 0.9
		needs_service = False
		
		for i in range(len(tire_wear_sensor)):
			if tire_wear_sensor[i] >= 0.9:
				needs_service = True
				
		if needs_service == True:
			return True
		else:
			return False