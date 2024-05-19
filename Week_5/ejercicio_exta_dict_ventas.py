tech_sales = [
    {
        "date": "11/01/24",
        "customer_email": "kevin@gmail.com",
        "items":  [
            {
                "name": "PS5",
                "upc": "ITEM-345",
                "unit_price": 450.50,
            },
            {
                "name": "PS controller",
                "upc": "ITEM-123",
                "unit_price": 30.50,
            },
            {
                "name": "HDMI Cable",
                "upc": "ITEM-767",
                "unit_price": 13.25,
            },
        ],       
    },
    {
        "date": "12/01/24",
        "customer_email": "alonso@hotmail.com",
        "items": [
            {
                "name": "The Last of Us game",
                "upc": "ITEM-868",
                "unit_price": 30.45,                
            },
            {
                "name": "GTA 6 game",
                "upc": "ITEM-977",
                "unit_price": 35.55,           
            },
            {
                "name": "God of War Ragnarok",
                "upc": "ITEM-432",
                "unit_price": 40.25,
            },
            ],
    },
    {
        "date": "13/01/2024",
        "customer_email": "walter@gmail.com",
        "items": [
            {
                "name": "Asus monitor",
                "upc": "ITEM-444",
                "unit_price": 250.75
            },
            {
                "name": "Acer monitor",
                "upc": "ITEM-545",
                "unit_price": 235.45
            },
            {
                "name": "HP monitor",
                "upc": "ITEM-231",
                "unit_price": 270.50,
            },
        ],
    },
    { 
        "date": "14/01/2024",
        "customer_email": "juan@microsoft.com",
        "items": [
            {
                "name": "logitech mouse",
                "upc": "ITEM-888",
                "unit_price": 105.25,
            },
            {
                "name": "logitech keyboard",
                "upc": "ITEM-919",
                "unit_price": 235.75,
            },
            {
                "name": "logitech camera",
                "upc": "ITEM-221",
                "unit_price": 170.25,
            },
        ],


    },
]

sales_totals ={} # Almacena el total de ventas

for sale in tech_sales: # Itera cada elemento de la lista de tech_sales

    for item in sale["items"]:# Itera sobre cada elemento de la lista de items

        upc = item["upc"] # se obtiene el código upc
        unit_price = item["unit_price"] # se obtiene el unit_price

        sales_totals[upc] = sales_totals.get(upc, 0) + unit_price

print ("Sales totals by UPC:")

for upc, total in sales_totals.items():
    print(f"{upc}: ₡{total:.2f}")  # imprime el upc y el total de ventas con formato (.2f) como un numero de punto flotante con 2 decimales