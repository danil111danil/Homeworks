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