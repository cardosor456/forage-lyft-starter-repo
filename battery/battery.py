from abc import ABC

from car import Car


class Battery(Car, ABC):
    def needs_service():
        pass