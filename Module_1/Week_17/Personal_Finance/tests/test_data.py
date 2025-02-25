import os
import data

def test_save_and_load_data():
    # Create sample data
    test_data = {
        "categories": ["Food", "Transport"],
        "transactions": [
            {"type": "expense", "title": "Lunch", "amount": 10, "category": "Food"}
        ]
    }

    # Save the data
    data.save_data(test_data)

    # Load the data back
    loaded_data = data.load_data()

    # Check if saved and loaded data match
    assert loaded_data == test_data

    # Clean up (delete the file after test)
    if os.path.exists("data.json"):
        os.remove("data.json")