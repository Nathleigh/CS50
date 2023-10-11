def main():
    greeting = input("Greeting: ").strip()
    output = value(greeting)
    print(f"${output}")


def value(greeting):
    greeting = greeting.lower()
    if greeting.startswith("hello"):
        pay = 0
    elif greeting.startswith("h"):
        pay = 20
    else:
        pay = 100
    return pay


if __name__ == "__main__":
    main()






