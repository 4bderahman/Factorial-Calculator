# intering the number
n = int(input("Enter a number: "))

fact = 1

# Loop to calculate the factorial
for i in range(1, n + 1):
    fact *= i

# the result
print(n,"! =",fact)
