from mongodb import operators

data = {
    "name": "Mahesh",
    "mobile": "9876543210",
    "status": "Pending"
}

operators.insert_one(data)

print("Operator Saved Successfully")