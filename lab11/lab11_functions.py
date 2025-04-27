"""
Karina Solomon
April 27, 2025, Python Applications
"""
# import 'math' func
import math 
# example 3
def greeting():
    print('Welcome to functions!') # prints nothing

# ex 4, func with parameter 'username'
def printusername(username):
    print(f"Welcome to function {username}")

# ex 5, func with default parameters
def user_country(username = "unknown", country = "nowhere"):
    print(f"{username} is based in {country}")
    return

# ex 6, func that returns a value 
# func that takes 2 numbers and returns 
def product(n1=5, n2=2):
    return n1 * n2

# ex 7, boolean func
# func to check if a number is a multiple
def multiple3(n):
    if n%3 == 0 and n != 0:
        return True
    else:
        return False
    
# ex 9, composition func
# define func to collect, validate, and return a number between 1 and 9
def collectnum():
    n = float(input("Enter a number: "))
    # validate the number
    while (not(1 <= n <= 9)):
        n = float(input("Re-enter number again: "))
    return n

def sumnumbers(totalnumbers=0):
    sum = 0
    for n in range(totalnumbers):
        sum += collectnum()
    return sum

# func to print result
def printresult (totalsum):
    print(f"Sum of all numbers is {totalsum}")

def areacircle (radius):
    a = math.pow(radius, 2) * math.pi
    return round(a,2) # rounds to 2 decimal places

# func to print result
def areaprint (area, radius=0):
    print(f"The area of a circle with {radius} radius is {area}")

# ex 10: try-except
# func to return the ratio of 2 numbers (hrs)
def ratio_hour(hour):
    try:
        dayhour = 24
        r = dayhour/hour
    except ZeroDivisionError:
        print("ZERO EXCEPTION")
        print("Number cannot be divided by 0")
        return 0
    except ValueError:
        print("VALUE EXCEPTION")
        print("Number was not provided")
        return 0
    except:
        print("GENERAL EXCEPTION")
        print("There was an error in the division")
    else:
        print("DIVISION IS FINE")
        return r
    finally:
        print("Process complete!")

# ex 11: defining a class name, 'Myclass'
class Myclass: # it's recommended to capitalize first letter of class
    # property attribute 
    id = 12345
    # method
    def msg(self):
        print("Welcome to Python class!")

# ex 12
class Complexnumber():
    #instantiate of the class
    def __init__(self, realnumber, imaginarynumber):
        self.r = realnumber
        self.i = imaginarynumber

# ex 13
class Car:
    # instantiate of the Car
    def __init__(self, make , model, year):
        self.carmake = make
        self.carmodel = model
        self.caryear = year

        # set property 'odometer'
        odometer_reading = 0

        # method to return descriptive of the car
        def getcardescription(self):
            return f"{self.carmake} with model {self.carmodel} was manufactured on {self.caryear}"
        
        # method to read the odometer
        def read_odometer(self){
            return f"This car has {self.odometer_reading} miles on it"
        }

        # method to update the odometer
        def update_odometer(self, mileage){
            if mileage > self.odometer_reading:
                self.odometer_reading = mileage
            else:
                print("Odometer cannot roll back")
        }
        # method to add mi to the odometer
        def increment_odometer(self, miles){
            if miles > 0:
                self.odometer_reading += miles
            else:
                print("Can't add negative miles")
        }