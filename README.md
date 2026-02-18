README for Converter.py functionality-
This program will be converting different measurments such as:
length(meters, kilometers, centimeters, feet, inches, miles),
mass(pounds, ounces, grams, kilograms),
liquid volume(liters, gallons, quarts),
tempature(celcius, and fahrenhiet)

Inputcollector(By Darrel)- takes users input for measurement, value, and both from and to units. Has exception handling for user input validation

For the converter program approach - a way to approach this be to create a general convertion program
I'm think of having a way to take inputcollector module return varialbes: measurement, value goodvalue, and convertvalue and 
creating a way to map each measurement with its base SI unit to a dictionary e.g {"kilometers": 1.609} 1.609 in meters, so every conversion will be set to base unit either in meters, kilograms or litre

If goodvalue is kilometers, it'll search through the dictionary for the value tied to the key
and same with countervalue and perform the conversions

e.g psuedocode

measurement = length
value = 10
goodvalue = in
convertvalue = cm

ValueFrom = dict{key, value}
ValueTo = dict{key, value} 

baseValue = 10 * baseformValue(base unit m)
ConvertedValue = baseValue / valueTo

print/return counvertedValue

this will only be for mass(weight) and length(distance) since tempature is only f and c since were not doing kelvin

would need to update inputcollector to get users measurement for either length, mass, liquid volume or temperature
