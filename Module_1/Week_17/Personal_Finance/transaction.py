import PySimpleGUI as sg
import data

def add_transaction(transaction_type):
    finance_data = data.load_data()

    if not finance_data["categories"]:
        sg.popup_error("Please add a category before continuing.")
        return

    title = sg.popup_get_text("Enter transaction title:")
    amount = sg.popup_get_text("Enter transaction amount:")
    category = sg.popup_get_text("Enter transaction category:")

    if title and amount.isdigit() and category:
        finance_data["transactions"].append({
            "type": transaction_type,
            "title": title,
            "amount": int(amount),
            "category": category
        })
        data.save_data(finance_data)
        sg.popup("Transaction saved!") 
