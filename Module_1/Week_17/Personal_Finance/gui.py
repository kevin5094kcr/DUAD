import PySimpleGUI as sg
import category
import transaction
import data

def format_data_for_table(transactions):
        return[[t["type"], t["title"], t["amount"], t["category"]] for t in transactions]


def show_main_window():
    
    finance_data = data.load_data()
    
    layout = [
        [sg.Text("Finance Manager", font=("Arial", 16))],
        [sg.Button("Add Category"), sg.Button("Add Expense"), sg.Button("Add Income")],
        [sg.Table(
            values=format_data_for_table(finance_data["transactions"]),
            headings=["Type", "Title", "Amount", "Category"],
            key="-TABLE-",
            auto_size_columns=False,
            justification="center"
        )],
        [sg.Button("Exit")]
    ]


    window = sg.Window("Finance Manager", layout)

    while True:
        event, _ = window.read()

        if event == "Exit":
            break
        elif event == "Add Category":
            category.add_category()
        elif event == "Add Expense":
            transaction.add_transaction("expense")
        elif event == "Add Income":
            transaction.add_transaction("income")

    finance_data = data.load_data()
    window.close()
