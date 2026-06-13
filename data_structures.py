# Favorite Tools List
tools = ["Python", "VS Code", "Git"]

tools.append("GitHub")
tools.remove("Git")

print(tools)

# Student Scores
scores = [70, 85, 90, 60, 100]

print("Highest:", max(scores))
print("Lowest:", min(scores))
print("Average:", sum(scores)/len(scores))

# Shopping List Manager
shopping = []

shopping.append("Rice")
shopping.append("Milk")
shopping.append("Bread")

print(shopping)

# Country Capitals
countries = (
    ("Ghana", "Accra"),
    ("Nigeria", "Abuja"),
    ("Kenya", "Nairobi")
)

print(countries)

# Unique Visitors
visitors = ["Ama", "Kofi", "Ama", "Yaw"]

unique_visitors = set(visitors)

print(unique_visitors)

# Common Skills
person1 = {"Python", "HTML", "CSS"}
person2 = {"Python", "JavaScript", "CSS"}

print(person1.intersection(person2))

# Student Record
student = {
    "name": "Keziah",
    "age": 20,
    "course": "Data Science"
}

print(student)

# Mini Contact Book
contacts = {
    "Ama": "0240000000",
    "Yaw": "0550000000"
}

search = input("Enter contact name: ")

if search in contacts:
    print(contacts[search])
else:
    print("Contact not found")