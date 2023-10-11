# CS50’s Introduction to Programming with Python - problem set 4 - professor
import random


def main():
    level = get_level()
    correct = 0
    for i in range(10):  # 10 questions
        x = generate_integer(level)
        y = generate_integer(level)
        answer = x + y
        mistakes = 0
        for j in range(3):  # 3 attempts allowed
            attempt = input(f"{x} + {y} = ")
            if attempt.isdecimal():
                attempt = int(attempt)
                if attempt == answer:
                    correct += 1
                    break
                else:
                    print("EEE")
                    mistakes += 1
            else:
                print("EEE")
                mistakes += 1
            if mistakes > 2:
                print(f"{x} + {y} = {answer}")
                break
    print("Score:", correct)


def get_level():
    while True:
        level = input("Level: ")
        if level.isdecimal():
            if int(level) > 0 and int(level) < 4:
                level = int(level)
                return level


def generate_integer(level):
    if level not in [1,2,3]:
        raise ValueError("Invalid level value. Expected 1 or 2 or 3")
    if level == 1:
        low, high = 0, 9
    elif level == 2:
        low, high = 10, 99
    elif level == 3:
        low, high = 100, 999
    num = random.choice(range(low, high + 1))
    return num


if __name__ == "__main__":
    main()