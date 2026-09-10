import json

# Open the JSON file in read mode
with open("JSON_MODULE/student.json", "r") as f:

    # Convert JSON data into a Python dictionary
    data = json.load(f)

# Print complete data
print("Complete Student Data:")
print(data)

# Print student's name
print("Name:", data["name"])

# Print student's skills
print("Skills:", data["skills"])