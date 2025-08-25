text = input()
# Write your code below
p_count=0
for char in text.lower():
    if char=='p':
        p_count+=1
print(p_count)