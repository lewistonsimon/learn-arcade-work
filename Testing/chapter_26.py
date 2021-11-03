# Chapter 26

# Import functions into 'my_functions' namespace
# import my_functions # if you use this you have to put my_functions.

# Import function into LOCAL namespace
from my_functions import foo # you can use import * and that will import everything


def main():
    foo()


main()
