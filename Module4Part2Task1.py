# Task 1:
start = int(input("Enter first number: "))
end = int(input("Enter second number: "))
if start < 0 or end < 0:
    print("Error. Please, use non-negative integer numbers.")
else:
    if end < start:
        start, end = end, start

    even_sum = 0
    even_count = 0
    odd_sum = 0
    odd_count = 0
    div9_sum = 0
    count_div9 = 0
    # First:
    print("\n")
    print("Even numbers:", end=" ")
    for even_numbers in range(start, end + 1):
        if even_numbers % 2 == 0:
            print(f"{even_numbers}", end=" ")
            even_sum += even_numbers
            even_count += 1
    # Second:
    print("\n")
    print("Odd numbers:", end=" ")
    for odd_numbers in range(start, end + 1):
        if odd_numbers % 2 != 0:
            print(f"{odd_numbers}", end=" ")
            odd_sum += odd_numbers
            odd_count += 1
    # Third:
    print("\n")
    print("Numbers dividable by 9:", end=" ")
    for div_by_9 in range (start, end + 1):
        if div_by_9 % 9 == 0:
            print(f"{div_by_9}", end=" ")
            count_div9 += 1
            div9_sum += div_by_9
    # Fourth:
    print("\n")
    if even_count > 0:
        print(f"Average for even numbers: {even_sum / even_count:.2f}")
    else:
        print("No even numbers in the range.")
    if odd_count > 0:
        print(f"Average for odd numbers: {odd_sum / odd_count:.2f}")
    else:
        print("No odd numbers in the range.")
    if count_div9 > 0:
        print(f"Average for numbers dividable by 9: {div9_sum / count_div9:.2f}")
    else:
        print("No numbers dividable by 9 in the range.")