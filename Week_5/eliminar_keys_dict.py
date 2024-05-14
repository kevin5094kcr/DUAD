list_of_keys = ['access_level', 'age']
employee = {'name': 'Kevin', 'email': 'kevin@gmail.com', 'access_level': 8, 'age': 29}

for key in list_of_keys:
    deleted_item = employee.pop(key)

print(employee)