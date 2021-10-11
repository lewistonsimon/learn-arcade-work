# Becomes difficult to use with tons of stuff
# name = "Link"
# outfit = "Green"
# max_hit_points = 50
# current_hit_points = 50
# armor_amount = 6
# max_speed = 10
#
# def display_character(name, outfit, max_hit_points, current_hit_points, armor, max_speed):
#     print(name, outfit, max_hit_points, current_hit_points)

# object is an instant of a class
# class Character:
#     """
#     This is a video game character
#     """
#     # a method is a function that is in a class
#     def __init__(self):
#         """ Create my character """
#         self.name = ""
#         self.outfit = ""
#         self.max_hit_points = 0
#         self.current_hit_points = 0
#         self.armor_amount = 0
#         self.max_speed = 0

# class Address:
#     """ Hold all the fields for a mailing address. """
#     def __init__(self):
#         """ Set up the address fields. """
#         self.name = ""
#         self.line1 = ""
#         self.line2 = ""
#         self.city = ""
#         self.state = ""
#         self.zip = ""
#
#     def main():
#         home_address = Address()
#         home_address.name = "John Smith"
#         home_address.line1 - "701 N. C Street"
#         home_address.line2 = "Carver Science Building"
#         home_address.city = "Indianola"
#         home_address.state = "IA"
#         home_address.zip = "50125"
#
#         # Create another address
#         vacation_home_address = Address()
#
#         # Set the fields in the address
#         vacation_home_address.name = "John Smith"
#         vacation_home_address.line1 = "1122 Main Street"
#         vacation_home_address.line2 = ""
#         vacation_home_address.city = "Panama City Beach"
#         vacation_home_address.state = "FL"
#         vacation_home_address.zip = "32407"
#
#         print(vacation_home_address.name)
#
#     def print_address(address):
#         """ Print an address to the screen """
#
#         print(address.name)
#         # If there is a line1 in the address, print it
#         if len(address.line1) > 0:
#             print(address.line1)
#         # If there is a line2 in the address, print it
#         if len(address.line2) > 0:
#             print(address.line2)
#         print(address.city + ", " + address.state + " " + address.zip)
#
#     def main():
#         # ... code for creating home_address and vacation_home_address
#         # goes here.
#         print_address(home_address)
#         print()
#         print_address(vacation_home_address)
#
#     main()


# class Dog():
#     def __init__(self, name):
#         """ Constructor """
#
#         self.name = name
#         print("A dog has been born!")
#
#
# def main():
#     # This creates the dog
#     my_dog = Dog("Spot")
#     print(f"The dog's name is: {my_dog.name}")
#
#     my_other_dog = Dog("Sam")
#     print(f"The dog's name is: {my_other_dog.name}")
#
#
# main()

# class Address():
#     def __init__(self, line1, line2, city, state, zip, country):
#         self.line1 = line1
#         self.line2 = line2
#         self.city = city
#         self.state = state
#         self.zip = zip
#         self.country = country
#
#
# def main():
#     # This creates the address
#     my_address = Address("701 N. C Street",
#                          "Carver Science Building",
#                          "Indianola",
#                          "IA",
#                          "50125",
#                           "USA")
#
#
# main()

# class Person:
#     def __init__(self):
#
#         self.name: str = "A"
#
#
#
#
# mary = Person()
# # mary.name = 22
#
# class Address:
#     def __init__(self,
#                  name: str = "",
#                  line1: str = "",
#                  line2: str = "",
#                  city: str = "",
#                  state: str = "",
#                  zip_code: str = ""
#                  ):
#         self.name: str = name
#         self.line1: str = line1
#         self.line2: str = line2
#         self.city: str = city
#         self.state: str = state
#         self.zip_code: str = zip_code
#
# # this code does exact same thing as the stuff above
# @dataclass  # much cleaner code @ is a decerator
# class Address:
#     name: str = ""
#     line1: str = ""
#     line2: str = ""
#     city: str = ""
#     state: str = ""
#     zip_code: str = ""


