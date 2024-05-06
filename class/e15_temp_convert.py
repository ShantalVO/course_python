"""
Write a program that displays a temperature conversion table for degrees Celsius and degrees Fahrenheit.
The table should include rows for all temperatures between 0 and 100 degrees Celsius that are multiples of 10 degrees Celsius.
Include appropriate headings on your columns.
The formula for converting between degrees Celsius and degrees Fahrenheit can be found on the Internet.
"""

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

print("Celsius\tFahrenheit")
print("-------------------")
for celsius in range(0, 101, 10):
    fahrenheit = celsius_to_fahrenheit(celsius)
    print("{:.0f}\t{:.1f}".format(celsius, fahrenheit))

# __________________________________________________________________________________________________________________

