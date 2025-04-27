"""
Karina Solomon
April 25, 2025
"""
print("\n------ Ex 1: for loop as a counter ------")
# print from 0 to 4
for x in range(0,4): # declare variable x then range starting at 0, and final value printed is second to last value
    print(f"Hello, x = {x}")

print("\n------ Ex 2: for loop in a list ------")
fruits = ["coconut", "apple", "grapes", "pineapple", "mango"] # create array
for fruit_index in range(0,len(fruits)): # create variable for index
    print(f"The {fruits[fruit_index]} is in aisle {fruit_index}") # pass var for index in array

# alternative way to print a for loop
for each_fruit in fruits: # create var for each obj in array
    print(f"{each_fruit}") # prints each object

print("\n------ Ex 3: for loop with different incerement ------")
# for loop to print 2 to 30 with an increment of 3
for num in range(2,30,3):
    print(num)

print("\n------ Ex 4: for loop with different decerement ------")
# for loop to print 10 to 0 with an decrement of -2
for num in range(10,0,-2):
    print(num)

print("\n------ Ex 5: for loop through a string ------")
username = "yes123"
for username_character in username:
    print(username_character)

print("\n------ Ex 6: nested conditional statement ------")
numbers = [-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9]
negative_counter = 0 # create var that counts neg values, start at 0
for each_number in numbers: # create var for indexes in range
    if each_number < 0: # checks if value is neg
        negative_counter += 1 # adds 1 for every neg value in numbers array

# print the result
print(f"There are {negative_counter} negative values.")

print("\n------ Ex 7: nested conditional statement, operation ------")
# for loop to add all odd numbers
sum_odd = 0
for each_number in numbers:
    if each_number %2 == 1: # %2==1 indicates an odd number
        sum_odd += each_number

print(f"The sum of all odd numbers is {sum_odd}")

print("\n------ Ex 8: break statement in a loop ------")
# for loop to print from 0 to 10 (exclusive), and terminate the loop when it reaches to a given number
for n in range(0,10):
    if n == 5:
        print(f"counter reaches to {n}")
        break
    else:
        print(n)
    
print("\n------ Ex 9: continue statement in a loop ------")
# for loop to add numbers from 0 to 10 (exclusive), except number 5
sumall = 0
for n in range(10):
    if n == 5:
        print("skip 5")
        continue # skips an iteration
    sumall += n
    print(n)
    print(f"\t{sumall}")

print("\n------ Ex 10: else statement in a for loop ------")
for n in range(6):
    if n == 3:
        break # stops the iteration
    print(n) 
else:
    print("loop completed")

print("\n------ Ex 11: while loop as a counter ------")
# while loop to print from 0 to 5
n = 0
while n < 6:
    n += 1
    print(n)

print("\n------ Ex 12: while loop as a checkpoint ------")
# while loop to collect and add numbers between -5 and 5
# if user enters number not in range, while loop should terminate
sumusernumber = 0
while(True):
    number = int(input("Enter a number between -5 and 5: "))
    if number < -5 or number > 5: # excludes numbers not in range
        break
    sumusernumber += number
print(f"The total is {sumusernumber}")

print("\n------ Ex 13: while loop as counting operator ------")
# while loop to count the even numbers in the list
numbers = [2, 0, -5, 1, 8, -6, 7, -3]
index = 0 # initiate index of array
len_numbers = len(numbers) # recognizes length of array
eventcount = 0 # counts even numbers in array
while index < len(numbers):
    if numbers[index] %2 == 0 and numbers[index] != 0: # checks if an even number
        eventcount +=1 
    index += 1
else:
    print(f"This is/are {eventcount} even numbers")

"""
Given the following list:
colors = ['red', 'orange', 'olive', 'magenta', 'green']
complete the code by writing a Python program that:
Takes a color input from the user using the keyboard.
Strips any leading/trailing whitespace from the input.
Converts the input to lowercase.
Uses a for loop and a nested conditional statement to check whether the entered color is in the list colors.
Uses a flag to indicate when the color is found, and breaks the loop once a match is found.
Prints a message depending on whether the color was found in the list.
If the color is found:
_____ color is in the list
If the color is not found:
_____ color IS NOT in the list
Note: Replace the blank with the entered color.
"""
colors = ['red','orange','olive','magenta','green']
user_color = str(input("Enter a color: "))
user_color = user_color.strip().lower()
for each_color in colors:
    if each_color == user_color:
        print(f"{user_color} is in the list")
        break
else:
    print(f"{user_color} IS NOT in the list")