def print_product_details(product_data):
    # Write code here
    if product_data:
        for key, value in product_data.items():
            print(f'{key.title()}: {value}')
    else:
        print('No product information available')
