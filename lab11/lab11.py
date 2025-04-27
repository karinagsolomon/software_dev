"""
Karina Solomon
April 27, 2025, Python Applications
"""
# '*' imports everything from another file
from lab11_functions import * 
# import 'math' module
import math
("\n------ Ex 1: Python Dictionary ------")
car = {
    "brand": "Ford",
    "model": "Mustang", # quotation marks needed around text keys
    "year": 1964 # no need for quotation marks around numerical keys
}

# print a complete dictionary
print(car)
# to access items in a dictionary, we use [], where [] goes the key's name
print(f"The year of the car is {car['year']}")
# update value of the key
car["year"] = 1980
print(f"The updated year of the car is {car['year']}")
# add value:pair
car["color"] = ["red"]
print(f"The color of the car is {car['color']}")
print(car)
print("\n Loop through each key in the dictionary")
for k in car:
    print(f"{k} has value = {car[k]}")

("\n------ Ex 2: Python Dictionary application ------")
# given the ff list, create a dictionary that will count the number of times that a word appears in the string.
# create a dictionary to organize the words as the keys, and the number of occurency of the word as the value of the key
phrase = "to be or not to be"
print(f"original phrase = {phrase}")
split_phrase = phrase.split()
print(f"splitted phrase = {split_phrase}")
# create the dictionary
word_count_dict = {}
# loop to each word in the list
for word in split_phrase:
    if word in word_count_dict:
        word_count_dict[word] += 1
    else:
        word_count_dict[word] = 1

print("result of dictionary: ")
# loop to print results
for w in split_phrase:
    print(f"{w} = {word_count_dict[w]}")

("\n------ Ex 3: func that doesn't return values ------")
# run function 'greeting'
greeting()

# run func 'username'
printusername("Karina Solomon") # enter argument when calling func

("\n------ Ex 5: ex func w/ default parameters ------")
user_country("Karina", "USA")
user_country("Mike")
user_country("", "New Zealand")

("\n------ Ex 6: func w/ return value ------")
num1 = 3
num2 = 4
prod1 = product(3, 4) # overrides arguments in orig func
print(f"The product of {num1} and {num2} is {prod1}")
prod1 = product() # calls arguments assigned in orig func
print(f"The product is {prod1}")

("\n------ Ex 7: Boolean func ------")
checknum1 = multiple3(num1)
checknum2 = multiple3(num2)
print(f"Is {num1} a multiple of 3? {checknum1}")
print(f"Is {num2} a multiple of 3? {checknum2}")

("\n------ Ex 8: composition func ------")
# test collectnum()
# number = collectnum()
# print(number)
# test sumnumbers()
sumall = sumnumbers(3)
printresult(sumall)

("\n------ Ex 9: built-in func ------")
#print(areacircle(2))

r = 2
a = areacircle(r)
areaprint(a,r)

("\n------ Ex 10: try-except ------")
ratio = ratio_hour(0)
print(ratio)
"""
try:
    ratio = ratio_hour()
except:
    print("Error with the function")

print(ratio)
"""
r1 = ratio_hour(0)
r2 = ratio_hour(3)
r3 = ratio_hour("Peter")

("\n------ Ex 11: classes ------")
# create an instance of the class
user1 = Myclass()
print(f"An instance of the class = {user1}")
# call the class' property
user1id = user1.id
print(f"User 1 ID is {user1id}")
# call the class' method
user1msg = user1.msg()
print(f"User 1 message is {user1msg}")

("\n------ Ex 12: instantiation classes ------")
# create an instance of the class
paircomplexnumber = Complexnumber(2, 3)
# call the instance object of the 'r' class
real = paircomplexnumber.r
print(f"User 1 message is {real}")

("\n------ Ex 13: classes application------")
# create an instant of the class
car1 = Car("Tesla", "S", 2023)
# call property odometer reading
car_reading = car1.odometer_reading
print(f"Car miles reading is {car_reading}")
# call method get_car_description()
print(car1.get_car_description())
# call method read_odometer
print(car1.read_odometer())
# update odometer to mileage = 10
car1.update_odometer = 10
print(car1.read_odometer())
car1.update_odometer = 5
print(car1.read_odometer())

# add 20 mi to the odometer