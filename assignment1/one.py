# Write a Python code to calculate Permutation (5,3)
# formula=n!/(n-r)!
n = 5
r = 3


# for neuminator(n!)
i = 1
numenator = 1
while i <= n:
    numenator *= i
    i += 1


# for deuminator
deuminator = 1
j = 1
while j <= (n-r):  # for (n-r)!
    deuminator *= j
    j += 1

# reslut of permutation
print("permutation is", int(numenator/deuminator))
