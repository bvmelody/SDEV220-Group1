import tkinter as tk

#using dictionary to have the key be length, mass, or liquid volume 
#and a nested for measurement and value for specific conversion - Kevin

'''
Final project submission, all sources pulled from GitHub Repo.  
Edited and Debugged by Darrell Cassidy

'''

measurement_conversions = {
    'length': {
        'meters': 1,
        'kilometers': 1000,
        'centimeters': 0.01,
        'inches': 0.0254,
        'feet': 0.3048,
        'miles': 1609.34
    },

    'mass': {
        'kilograms': 1,
        'grams': 0.001,
        'pounds': 0.453592,
        'ounces': 0.0283495
    },
#will be converting to liter and the measurment conversion is from US measurments to liter not Imperial measurment - Kevin
    'liquid': {
        'liters': 1,
        'gallons': 3.785,
        'pints': 0.4732,
        'quarts': 0.9463,
        'cups': 0.24
    }
}
'''
Author: Darrell Cassidy (edited by Kevin Ramirez)
Date: 2/2/26
Program: inputcollector.py

'''

#the following class is used to get the users input.  the user must enter a valid numerical value along with valid units that tell 
#the app the original unit value and the selected value output

class InputCollector:

    MEASURING_UNITS = {
        "meters", "kilometers", "centimeters", "feet", "inches", "miles",
        "pounds", "kilograms", "grams", "ounces",
        "liters", "gallons", "quarts", "pints", "cups",
        "celsius", "fahrenheit"
    }

    MEASUREMENTS = {"length", "mass", "liquid", "temperature"}

    def __init__(self, value=None, goodvalue=None, convertvalue=None, measurement=None):
        self.value = value
        self.goodvalue = goodvalue
        self.convertvalue = convertvalue
        self.measurement = measurement



    def input_user_req(self):
        while True:

            #adding what kind of measurement the user wants - kevin
            self.measurement = input("Enter measurement (length, mass, liquid, temperature): ").strip().lower()

            if self.measurement not in self.MEASUREMENTS:
                print("Invalid measurement.")
                continue

            try:
                self.value = float(input("Please enter a number here: "))
            except ValueError:
                print("that is not a valid number")
                continue

            self.goodvalue = input("please put a source unit in here: ").strip().lower()
            
            if self.goodvalue not in self.MEASURING_UNITS:
                print("invalid source unit")
                continue

            self.convertvalue = input("please put the unit you wish to convert to: ").strip().lower()
            if self.convertvalue not in self.MEASURING_UNITS:
                print("invalid converting unit")
                continue

            return self.measurement, self.value, self.goodvalue, self.convertvalue


'''
Author: Kevin Ramirez
Date: 2/8/26
Program: convertor.py
Purpose: converting measurement unit to desired measurement
''' 



class general_conversion:
     #constructor
    def __init__(self, measurement: str, value: float, initial_unit: str, converted_unit: str):
        self.measurement = measurement
        self.value = value
        self.initial_unit = initial_unit
        self.converted_unit = converted_unit
      #searches the dictionary since we specifically know what to look for

    def convert(self) -> float:
        value_from = measurement_conversions[self.measurement][self.initial_unit]
        value_to = measurement_conversions[self.measurement][self.converted_unit]
       #this part is the converting formula to all measurements
       #since its putting them in general form to either meters(m), kilograms(kg), litres(L)
       #then applying them to user requested conversion unit
        base_value = self.value * value_from
        conversion_Value = base_value / value_to

        return conversion_Value


#for class tempature and only need two parameters, using convertValue for determining conversion and value to convert
class Temperature:
     #Constructor
    def __init__(self, value: float, initial_unit: str, convert_unit: str):
        self.value = value
        self.initial_unit = initial_unit
        self.convert_unit = convert_unit
      #using convert_unit as condition to determine conversion
    def convert(self) -> float:
        if self.initial_unit == "celsius" and self.convert_unit == "fahrenheit":
            return (self.value * 9/5) + 32

        elif self.initial_unit == "fahrenheit" and self.convert_unit == "celsius":
            return (self.value - 32) * 5/9

        else:
            raise ValueError("Invalid temperature conversion.")





"""
The following ( def open_conversion_popup() ) was added to allow the convertor.py
to enteract with the GUI -  Darrell Cassidy

"""


def open_conversion_popup():
    popup = tk.Toplevel()
    popup.title("Unit Conversion")
    popup.geometry("350x400")

    tk.Label(popup, text="Measurement (length, mass, liquid, temperature):").pack()
    measurement_entry = tk.Entry(popup)
    measurement_entry.pack()

    tk.Label(popup, text="Value:").pack()
    value_entry = tk.Entry(popup)
    value_entry.pack()

    tk.Label(popup, text="From Unit:").pack()
    from_entry = tk.Entry(popup)
    from_entry.pack()

    tk.Label(popup, text="To Unit:").pack()
    to_entry = tk.Entry(popup)
    to_entry.pack()

    result_label = tk.Label(popup, text="", fg="red")
    result_label.pack(pady=20)

    def run_conversion():
        
        measurement = measurement_entry.get().strip().lower()
        from_unit = from_entry.get().strip().lower()
        to_unit = to_entry.get().strip().lower()

        VALID_MEASUREMENTS = {"length", "mass", "liquid", "temperature"}
        VALID_UNITS = {
        "meters", "kilometers", "centimeters", "feet", "inches", "miles",
        "pounds", "kilograms", "grams", "ounces",
        "liters", "gallons", "quarts", "pints", "cups",
        "celsius", "fahrenheit"
           }

        if measurement not in VALID_MEASUREMENTS:
            result_label.config(text=f"Invalid measurement type: {measurement}")
            return

        if from_unit not in VALID_UNITS:
            result_label.config(text=f"Invalid source unit: {from_unit}")
            return

        if to_unit not in VALID_UNITS:
            result_label.config(text=f"Invalid target unit: {to_unit}")
            return


        try:
            value = float(value_entry.get())
        except ValueError:
            result_label.config(text="Invalid numeric value.")
            return

        try:
            if measurement == "temperature":
                conv = Temperature(value, from_unit, to_unit)
            else:
                conv = general_conversion(measurement, value, from_unit, to_unit)

            result = conv.convert()
            result_label.config(text=f"Result: {result:.4f} {to_unit}")

        except Exception as oops:
            result_label.config(text=f"Error: {oops}")

    tk.Button(popup, text="Convert", command=run_conversion).pack(pady=20)



'''
Author: Brenden Melody (Turned in before switching to other group - Darrell Cassidy)

'''

def main():
    mainMenu = tk.Tk()
    mainMenu.title("Math Converter")
    mainMenu.geometry("500x500")
    mainMenu['background'] = "white"

    welcomeMessage = tk.Label(mainMenu, text="Welcome to our Metric/Imperial Converter!")
    imperialToMetric = tk.Button(mainMenu, text="Imperial to Metric", command=open_conversion_popup)
    metricToImperial = tk.Button(mainMenu, text="Metric to Imperial", command=open_conversion_popup)
    exitButton = tk.Button(mainMenu, text="Exit", command=mainMenu.quit)

    welcomeMessage.pack()
    imperialToMetric.pack()
    metricToImperial.pack()
    exitButton.pack()

    mainMenu.mainloop()



if __name__ == "__main__":
    
    main()