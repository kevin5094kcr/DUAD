import PySimpleGUI as sg
import data

def manage_categories():
    loaded_data = data.load_data()
    categories = loaded_data.get("categories", [])

    layout = [
        [sg.Text("Existing Categories")],
        [sg.Listbox(values=categories, size=(30, 6), key="-CATEGORY_LIST-")],
        [sg.Text("New Category"), sg.InputText(key="-NEW_CATEGORY-")],
        [sg.Button("Add"), sg.Button("Close")]
    ]

    window = sg.Window("Category Management", layout)

    while True:
        event, values = window.read()
        if event in ("Close", sg.WIN_CLOSED):
            break
        elif event == "Add":
            new_category = values["-NEW_CATEGORY-"]
            if new_category and new_category not in categories:
                categories.append(new_category)
                loaded_data["categories"] = categories
                data.save_data(loaded_data)
                window["-CATEGORY_LIST-"].update(values=categories)

    window.close()

# def add_category():
#     loaded_data = data.load_data()
#     new_category = sg.popup_get_text("Enter category name:")


#     if new_category and new_category not in loaded_data["categories"]:
#         loaded_data["categories"].append(new_category)
#         data.save_data(loaded_data)
#         sg.popup("Category saved!")