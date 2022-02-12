import time
import random

from numpy import Infinity

money = 10000
world_record = 39000000
max_gamble = world_record
min_gamble = 5

print(" ")
print("You have " + str(money) + " money")

while True:
    print(" ")
    time.sleep(1)
    gamble = int(raw_input("How much money would you like to gamble? "))
    print(" ")
    time.sleep(1)
    if gamble > max_gamble:
        print("Gamble a number lower than that")
        print(" ")
        time.sleep(1)
    elif gamble < min_gamble:
        print("Gamble a number higher than that")
        print(" ")
        time.sleep(1)
    elif gamble == money:
        option = raw_input("Are you sure you want to gamble all of your money? (yes/no): ").lower()
        print(" ")
        if option == "yes":
            number = random.randint(1, 5)
            guess = int(raw_input("Guess a number between 1 through 5: "))
            print(" ")
            time.sleep(1)
            if guess == number:
                print("You got the number right!")
                print(" ")
                time.sleep(1)
                money += gamble
                print("You have " + str(money) + " money now")
                print(" ")
                time.sleep(1)
                if money > world_record:
                    print("You have the world record for the most money gambled")
                    print(" ")
                    time.sleep(1)
                    print("Now you will get infinite money")
                    print(" ")
                    time.sleep(1)
                    money += Infinity
                    print("Your money now is " + str(money))
                    print(" ")
                    time.sleep(1)
                    break
            else:
                print("You got the number wrong :(")
                print(" ")
                time.sleep(1)
                print("The number was " + str(number))
                print(" ")
                time.sleep(1)
                money -= gamble
                print("You have " + str(money) + " money left")
                print(" ")
                time.sleep(1)
                print("You are broke now")
                print(" ")
                time.sleep(1)
                quit()
        elif option == "no":
            continue
                
    elif gamble > money:
        option2 = raw_input("Are you sure you want to gamble more than what you have? (yes/no): ").lower()
        print(" ")
        time.sleep(1)
        if option2 == "yes":
            number3 = random.randint(1, 5)
            guess3 = int(raw_input("Guess a number between 1 through 5: "))
            print(" ")
            time.sleep(1)
            if guess3 == number3:
                print("You got the number right!")
                print(" ")
                time.sleep(1)
                money += gamble
                print("You have " + str(money) + " money now")
                print(" ")
                time.sleep(1)
                if money > world_record:
                    print("You have the world record for the most money gambled")
                    print(" ")
                    time.sleep(1)
                    print("Now you will get infinite money")
                    print(" ")
                    time.sleep(1)
                    money += Infinity
                    print("Your money now is ∞")
                    print(" ")
                    time.sleep(1)
                    break
            else:
                print("You got the number wrong :(")
                print(" ")
                time.sleep(1)
                print("The number was " + str(number3))
                print(" ")
                time.sleep(1)
                money -= gamble
                print("You have " + str(money) + " money left")
                print(" ")
                time.sleep(1)
                print("You are arrested until you pay back all your debt")
                print(" ")
                time.sleep(1)
                quit()
        elif option2 == "no":
            continue
        
    elif money == 0:
        print("You can't gamble anymore")
        print(" ")
        time.sleep(1)
        quit()
    elif money < min_gamble:
        print("You don't have enough money to gamble")
        print(" ")
        time.sleep(1)
        quit()
    elif money > world_record:
        print("You have the world record for the most money gambled")
        print(" ")
        time.sleep(1)
        print("Now you will get infinite money")
        print(" ")
        time.sleep(1)
        money += Infinity
        print("Your money now is ∞")
        print(" ")
        time.sleep(1)
        break
    else:
        number2 = random.randint(1, 5)
        guess2 = int(raw_input("Guess a number between 1 through 5: "))
        print(" ")
        time.sleep(1)
        if guess2 == number2:
            print("You got the number right!")
            print(" ")
            time.sleep(1)
            money += gamble
            print("You have " + str(money) + " money now")
            print(" ")
            time.sleep(1)
            if money > world_record:
                print("You have the world record for the most money gambled")
                print(" ")
                time.sleep(1)
                print("Now you will get infinite money")
                print(" ")
                time.sleep(1)
                money += Infinity
                print("Your money now is ∞")
                print(" ")
                time.sleep(1)
                break
        else:
            print("You got it wrong :(")
            print(" ")
            time.sleep(1)
            print("The number was " + str(number2))
            print(" ")
            time.sleep(1)
            money -= gamble
            print("You have " + str(money) + " money left")
            print(" ")
            time.sleep(1)