import unittest
from datetime import datetime

from engine import Engine
from battery import Battery


class TestCapuletEngine(unittest.TestCase):
	def test_needs_service(self):
		current_mileage = 30000
		last_service_mileage = 0
		
		capuletengine = CapuletEngine(current_mileage, last_service_mileage)
		self.assertTrue(capuletengine.needs_service())
		
	def test_does_not_need_service(self):
		current_mileage = 15000
		last_service_mileage = 0
		
		capuletengine = CapuletEngine(current_mileage, last_service_mileage)
		self.assertTrue(capuletengine.needs_service())
		
class TestSternmanEngine(unittest.TestCase):
	def test_needs_service(self):
		warning_light_is_on = True
		
		sternmanengine = SternmanEngine(warning_light_is_on)
		self.assertTrue(sternmanengine.needs_service())
		
	def test_does_not_need_service(self):
		warning_light_is_on = False
		
		sternmanengine = SternmanEngine(warning_light_is_on)
		self.assertTrue(sternmanengine.needs_service())
		
class TestWilloughbyEngine(unittest.TestCase):
	def test_needs_service(self):
		current_mileage = 60000
		last_service_mileage = 0
		
		willoughbyengine = WilloughbyEngine(current_mileage, last_service_mileage)
		self.assertTrue(willoughbyengine.needs_service())
		
	def test_does_not_need_service(self):
		current_mileage = 59999
		last_service_mileage = 0
		
		willoughbyengine = WilloughbyEngine(current_mileage, last_service_mileage)
		self.assertTrue(willoughbyengine.needs_service())
		
class TestSpindlerBattery(unittest.TestCase):
	def test_needs_service(self):
		current_date = datetime.today().date()
		last_service_date = today.replace(year=today.year - 3)
		
		spindlerbattery = SpindlerBattery(current_date, last_service_date)
		self.assertTrue(spindlerbattery.needs_service())
		
	def test_does_not_need_service(self):
		current_date = datetime.today().date()
		last_service_date = today.replace(year=today.year - 1)
		
		spindlerbattery = SpindlerBattery(current_date, last_service_date)
		self.assertTrue(spindlerbattery.needs_service())
		
class TestNubbinBattery(unittest.TestCase):
	def test_needs_service(self):
		current_date = datetime.today().date()
		last_service_date = today.replace(year=today.year - 5)
		
		nubbinbattery = NubbinBattery(current_date, last_service_date)
		self.assertTrue(nubbinbattery.needs_service())

	def test_does_not_need_service(self):
		current_date = datetime.today().date()
		last_service_date = today.replace(year=today.year - 3)
		
		nubbinbattery = NubbinBattery(current_date, last_service_date)
		self.assertTrue(nubbinbattery.needs_service())
		
if __name__ == '__main__':
    unittest.main()
