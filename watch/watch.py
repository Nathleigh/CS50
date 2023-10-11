# Harvard CS50P week 7 - Regex
# You’d like to extract the URLs of YouTube videos that are embedded in pages
# (e.g., https://www.youtube.com/embed/xvFZjo5PgG0),
# converting them back to shorter, shareable youtu.be URLs (e.g., https://youtu.be/xvFZjo5PgG0)
# where they can be watched on YouTube itself.
# In a file called watch.py, implement a function called parse that expects a str of HTML as input,
# extracts any YouTube URL that’s the value of a src attribute of an iframe element therein, and
# returns its shorter, shareable youtu.be equivalent as a str. Expect that any such URL will be in
# one of the formats below. Assume that the value of src will be surrounded by double quotes.
# And assume that the input will contain no more than one such URL.
# If the input does not contain any such URL at all, return None.
# test data: src="https://www.youtube.com/embed/xvFZjo5PgG0"
import re
import string


def main():
    print(parse(input("HTML: ")))


def parse(s):
    match = re.search(r'src=".+youtube.+"', s)
    if match:
        link = match.group()
        # print(link)
        endcode = link.split('/')[-1].rstrip(string.punctuation)
        # print(endcode)
        return "https://youtu.be/" + endcode

    else:
        return None


if __name__ == "__main__":
    main()
