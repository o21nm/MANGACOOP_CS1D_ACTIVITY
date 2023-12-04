def find_smallest_factor(n):
    for i in range(2, n):
        if n % i == 0:
            print(f"The smallest factor other than 1 for {n} is {i}.")
            return

while True:
    try:
        user_input = int(input("Enter an Integer: "))
        if user_input > 2:
            find_smallest_factor(user_input)
            break
        else:
            print("Invalid input. Enter a number greater than 2.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")