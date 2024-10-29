"""
def get_user_info(*args, **kwargs):
    for arg in args:
        print(f'Hello, {arg}')

    for key, value in kwargs.items():
        print(f'{key} is {value} years old.')


# User input
name = input("Enter your name: ")
age = input("Enter your age: ")

get_user_info(name, age=age)
"""

#function to take user input and print the name of cars.
def print_car(*args, **kwargs):
    for arg in args:
        print(f'Hello, {arg}')
    for key, value in kwargs.items():
        print(f'{key} is {value} best model')


#user input
car_name = input("Enter your car name: ")
model_year=input("Enter your model year: ")

#call the function with the parameters
print_car(car_name,model_year=model_year)