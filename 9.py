# ConcentricSquareNumbers(Hard)

n = int(input("Enter the number of layers: "))
s = 2 * n - 1
for i in range(s):
    for j in range(s):
        print(n - min(i, j, s - 1 - i, s - 1 - j), end="")
    print()
