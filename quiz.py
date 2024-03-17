print("Welcome to Quiz Game!")

playing = input("Do you want to play? ")

if playing.lower() == 'yes':
    print("Okay! Let's play :)")

score = 0

answer = input("What does CPU stands for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stands for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stands for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


answer = input("What does PSU stands for? ")
if answer.lower() == "power supply unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does HDD stands for? ")
if answer.lower() == "hard disk drive":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does SSD stands for? ")
if answer.lower() == "solid state drive":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does BIOS stands for? ")
if answer.lower() == "basic input/output system" or "basic input output system":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does VGA stands for? ")
if answer.lower() == "video graphics array":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does NIC stands for? ")
if answer.lower() == "network interface card":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does CMOS stands for? ")
if answer.lower() == "complementary mental-oxide semiconductor" or "complementary mental oxide semiconductor":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " question correct!")
print("You got " + str((score / 10) * 100) + "%.")