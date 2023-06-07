def fizzbuzz(number):
    if number <= 0:
        return "Number must be bigger than 0"
    if (number % 3 == 0) and (number % 5 == 0):
        return "FizzBuzz"
    if number % 5 == 0:
        return "Buzz"
    if number % 3 == 0:
        return "Fizz"
    return number


while True:
    user_input = input("Enter an integer, or 'quit' to exit: ")
    if user_input.lower() == "quit":
        print("Bye Bye.")
        break
    try:
        print(fizzbuzz(int(user_input)))
    except ValueError:
        print("Invalid input. Please enter a valid integer or 'quit' to exit.")
