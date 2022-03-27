print("Welcome to my quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
point = 0
question = 0

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    point += 1
    question += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    point += 2
    question += 1
else:
    print("Incorrect!")

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    point += 3
    question += 1
else:
    print("Incorrect!")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print("Correct!")
    point += 4
    question += 1
else:
    print("Incorrect!")

answer = input("What does DOS stand for? ")
if answer.lower() == "disk operating system":
    print("Correct!")
    point += 5
    question += 1
else:
    print("Incorrect!")
print("You got " + str(question) + " questions correct!")
print("You got " + str((point / 15) * 100) + "%.")
