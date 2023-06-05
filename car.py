from abc import ABC
from engine import Engine
from battery import Battery

class Car(Engine, Battery, ABC):
    def __init__(self, ABC): 

    def needs_service(self):
        pass
