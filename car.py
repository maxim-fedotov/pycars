from numbers import Number 
from typing import Literal


class Car:
    
    directions = ["left", "right"]
    
    def __init__(
        self,
        model: str,
        color: str,
        horse_power: int,
        location: Number = 0
    ) -> None:
        self.model = model
        self.color = color
        self.horse_power = horse_power
        self.location = location
        
    def move(
        self, 
        direction: Literal["left", "right"],
        by: Number
    ) -> None:
        if direction not in self.directions:
            raise ValueError(
                "Direction must be either "
                + " or ".join(self.directions) + "."
            )
        self.location += (2 * (direction == "right") - 1) * by