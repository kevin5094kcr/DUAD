import category

def test_add_category():
    categories = []
    category.add_category(categories, "Entertainment")
    
    assert "Entertainment" in categories