text = input()
# Write your code below
s_count=0
for char in text.lower():
    if char=='s':
        s_count+=1
print(s_count)