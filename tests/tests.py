def calculate_total(products, offer):
    total = 0
    for product in products:
        total += product["price"]
    
    for item in offer:
        item["price"] -= 2
    
    return total, item

def test_calculate_total_with_empty_list():
    assert calculate_total([]) == 0

def test_calculate_total_with_single_product():
    products = [
        {
            "name" : "Notebook",
            "price" : 5
        }
    ]
    offer = [
        {
            "name" : "pescado",
            "price" : "4"
        },
        {
            "name" : "pescado",
            "price" : "10"
        },  
    ]
    assert calculate_total(products) == 5

def test_calculate_total_with_multiple_product():
    products = [
        {
            "name" : "Book",
            "price" : 10
        },
         {
            "name" : "Pen",
            "price" : 2
        }
    ]
    assert calculate_total(products) == 5


if __name__ == "__main__":
    test_calculate_total_with_empty_list()
    test_calculate_total_with_single_product()
    test_calculate_total_with_multiple_product()