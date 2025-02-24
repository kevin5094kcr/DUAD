import PySimpleGUI as sg
import data

def add_category():
    loaded_data = data.load_data()
    new_category = sg.popup_get_text("Enter category name:")


    if new_category and new_category not in loaded_data["categories"]:
        loaded_data["categories"].append(new_category)
        data.save_data(loaded_data)
        sg.popup("Category saved!")