# Copyright (C) 2023 Maxim Fedotov <maxim.fedotov@upf.edu>

from ..car import Car

def test_move():
    car = Car(
        model="Fancy Car", 
        color="red",
        horse_power=10
    )
    car.move("right", 10)
    assert car.location == 10
    car.move("left", 20)
    assert car.location == -10