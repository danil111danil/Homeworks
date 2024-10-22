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
# Task 2:
start = int(input("\nEnter first number: "))
end = int(input("Enter second number: "))
if start < 0 or end < 0:
    print("Error. Please, use non-negative integer numbers.")
else:
    if end < start:
        start, end = end, start
    # First:
    print("Ascending number:", end=" ")
    for asc_num in range(start, end + 1):
        print(f"{asc_num}", end=" ")
    # Second:
    print("\nDecreasing numbers:", end=" ")
    for dec_num in range(end, start - 1, -1):
        print(f"{dec_num}", end=" ")
    # Third:
    start1=start # To keep the start the same for the fourth sub-task.
    if start % 7 != 0:
        start += 7 - (start % 7)

    print("\nNumbers dividable by 7:", end=" ")
    for i in range(start, end + 1, 7):
        print(f"{i}", end=" ")
    # Fourth:
    count = 0
    for div_by_5 in range (start1, end + 1):
        if div_by_5 % 5 == 0:  # Check if the number is divisible by 5
            count += 1  # Increment the count

    print(f"\nTotal count of numbers divisible by 5: {count}")
# Task 3:
start = int(input("\nEnter first number: "))
end = int(input("Enter second number: "))
if start < 0 or end < 0:
    print("Error. Please, use non-negative integer numbers.")
else:
    if end < start:
        start, end = end, start
    for i in range(start, end + 1):
        if i % 3 == 0 and i % 5 == 0:
                print("FizzBuzz", end=" ")
        elif i % 3 == 0:
                print("Fizz", end=" ")
        elif i % 5 == 0:
                print("Buzz", end=" ")
        else:
            print(i, end=" ")