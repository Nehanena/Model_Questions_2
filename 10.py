# Hourglass Pattern

r=int(input("enter number of rows: "))
for i in range(r, 0, -1):
        print(" " * (r - i) + "* " * i)
for i in range(2, r + 1):
        print(" " * (r - i) + "* " * i)
print()        