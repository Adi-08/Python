import json


# ============================================================
# 1. PYTHON DICTIONARY → JSON FILE
#    json.dump()
# ============================================================

employee = {
    "name": "Rahul",
    "age": 25,
    "department": "Data Analytics",
    "salary": 50000
}

# Open/create JSON file in write mode
with open("employee.json", "w") as f:

    # Convert Python dictionary into JSON and save it to the file
    json.dump(employee, f, indent=4)

print("Employee data saved successfully!")


# ============================================================
# 2. JSON FILE → PYTHON DICTIONARY
#    json.load()
# ============================================================

# Open JSON file in read mode
with open("employee.json", "r") as f:

    # Convert JSON file data into Python dictionary
    data = json.load(f)

print("\n--- Employee Data ---")
print(data)

# Access individual values
print("Name:", data["name"])
print("Salary:", data["salary"])


# ============================================================
# 3. ADD NEW DATA
# ============================================================

# Add a new key-value pair
data["city"] = "Pune"

print("\n--- After Adding City ---")
print(data)


# ============================================================
# 4. UPDATE EXISTING DATA
# ============================================================

# Change the existing salary
data["salary"] = 60000

print("\n--- After Updating Salary ---")
print(data)


# ============================================================
# 5. DELETE DATA
# ============================================================

# Delete the city key
del data["city"]

print("\n--- After Deleting City ---")
print(data)


# ============================================================
# 6. SAVE UPDATED DATA INTO JSON FILE
# ============================================================

# Open JSON file in write mode
with open("employee.json", "w") as f:

    # Save the updated dictionary into JSON
    json.dump(data, f, indent=4)

print("\nUpdated employee data saved!")


# ============================================================
# 7. LOOP THROUGH JSON
#    keys(), values(), items()
# ============================================================

print("\n--- Keys ---")

# Print only keys
for key in data.keys():
    print(key)


print("\n--- Values ---")

# Print only values
for value in data.values():
    print(value)


print("\n--- Keys and Values ---")

# Print both key and value
for key, value in data.items():
    print(key, ":", value)


# ============================================================
# 8. LIST OF JSON OBJECTS
# ============================================================

employees = [
    {
        "name": "Rahul",
        "department": "IT",
        "salary": 50000
    },
    {
        "name": "Amit",
        "department": "HR",
        "salary": 45000
    },
    {
        "name": "Priya",
        "department": "Finance",
        "salary": 55000
    }
]

# Save list of employees into JSON file
with open("employees.json", "w") as f:

    # Convert Python list into JSON
    json.dump(employees, f, indent=4)

print("\nEmployees saved successfully!")


# Access first employee
print("\nFirst Employee:")
print(employees[0])

# Access first employee's name
print("Name:", employees[0]["name"])


# Loop through all employees
print("\n--- All Employees ---")

for employee in employees:
    print(employee["name"], "-", employee["department"])


# ============================================================
# 9. NESTED JSON
# ============================================================

customer = {
    "name": "Aditya",
    "age": 21,

    # Address is another dictionary inside the main dictionary
    "address": {
        "city": "Pune",
        "state": "Maharashtra",
        "country": "India"
    }
}

print("\n--- Nested JSON ---")
print(customer)

# Access nested data
print("City:", customer["address"]["city"])
print("State:", customer["address"]["state"])


# ============================================================
# 10. JSON STRING → PYTHON
#     json.loads()
# ============================================================

# JSON data received as a string
json_text = '{"name": "Aditya", "age": 21, "city": "Pune"}'

# Convert JSON string into Python dictionary
python_data = json.loads(json_text)

print("\n--- JSON String → Python ---")
print(python_data)

print("Name:", python_data["name"])


# ============================================================
# 11. PYTHON → JSON STRING
#     json.dumps()
# ============================================================

# Convert Python dictionary into JSON string
json_string = json.dumps(python_data, indent=4)

print("\n--- Python → JSON String ---")
print(json_string)


# ============================================================
# 12. PANDAS + JSON
#     pd.read_json()
# ============================================================

import pandas as pd

# Read JSON file directly into a Pandas DataFrame
df = pd.read_json("employees.json")

print("\n--- Pandas DataFrame ---")
print(df)


# ============================================================
# 13. JSON → PANDAS DATAFRAME
#     json_normalize()
# ============================================================

# Nested JSON data
orders = [
    {
        "order_id": 101,
        "customer": {
            "name": "Aditya",
            "city": "Pune"
        },
        "amount": 2000
    },

    {
        "order_id": 102,
        "customer": {
            "name": "Rahul",
            "city": "Mumbai"
        },
        "amount": 3000
    }
]

# Convert nested JSON into a flat DataFrame
flat_df = pd.json_normalize(orders)

print("\n--- Flattened JSON ---")
print(flat_df)


# ============================================================
# 14. JSON FROM API
# ============================================================

import requests

# API URL
url = "https://jsonplaceholder.typicode.com/users"

# Send request to API
response = requests.get(url)

# Convert API response JSON into Python data
api_data = response.json()

print("\n--- API JSON Data ---")

# Print first user
print(api_data[0])