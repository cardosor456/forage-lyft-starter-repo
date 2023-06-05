from abc import ABC

from car import Car


class Engine(Car, ABC):
    def needs_service():
        pass