def find_occurrences(text, pattern):
    # Write your code here
    positions=[]
    if pattern in text:
        
        start=0
        while True:
            start=text.find(pattern,start)
            if start==-1:
                break
            positions.append(start)
            start+=1    

        return(True,len(positions),positions)
    return(False, len(positions), positions)

# Read input
text = input()
pattern = input()

# Call your function and print the result
result = find_occurrences(text, pattern)
print(result)