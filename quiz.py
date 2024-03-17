print("Welcome to Quiz Game!")

playing = input("Do you want to play? ")

if playing.lower() == 'yes':
    print("Okay! Let's play :)")

answer = input("What does CPU stands for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
else:
    print("Incorrect!")