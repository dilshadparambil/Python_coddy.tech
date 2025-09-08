# Get input for rows and columns
rows = int(input())
cols = int(input())

# Write your nested loops here
# Outer loop for rows
# Inner loop for columns
for i in range(rows):
    star=""
    for j in range(cols):
        star+='*'
    print(star)