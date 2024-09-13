# Copyright (C) 2023 Maxim Fedotov <maxim.fedotov@upf.edu>

class MeasureConverter:
    
    measures_dictionary = {"hp": ["kWh"], "kWh": ["hp"]}
    
    @staticmethod
    def convert(_from: str, _to: str, value):
        if {_from, _to} == {"hp", "kWh"}:
            multiplier = 0.7457 if _from == "hp" else 0.7457**(-1)
            value_converted = multiplier * value 
            return value_converted
        else:
            raise NotImplementedError("Conversion for measures other than hp and kWh are not implemented")
    
    @classmethod
    def convertable_to(cls, _from: str):
        print(f"This converter can convert {_from} to:", *cls.measures_dictionary[_from])