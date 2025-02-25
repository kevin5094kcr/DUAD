import json

def load_data():
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            print("Loaded data:", data)  
            return data
        
    except FileNotFoundError:
        print("No data file found, creating new file.")  
        initial_data = {"categories": [], "transactions": []}
        save_data(initial_data)
        return initial_data
    

def save_data(finance_data):
    with open("data.json", "w") as file:
        json.dump(finance_data, file, indent=4)
    print("Data saved successfully!")  