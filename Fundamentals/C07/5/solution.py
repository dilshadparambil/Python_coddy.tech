print("Bill Split Calculator")

bill=float(input())
tip_percent=float(input())

tip=(tip_percent/100)*bill
total=tip+bill
print(f"Total (including tip): ${total}")

people_count=int(input())
split=total/people_count
print(f"Each person pays: ${split}")