def calculate_discount(price, discount_percentage):
    # Write code here
    discount=price*(discount_percentage/100)
    new_price=round(price-discount,2)
    return new_price

print(calculate_discount(75.5,10))