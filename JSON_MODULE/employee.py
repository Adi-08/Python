import json

# Python dictionary
employee = {
    "name": "Rahul",
    "age": 25,
    "department": "Data Analytics",
    "salary": 50000
}

# Open/create JSON file in write mode
with open("employee.json", "w") as f:

    # Convert Python dictionary into JSON
    json.dump(employee, f, indent=4)

print("Employee data saved successfully!")



