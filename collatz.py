import sys

print("Give number: ")
try:
    userInput = int(input())
    def collatz(number):
        if number % 2 == 0:
            global userInput
            userInput = number // 2
            print(userInput)
        else:
            userInput = 3 * number + 1
            print(userInput)
        return userInput

    while collatz(userInput) != 1:
        try:
            collatz(userInput)
        except KeyboardInterrupt:
            sys.exit()
except ValueError:
    print("You have to enter an integer")

