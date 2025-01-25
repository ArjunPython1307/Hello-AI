Name = input("What is your name")
print("Hi I am a chat bot how is your day today",Name)
mood = input("(Good/Bad)")
mood = mood.lower()
if mood == "good":
    print("I am glad to here that")
elif mood == "bad":
    print(" I am sorry to here that")
else:
    print("Please type the given responses")