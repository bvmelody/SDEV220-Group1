#the following class is used to get the users input.  the user must enter a valid numerical value along with valid units that tell 
#the app the original unit value and the selected value output
class InputCollector:

    '''
        contain sets for the units and type of measurement
        contain class for taking users requests
    '''
    #adding the remaining conversion units to set
    MEASURING_UNITS = {"meters", "kilometers", "centimeters", "feet", "inches", "miles",
        "pounds", "kilograms", "grams", "ounces",
        "liters", "gallons", "quarts", "pints", "cups",
        "celsius", "fahrenheit"}
    #creating the set for users measurement
    MEASUREMENTS = {"length", "mass", "liquid", "temperature"}

    #creating constuctor -kevin
    def __init__(self, value=None, goodvalue=None, convertvalue=None, measurement=None):
        self.value = value
        self.goodvalue = goodvalue
        self.convertvalue = convertvalue
        self.measurement = measurement

    def input_user_req(self):
        while True:

           #adding what kind of measurement the user wants - kevin
            self.measurement = input("Enter desire measurement(length, mass, liquid, or temperature): ").strip().lower()
           
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
        