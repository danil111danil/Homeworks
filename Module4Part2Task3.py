# Task 3:
print('Enter 7 to leave the "app".')
print('Current "app" determines if number is positive, negative or equal to zero.')
while True:
    number = float(input("Enter a number: "))

    if number == 7:
        print("Goodbye!")
        break

    elif number > 0:
        print("Number is positive.")
    elif number < 0:
        print("Number is negative.")
    else:
        print("Number is equal to zero.")