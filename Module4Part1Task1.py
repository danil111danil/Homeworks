# Task 1:
start = int(input("Enter first number: "))
end = int(input("Enter second number: "))
# Check for non-negative integers
if start < 0 or end < 0:
    print("Error. Please, use non-negative integer numbers.")
else:
    # Swap if end is less than start
    if end < start:
        start, end = end, start

    # Adjust the start to the next multiple of 7 if necessary
    if start % 7 != 0:
        start += 7 - (start % 7)

    # Loop through the range starting at adjusted the start, ending at the end, stepping by 7
    for i in range(start, end + 1, 7):
        print(f"{i}", end=" ")