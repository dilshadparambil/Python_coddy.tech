def handle_shopping_cart(orders):
    # Create an empty dictionary for the shopping cart
    cart={}
    # Process each order in the list
    for order in orders:
        try:
            # Split the order and add to cart
            item=order.split(':')[0]
            quantity=int(order.split(':')[1])
            if quantity<0:
                print(f"Negative quantity not allowed: {order}")
            
            elif item in cart:
                cart[item]+=quantity
            else:
                cart[item]=quantity
            # Handle potential errors
            
        except ValueError:
            # Handle value errors
            print(f"Invalid quantity: {order}")

        except Exception as e:
            # Handle unexpected errors
            print(f"Invalid format: {order}")
    # Return the completed car
    return cart

print(handle_shopping_cart(["cereal:1","cereal:3","orange:5","butter:2"]))