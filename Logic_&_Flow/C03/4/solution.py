def print_employee_details(employee_data):
    # Write code here
    if employee_data:
        for key, value in employee_data.items():
            print(f'{key}: {value}')
    else:
        print('No data available')
