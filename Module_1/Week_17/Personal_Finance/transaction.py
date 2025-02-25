import PySimpleGUI as sg
import data


def add_transaction(transaction_type):
    finance_data = data.load_data()
    categories = finance_data.get("categories", [])

    layout = [
        [sg.Text("Title"), sg.InputText(key="-TITLE-")],
        [sg.Text("Amount"), sg.InputText(key="-AMOUNT-")],
        [sg.Text("Category"), sg.Combo(categories, key="-CATEGORY-")],
        [sg.Button("Save"), sg.Button("Cancel")]
    ]

    window= sg.Window("Add Transaction", layout)
    event, values =  window.read()

    if event == "Save" and values["-TITLE-"] and values["-AMOUNT-"].isdigit() and values["-CATEGORY-"]:
        finance_data.setdefault("transactions", []).append({
            "type": transaction_type,
            "title": values["-TITLE-"],
            "amount": int(values["-AMOUNT-"]),
            "category": values["-CATEGORY-"]
        })
        data.save_data(finance_data)
        sg.popup("Transaction saved")

    window.close()



