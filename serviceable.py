from abc import ABc
from car import Car


class Serviceable(Car, ABC):
    def needs_service():
        pass