# my_list = []
# user_input = input()
# my_list.append(user_input)
# print(my_list)





# class Cat:
#     population
#
#     def __init__(self, name):
#         self.name = name
#         Cat.population +=
#
# def main():
#     cat1 = Cat("Pat")
#     cat2 = Cat("Pepper")
#     cat3 = Cat("Pouncy")
#
#     print("The cat population is", Cat.population)
#
# main()



# Chapter 17
# Class Methods

# class Dog:
#     def __init__(self):
#         self.age = 0
#         self.name = ""
#         self.weight = 0
#
#     # a function in a class is called a method
#     def bark(self):
#         if self.weight < 10:
#             print("Yip! says", self.name)
#         else:
#             print("woof says", self.name)
#
# def main():
#     my_dog = Dog()
#     my_dog.name = "spot"
#     my_dog.weight = 9
#     my_dog.age = 3
#     my_dog.bark()
#
#     my_other_dog = Dog()
#     my_other_dog.name = "Fluffy"
#     my_other_dog.weight = 20
#     my_other_dog.age = 3
#     my_other_dog.bark()
#
# main()

# 17.1.1
# References
# class Person():
#     def __init__(self):
#         self.name = ""
#         self.money = 0
#
#
# def main(): # bob and nancy are just pointers
#     bob = Person()
#     bob.name = "Bob"
#     bob.money = 100
#
#     nancy = Person()
#     nancy.name = "Nancy"
#
#     print(bob.name, "has", bob.money, "dollars.")
#     print(nancy.name, "has", nancy.money, "dollars.")
#
#
# main()


# class Person():
#     def __init__(self):
#         self.name = ""
#         self.money = 0
#
#
# def main(): # bob and nancy are just pointers
#     bob = Person()
#     bob.name = "Bob"
#     bob.money = 100
#
#     nancy = bob
#     nancy.name = "Nancy"
#
#     print(bob.name, "has", bob.money, "dollars.")
#     print(nancy.name, "has", nancy.money, "dollars.")
#
#
# main()


# def give_money1(person):
#     person.money += 100
#
#
# class Person():
#     def __init__(self):
#         self.name = ""
#         self.money = 0
#
#
# def main():
#     bob = Person()
#     bob.name = "Bob"
#     bob.money = 100
#
#     give_money1(bob)
#     print(bob.money)
#
# main()

# Wrong
# class Dog():
#     def __init__(self):
#         self.age = 0
#         self.name = ""
#         self.weight = 0
#
#     def __init__(self): # it will ignore the first def __init__(self): and only do the second
#         print("New dog!")
#
# # Correct:
# class Dog():
#     def __init__(self):
#         self.age = 0
#         self.name = ""
#         self.weight = 0
#         print("New dog!")


# class Boat():
#     def __init__(self):
#         self.tonnage = 0
#         self.name = ""
#         self.is_docked = True
#
#     def dock(self):
#         if self.is_docked:
#             print("You are already docked.")
#         else:
#             self.is_docked = True
#             print("Docking")
#
#     def undock(self):
#         if not self.is_docked:
#             print("You aren't docked.")
#         else:
#             self.is_docked = False
#             print("Undocking")
#
# class Submarine(Boat): # a child class will get everything that the parent class
#     def submerge(self):
#         print("Submerge!")


# class Person():
#     def __init__(self):
#         self.name = ""
#
# class Employee(Person):
#     def __init__(self):
#         # Call the parent/super class constructor first
#         super().__init__()
#
#         # Now set up our variables
#         self.job_title = ""
#
# class Customer(Person):
#     def __init__(self):
#         super().__init__()
#         self.email = ""
#
# def main():
#     john_smith = Person()
#     john_smith.name = "John Smith"
#
#     jane_employee = Employee()
#     jane_employee.name = "Jane Employee"
#     jane_employee.job_title = "Web Developer"
#
#     bob_customer = Customer()
#     bob_customer.name = "Bob Customer"
#     bob_customer.email = "send_me@spam.com"
#
# main()


"""

Is-A
Has-A



"""