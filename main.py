print("Program starting.")
print()
print("Check multiplicative persistence.")

n = int(input("Insert an integer: "))
count = 0

while n >= 10:
    digits = [int(digit) for digit in str(n)]
    product = 1

    for digit in digits:
        product *= digit

    line = " * ".join(str(digit) for digit in digits)
    print(f"{line} = {product}")

    n = product
    count += 1

print("No more steps.")
print()
print(f"This program took {count} step(s)")
print()
print("Program ending.")