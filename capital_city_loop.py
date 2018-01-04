from capitals import capitals_dict
import random

states = list()
practice = True

for item in capitals_dict:
    states.append(item)

while practice is True:
    statepick = random.choice(states)
    capitalpick = capitals_dict[statepick]
    print("What is the capital of %s?" % statepick)
    capitalchoice = input(">>")
    if capitalchoice.upper() == capitalpick.upper():
        print("Correct!")
    elif capitalchoice.upper() == "EXIT":
        practice = False
    elif capitalchoice.upper() == "GIVE UP":
        print(capitalpick)
    else:
        print("That is not correct. Try again.")
        print("What is the capital of %s?" % statepick)
        capitalchoice = input(">>")

print("Goodbye.")
