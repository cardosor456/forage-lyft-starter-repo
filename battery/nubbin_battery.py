from abc import ABC

from engine import Engine


class NubbinBattery(Battery, ABC):
    def __init__(self, last_service_date, current_date):
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self):
        return getYear(self.current_date) - getYear(self.last_service_mileage) >= 4