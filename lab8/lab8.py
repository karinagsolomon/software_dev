"""
Karina Solomon
April 20, introduction Python
"""
# Single comment. This line WILL NOT run
print('\n------ Example 1: string characters ------')
print("\tGood morning! \nThis is my first \"Python\" code!")
print('\n------ Example 2: data type ------')
print(f"Data type of 3.56 = {type(3.56)}")
print(f"Data type of -25 = {type(-25)}")
print(f"Data type of 'Hello world!' = {type('Hello world!')}")
print(f"Data type of character '$' = {type('$')}")
print(f"Data type of False = {type(False)}")

print('\n------ Example 3: variables ------')
# declare variables
number1 = 25
number2 = -12
username = "Karina Solomon"
add_numbers = number1 + number2
is_raining = True
# prompt results
print(f"{username}, the sum of {number1} and {number2} is {add_numbers}")
print(f"Is it raining today? = {is_raining}")

print('\n------ Example 4: assigning values to multiple variables ------')
# declare multiple variables
item1, item2, item3 = "apples", 25, False
print(f"item 1 = {item1}, item 2 = {item2}, item 3 = {item3}")
# declare multiple variables with the same value
score1 = score2 = score3 = 88
print(f"score 1 = {score1}, score 2 = {score2}, score 3 = {score3}")

print('\n------ Example 5: input command ------')
print("Enter username: ")
username = input()
print(f"Collected username: {username}")

# Cast from string to integer
luckynumber = int(input("Enter a lucky number: "))
print(f"Lucky number: {luckynumber}")

# double the lucky number. Cast from string integer
doublelucky = int(luckynumber)*2
print(f"Print double the lucky number: {doublelucky}")

# Cast from int (or float) to string
triplelucky = str(doublelucky) * 3
print(f"Triple the casted number: {triplelucky}")

# Cast integer to bool value
completed_task = -20
print(f"completed task: {bool(completed_task)}")

print('\n------ Example 6: arithmetic operations ------')
num1 = 9
num2 = 2
print(f"The sum of num1 and num2 are                    {num1+num2}")
print(f"The difference between num 1 and num2 is        {num1-num2}")
print(f"The product of num1 and num2 is                 {num1*num2}")
print(f"The quotient of num1 and num2 is                {num1/num2}")
print(f"The modulus (remainder) of num1 and num2 is     {num1%num2}")
print(f"The integer of quotient of num1 and num2 is     {num1//num2}")
print(f"The result of base {num2} to the power of 3 is  {num2**3}")

print('\n------ Example 7: finding the hypotenuse ------')
# declare and assign values
x = float(input("Enter side 1: "))
y = float(input("Enter side 2: "))
# Calculate the hypotenuse
hyp = (x**2 + y**2)**.05
# prompt result
print(f"The hypotenuse of {x:0.2} and {y:0.3} is {hyp:0.3}")

print('\n------ Example 8: assignment operators ------')
n = 2
print(f"number =       {n}")
# assignment operator +
n += 3
print(f"number + 3 =   {n}")
# assignment operator -
n -= 1
print(f"updated - 1 =   {n}")
# assignment operator *
n *= 2
print(f"updated * 2 =   {n}")
# assignment operator /
n /= 2
print(f"updated / 2 = {n}")
# assignment operator //
n //= 2
print(f"updated // 2 = {n}")
# assignment operator ** (exponent)
n **= 2
print(f"updated ** 2 == {n}")
# modulus or remainder
n %= 2
print(f"updated % 2: {n}")

print('\n------ Example 9: comparison operators ------')
n1 = 10
n2 = 3
n3 = 7
compare1 = n1==n2
compare2 = n1==(n2+n3)
print(f"is n1 == n2? {compare1}")
print(f"is n1 = n2 + n3? {compare2}")
compare3 = n1>n2
compare4 = n2<=n3
print(f"is n1 > n2? {compare3}")
print(f"is n2 <= n3? {compare4}")

print('\n------ Example 10: string indexing ------')
# positive index
username = "peterpan123"
print(f"The fifth character = {username[4]}")

# negative index 
print(f"The fifth last character is {username[-5]}")

print('\n------ Example 11: string slice ------')
# slice from the beginning to the 4th character
print(f"Slice from beginning to the 4th character {username[:4]}")
# slice from the 7th character to the end
print(f"Slice from the 7th character to the end {username[6:]}")
# slice from the 3rd to the 8th character
print(f"Slice from 3rd to 8th character {username[2:8]}")
# slice from the 4th to 6th character using negative index
print(f"Slice from the 4th to 6th character using negative index {username[-8:-5]}")


print('\n------ Example 12: print length of string ------')
print(f"The username has {len(username)} characters.")