# Write a Python code to calculate Combination (15,3)
# formula of combination is  n! / (r! (n – r)!)
n = 15
r = 3

# for neuminator(n!)
i = 1
numenator = 1
while i <= n:
    numenator *= i
    i += 1

# for r factorial
j = 1
rfactorial = 1
while j <= r:
    rfactorial *= j
    j += 1

# for deuminator
deuminator = 1
k = 1
while k <= (n-r):  # for (n-r)!
    deuminator *= k
    k += 1

# for combination
deuminator = rfactorial*deuminator

# for result
print("combination is", int(numenator/deuminator))
