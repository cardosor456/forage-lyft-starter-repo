from tires.tires import Tires


class OctoprimeTires(Tires):
	def __init__(self, tire_wear_sensor):
		self.tire_wear_sensor = tire_wear_sensor
		
	def needs_service(self): # Needs service when sum of all values in wear sensor array >= 3
		sensor_counter = 0
		
		for i in range(len(tire_wear_sensor)):
			sensor_counter = sensor_counter + tire_wear_sensor[i]
				
		if sensor_counter >= 3:
			return True
		else:
			return False