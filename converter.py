'''
Author: Kevin Ramirez
Date: 2/8/26
Program: converter.py
Purpose: converting measurement unit to desired measurement
'''
from inputcollector import InputCollector
#using dictionary to have the key be length, mass, or liquid volume 
#and a nested for measurement and value for specific conversion
measurment_conversions ={

    'length':
    {
        'meters': 1, 
        'kilometers': 1000,
        'centimeters': 0.01,
        'inches': 0.025,
        'feet': 0.3048,
        'miles': 1609.34
    },
       
    'mass': 
    {
        'kilograms': 1,
        'grams': 1000,
        'pounds': 2.20462,
        'ounces': 35.274,
    },

    #will be converting to litre and the measurment conversion is from US measurments to litre not Imperial measurment
    'liquid': 
    {
        'litres': 1,
        'gallons': 3.785,
        'pints': .4732,
        'quarts': .9463,
        'cups': .24,
    }

}
     
#class for length, mass, and liquid volume conversion
class general_conversion:
    #constructor
    def __init__(self, measurement: str, value: float, initial_unit: str, converted_unit: str):
        self.measurement = measurement
        self.value = value
        self.initial_unit = initial_unit
        self.converted_unit = converted_unit

    def convert(self) -> float:
        #searches the dictionary since we specifically know what to look for 
        valueFrom = measurment_conversions[measurement][self.initial_unit]
        valueTo = measurment_conversions[measurement][self.converted_unit]

        #this part is the converting formula to all measurements
        #since its putting them in general form to either meters(m), kilograms(kg), litres(L)
        #then applying them to user requested conversion unit
        baseValue: float = self.value * valueFrom
        conversion_Value: float = baseValue / valueTo

        return conversion_Value


#for class tempature and only need two parameters, using convertValue for determining conversion and value to convert
class Temperature:
    #constructor
    def __init__(self, value: float, initial_unit: str, convert_unit:str):
        self.value = value
        self.initial_unit = initial_unit
        self.convert_unit = convert_unit

    #using convert_unit as condition to determine conversion
    def convert(self) -> float:
        if self.initial_unit == "celsius" and self.convert_unit == "fahrenheit":
            return (self.value * 9 / 5) + 32
        elif self.initial_unit == "fahrenheit" and self.convert_unit == "celsius":
            return (self.value - 32) * 5 / 9
        else:
            raise ValueError(f"Invalid temperature conversion from {self.initial_unit} to {self.convert_unit}. Only celsius to fahrenheit only.")

#accessing the variables from input collector class
measurement: str = ""
value: float = None
goodValue:str = ""
convertValue: str = ""

variables = InputCollector(measurement, value, goodValue, convertValue)
measurement, value, goodValue, convertValue = variables.input_user_req()

#if else will take the returnec varaibles from inputcollector and perform coditional logic and print users conversions 
if measurement == 'temperature':

    conv = Temperature(value, goodValue, convertValue)
    result = conv.convert()
    print(f"{value} {goodValue} converted to {result:.2f} {convertValue}.")

else:
    conv = general_conversion(measurement, value, goodValue, convertValue)
    result = conv.convert()
    print(f"{value} {goodValue} converted to {result:.1f} {convertValue}.")
