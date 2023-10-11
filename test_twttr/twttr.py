
def main():
    msg = input("Input: ")
    msg2 = shorten(msg)
    print("Output:", msg2)
    print()


def shorten(word):
    short = ""
    for chr in word:
        if chr not in 'aeiouAEIOU':
            short += chr
    return short


if __name__ == "__main__":
    main()