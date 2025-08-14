# Initialize variables
is_sunny=True
temperature=25
wind_speed=10
water_temperature=22

# Calculate conditions
can_go_hiking = is_sunny and temperature>15 and wind_speed<20
can_go_swimming = is_sunny and temperature>20 and water_temperature>18
cannot_go_outside = not is_sunny or temperature<10 or wind_speed>30

# Don't delete the lines below
print("Can go hiking:", can_go_hiking)
print("Can go swimming:", can_go_swimming)
print("Cannot go outside:", cannot_go_outside)
