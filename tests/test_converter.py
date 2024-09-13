# Copyright (C) 2023 Maxim Fedotov <maxim.fedotov@upf.edu>

from ..utils import MeasureConverter
from numpy import isclose

def test_converter():
    assert isclose(
        MeasureConverter.convert("hp", "kWh", 100),
        74.57,
        rtol=1e-4
    )