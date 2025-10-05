# Polynomial Evaluation

n = float(input("Enter the value of n: "))
coefficients = [3, 2, 1, 5] 
result = 0
power = len(coefficients) - 1
for i in range(len(coefficients)):
    result += coefficients[i] * (n ** power)
    power -= 1
print("Polynomial value at n =", n, "is", result)
