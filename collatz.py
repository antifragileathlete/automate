import sys

print("Give number")
userInput = int(input())


def collatz(number):
    global userInput
    if number % 2 == 0:
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
