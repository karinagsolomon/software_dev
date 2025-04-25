"""
Karina Solomon 
April 24, conditional statement
"""
print("\n------ example 1 and 2: if statement ------")
age = 21
agecode = 123
if age >= 21:
    print("You are an adult!")
    agecode = 200
else:
    print("You are under 21.")
    agecode = 100
print(f"After the 'if' statement, age = {agecode}")

print("\n------ example 3: multi statement ------")
age = -1
if age > 0 and age < 21:
    print("You are a minor!")
elif age >= 21 and age < 65:
    print("You are an adult!")
elif age >= 65 and age <= 100:
    print("You are a senior citizen")
else:
    print("unable to read age")

print("\n------ example 4: and operator ------")
temperature = 90
humidity = 60
if 70 <= temperature <= 90 and humidity < 80:
    print("The weather is pleasant")
else:
    print("The weather is not ideal")

print("\n------ example 5: or operator ------")
day = "Monday"
is_holiday = True

if day=="Saturday" or day=="Sunday" or is_holiday:
    print("You can relax")
else:
    print("It is a weekday")

print("\n------ example 6: nested if statement ------")
number = int(input("Enter a number: "))
if number >= 0:
    if number == 0:
        print("The number is 0")
    else:   
        print(f"{number} is positive")
else:
    print(f"{number} is negative")

print("\n------ example 7: username validation ------")
# username validation. username must have 3+ characters without whitespace
username = input("Enter a username: ")
username = username.strip()
len_username = len(username)
if len_username >= 3:
    index_whitespace = username.find(" ") # use .find method to check for whitespace
    if index_whitespace == -1:
        print(f"{username} is 3+ characters.")
    else:
        print("Username cannot have spaces")
else:
    print(f"{username} is invalid. Username must have 3+ characters.")

print("\n------ example 8: match case statement ------")
response_code = 404
match response_code:
    case 400:
        print(f"Code = {response_code}. Server CANNOT understand.")
    case 401 | 403:
        print(f"Code = {response_code}. Server refused to send back.")
    case 404:
        print(f"Code = {response_code}. Server cannot find.")
    case _:
        print("Code is invalid.")
# the match case written as an if-elif-else statement
if response_code == 400:
    print(f"Code = {response_code}. Server CANNOT understand.")
elif response_code == 401 or response_code == 403:
    print(f"Code = {response_code}. Server refused to send back.")
elif response_code == 404:
    print(f"Code = {response_code}. Server cannot find.")
else:
    print("Code is invalid.")

# Create Py code calculating ave of 2 grades and return GPA according to the ave.
# Average 90 and 100, GPA = A
# Average 89.99 and 70, GPA = B 
# Average 69.99 and 60, GPA = C 
# Average 59.99 and 0, GPA = FAIL! 
# Any other average = UNDEFINED! 

grade1 = float(input("Enter first grade with two decimal pts: "))
grade2 = float(input("Enter second grade with two decimal pts: "))
ave = float((grade1+grade2)/2)
if ave >= 90 and ave <= 100:
    print(f"For the average of {ave}, your GPA is A")
elif ave >= 80 and ave <= 89.99:
    print(f"For the average of {ave}, your GPA is B")
elif ave >= 70 and ave <= 79.99:
    print(f"For the average of {ave}, your GPA is C")   
elif ave >= 60 and ave <= 69.99:
    print(f"For the average of {ave}, your GPA is D")
elif ave >= 0 and ave <= 59.99:
    print(f"For the average of {ave}, your GPA is F")
else:
    print("UNDEFINED")
