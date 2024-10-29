"""the skeleton of the python function is as follows
def function_name(parameters)
     ----the body or statement to be done
     return expression.
#functions reduce the coding time and can be reused.

--global variables are not defined inside a function  while local,varibales are defined inside a function.--
example lets create a function to check if a number is even or odd.
"""
def if_even_or_odd(x):# x is the number to be checked
    if x % 2 == 0:
        print("even")
    else:
        print("odd")
#we have to call th function to execute .
if_even_or_odd(int(input("enter a number")))

#the value of x is taken by 5 in the call statement. from the users input but we had to change it to int less it would be a string.