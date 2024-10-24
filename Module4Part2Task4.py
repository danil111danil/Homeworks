total_sum = 0
min_number = None
max_number = None

print('Enter 7 to leave the "app".')
print('Current "app" summarizes and finds minimum and maximum number.')
while True:
    number = float(input("Enter a number: "))

    if number == 7:
        print("Goodbye!")
        break

    total_sum += number

    if min_number is None or number < min_number:
        min_number = number
    if max_number is None or number > max_number:
        max_number = number

    print(f"Current sum: {total_sum}, Min: {min_number}, Max: {max_number}")