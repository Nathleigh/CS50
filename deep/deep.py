user_thought = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
user_thought = user_thought.strip().lower()
# print(user_thought)
# if user_thought == ('42' or 'forty two' or 'forty-two'):
if user_thought in ['42', 'forty two', 'forty-two']:
    print("Yes")
else:
    print("No")
