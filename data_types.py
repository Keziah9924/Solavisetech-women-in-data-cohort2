# Personal Bio Generator
name = "Keziah"
age = 20
height = 5.6
favorite_field = "Data Science"
is_student = True

print(f"My name is {name}. I am {age} years old.")
print(f"I love {favorite_field} and student status is {is_student}.")

# Type Checker
print(type(name))
print(type(age))
print(type(height))
print(type(is_student))

# Data Conversion
number = 10
print(str(number))

decimal = 5.9
print(int(decimal))

string_number = "25"
print(int(string_number))

# User Information
user_name = input("Enter your name: ")
user_age = input("Enter your age: ")
country = input("Enter your country: ")

print(f"Hello {user_name} from {country}. You are {user_age} years old.")

# Temperature Converter
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32

print(f"{celsius}°C is equal to {fahrenheit}°F")