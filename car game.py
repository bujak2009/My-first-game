print("""
This is a car game! You can go and stop and when you ready - stop and quit the car.
Type 'help' if you don't know what to do ;)
""")
quit_number = 0
quit_limit = 2
car_started = False
command = ""
while True:
    command = input("What we do? ").lower()
    if command == "start":
        if car_started:
            print("Car is already started, man...")
        else:
            car_started = True
            print("Car started... We are on the way!")
    elif command == "stop":
        if not car_started:
            print("Don't you see? It's not moving!")
        else:
            car_started = False
            print("Car stopped.")
    elif command == "help":
        print("""
start - to start a car
stop - to stop a car
quit - to quit a car and end the game
        """)
    elif command == "quit":
        if not car_started:
            print("You left the car! Congratulation - You survived!")
            print("GAME OVER")
            break
        else:
            print("Don't do that! You will kill yourself!!!")
            while quit_number < quit_limit:
                first_answer = input("Are you really sure about this? Yes or No ")
                if first_answer == "No":
                    print("Huh, that was close...")
                    break
                elif first_answer == "Yes":
                    quit_number += 1
                    last_answer = input("Are you REALLY sure about this? Yes or No ")
                    if last_answer == "No":
                        print("Huh, that was close...")
                        quit_number = 0
                        break
                    elif last_answer == "Yes":
                        quit_number += 1
            else:
                print("You jumped out of riding car! YOU ARE DEAD!")
                print("GAME OVER")
                break
    else:
        print("I don't understand, driver...")