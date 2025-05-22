import random
import time


print(r"""
+~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
| Seems like someone wants   |
| to roll a dice! If you are |
| interested in doing so,    |
| enter Y. If not, enter N   |
|      ____                  |
|     /\' .\    _____        |
|    /: \___\  / .  /\       |
|    \' / . / /____/..\      |
|     \/___/  \'  '\  /      |
|              \'__'\/       |
+~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
""")


def dice():
    dice = random.randint(1, 6)
    return dice


while True:
    roll = input("Roll the dice? (Y/N): ")
    if roll.upper() == 'Y':
        break
    elif roll.upper() == 'N':
        print("Adios!")
        exit()
    else:
        print("Please enter either Y or N")

while True:
    print("Then let's get started!")
    time.sleep(2)
    print("You rolled a...")

    # building suspense...
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)

    number = dice()
    print(number, "!")

    while True:
        again = input("Roll again? (Y/N): ")
        if again.upper() == 'Y':
            break
        elif again.upper() == 'N':
            print("Adios!")
            exit()
        else:
            print("Please enter either Y or N")
