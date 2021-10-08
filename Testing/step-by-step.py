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


my_list = []
user_input = input()
my_list.append(user_input)
print(my_list)
