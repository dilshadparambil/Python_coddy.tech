# Read input for the three matches
match1 = eval(input())
match2 = eval(input())
match3 = eval(input())

# 1. Find players who participated in all three matches
q1=match1&match2&match3
# 2. Find players who participated in exactly two matches
a=match1.intersection(match2)-match3
b=match1.intersection(match3)-match2
c=match2.intersection(match3)-match1
q2=a|b|c
# 3. Find players who participated in only one match
q3=(match1-match2-match3)|(match2-match1-match3)|(match3-match1-match2)
# 4. Count total unique players
q4=len(match1|match2|match3)
# 5. Find players in Match 1 only
q5=match1-match2-match3
# Print results in the specified format
print(f"Players in all matches: {sorted(list(q1))}")
print(f"Players in exactly two matches: {sorted(list(q2))}")
print(f"Players in only one match: {sorted(list(q3))}")
print(f"Total unique players: {q4}")
print(f"Players in Match 1 only: {sorted(list(q5))}")