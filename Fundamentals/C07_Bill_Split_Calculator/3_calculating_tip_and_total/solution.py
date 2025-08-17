print("Bill Split Calculator")

bill=float(input())
tip_percent=float(input())

tip=(tip_percent/100)*bill
total=tip+bill
print(total)