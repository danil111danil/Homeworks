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