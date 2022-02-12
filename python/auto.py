import time
import random

money_spent = 0


def main():
    limit = random.randint(1, 500000)
    print("The limit is 1 through 500,000")
    print(" ")
    time.sleep(1)
    while True:
        spend = int(raw_input("How much money do you want to spend? but there is a limit: "))
        print(" ")
        time.sleep(1)
        global money_spent
        money_spent += spend
        if money_spent > limit:
            print("You were " + str(money_spent - limit) + " over the limit")
            print(" ")
            time.sleep(1)
            print("Now, you have no money")
            print(" ")
            time.sleep(1)
            quit()
        elif money_spent == limit:
            print("I'm impressed you landed exactly on the limit")
            print(" ")
            time.sleep(1)
            quit()
        elif spend == 0:
            print("Spend at least a dollar")
            print(" ")
            time.sleep(1)
        else:
            print("You have spent " + str(money_spent) + " money in all")
            print(" ")
            time.sleep(1)
            reveal_limit = raw_input("Are you willing to pay 100,000$ to know the limit? (yes/no): ").lower()
            print(" ")
            time.sleep(1)
            if reveal_limit == "yes":
                money_spent += 100000
                if money_spent > limit:
                    print("You were " + str(money_spent - limit) + " over the limit")
                    print(" ")
                    time.sleep(1)
                    print("Now, you have no money")
                    print(" ")
                    time.sleep(1)
                    quit()
                print("The limit is " + str(limit) + " money")
                print(" ")
                time.sleep(1)
            reveal = raw_input("Do you want to reveal how close you were to the limit? (yes/no): ").lower()
            print(" ")
            time.sleep(1)

            if reveal == "yes":
                print("You were " + str(limit - money_spent) + " away from the limit")
                print(" ")
                time.sleep(1)
                quit()
            elif reveal == "no":
                continue
            else:
                print("Not an option")
                print(" ")
                time.sleep(1)

main()
