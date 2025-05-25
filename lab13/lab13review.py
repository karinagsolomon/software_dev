"""
Karina Solomon
May 4, 2025, Python classes
"""
class Person:
    def __init__(self, name, age):
        
        self.username = name
        self.user_age = age

    def __str__(self):
        return f"Person: {self.username}\n Age: {self.user_age}"
    
    # method
    def intro(self):
        return f"Hello, I am {self.username}!"
    
print("\n-----Example 1-----")
# Create an object of the Person class
user1 = Person("Karina", 21)
print(user1.intro())

# Example 2 private properties
class Chair:
    # method declaring variables
    def __init__(self, height, width, length):
        self.chairheight = height
        self.__width = width # 2 underscores makes property width to be very private
        self.chairlength = length * 2

    # method to pass length
    def pass_length(self):
        return self.chairlength
    
    # method to pass volume
    def pass_volume(self):
        return self.chairheight * self.__width * self.chairlength
    
    # method to pass color
    def chair_color(self): 
        return "mahogany"
    
    # method to return volume of the chair
    def get_volume(self):
        return self.pass_volume()

    # method to return the color of the chair
    def get_color(self):
        return self.chair_color()

    # method to return the description of the chair
    def get_description(self):
        return f"The total volume of the chair is {self.get_volume()}. The chair color is {self.get_color()}."
    
    # method with a private property
    def set_price(self, price):
        self._chairprice = price # 1 underscore makes property chairprice to be private

# create an object
userchair1 = Chair(5, 10, 15)
print(f"The chair length is {userchair1.chairlength}.")
print(f"The chair width is {userchair1._Chair__width}.")

# call method pass_length
print(f"The chair has length {userchair1.pass_length()}.")
print(f"The chair has volume {userchair1.pass_volume()}.")
print(f"{userchair1.get_description()}")

# call private method
userchair1.set_price(25)
print(f"The price of the chair is {userchair1._chairprice}.")