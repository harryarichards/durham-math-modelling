# BAD: Loop over all values of the variable i, and sum the squares, then
# take a square root.
res=0
for i in [4,2,6,8,3]:
    res += i*i
res=math.sqrt(res)

# GOOD: We need the length of our 5d vector.
norm=0
for component in [4,2,6,8,3]:
    norm += component*component
norm=math.sqrt(norm)
