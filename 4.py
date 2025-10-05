# Armstrong numbers with recursion

def is_armstrong(num, power):
    if num == 0:
        return 0
    digit = num % 10
    return (digit ** power) + is_armstrong(num // 10, power)

def find_armstrong(start, end):
    if start > end:
        return
    power = len(str(start))
    if start == is_armstrong(start, power):
        print(start)
    find_armstrong(start + 1, end)

small = int(input("Enter start of range: "))
large= int(input("Enter end of range: "))

print(f"Armstrong numbers between {small} and {large}:")
find_armstrong(small, large)


