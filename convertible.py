# Copyright (C) 2023 Maxim Fedotov <maxim.fedotov@upf.edu>

from numbers import Number
from .car import Car

# Let's add a class that inherits properties and methods from the Car class.
# You can check that method .move works as well for an instance of 
# class Convertible as it is inherited from Car.

class Convertible(Car):
    
    roof_states = ['up', 'down']
    
    def __init__(
        self, 
        model: str, 
        color: str, 
        horse_power: int, 
        roof_state: str, 
        location: Number = 0
    ) -> None:
        if roof_state not in self.roof_states:
            raise ValueError('The roof parameter can be either up or down.')
        # super() refers to the parent class
        super().__init__(model, color, horse_power, location)  
        self.roof_state = roof_state
    
    def roof_switch(self):
        if self.roof_state == "up":
            self.roof_state = "down"
        if self.roof_state == "down":
            self.roof_state = "up"