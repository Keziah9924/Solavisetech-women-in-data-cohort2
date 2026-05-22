# Age Eligibility Checker
age = int(input("Enter your age: "))

if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
else:
    print("Adult")

# Password Validator
password = input("Enter password: ")

if len(password) >= 8:
    print("Strong password")
else:
    print("Weak password")

# Grade Classification
score = int(input("Enter your score: "))

if score >= 80:
    print("Grade A")
elif score >= 70:
    print("Grade B")
elif score >= 60:
    print("Grade C")
else:
    print("Fail")

# Multiplication Table
number = int(input("Enter a number: "))

for i in range(1, 13):
    print(f"{number} x {i} = {number * i}")

# Number Guessing Game
secret = 7
guess = 0

while guess != secret:
    guess = int(input("Guess the number: "))

print("Correct!")

# Countdown Timer
for i in range(10, 0, -1):
    print(i)

# ATM Withdrawal Simulation
balance = 1000
withdraw = float(input("Enter withdrawal amount: "))

if withdraw <= balance:
    print("Withdrawal successful")
else:
    print("Insufficient balance")

# Login System
username = "admin"
password = "1234"

user = input("Username: ")
passcode = input("Password: ")

if user == username and passcode == password:
    print("Login successful")
else:
    print("Invalid credentials")