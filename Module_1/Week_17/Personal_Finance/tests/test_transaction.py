import transaction

def test_add_transaction():
    transactions = []
    
    transaction.add_transaction(transactions, "expense", "Coffee", 5, "Food")
    
    assert len(transactions) == 1
    assert transactions[0]["title"] == "Coffee"
    assert transactions[0]["amount"] == 5
    assert transactions[0]["category"] == "Food"