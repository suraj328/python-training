# Ask enter to enter two numbers (say, a and b). Generate two random numbers between those two numbers and find a combination of these two newly generated random numbers.
n =int(input("enter 1st integer:"))
r =int(input("enter 2nd integer:"))

#for random number
l=n
print(f"the random number between {n} and {r} are:")

while l<=r:
    print(l)
    l+=1
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
print("\n")
print("combination is",int(numenator/deuminator))
