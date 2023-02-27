"""Create a class named Temperature. Make two methods :
i. convert_fahrenheit - it will take the celsius and will print it into Fahrenheit
ii. convert_celsius - it will take the Fahrenheit and will convert it to Celsius"""

celsius = int(input("Enter the temperature in degrees : "))
fahrenheit = int(input("Enter the temperature in fahrenheit : "))

class Temperature:
    def __init__(self,celsius,fahrenheit):
        self.celsius = celsius
        self.fahrenheit = fahrenheit

    def convert_fahrenheit(self):
        return (self.celsius * (9/5)) + 32
    
    def convert_celsius(self):
        return (self.fahrenheit - 32) * (5/9)
    
temp = Temperature(celsius,fahrenheit)

print("Your temperature reading in fahrenheit is : ", temp.convert_fahrenheit())
print("Your temperature reading in degrees celsius is : ", temp.convert_celsius())




    