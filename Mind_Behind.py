import sys


def run():
    while True:
        try:
            name = str(input("Your Name :> "))
            print("Hello "+str(name)+" Your Adventure begins Here.")
            print("You are lost in a cave and you want to Get outside the cave"
                  ", There are Torches Placed on the Wall."
                  " Do You Want to Follow them ?")
            follow = str(input("Y/N :> "))
            if follow == "Y":
                print("Ok, There are two ways."
                      " Left or Right"
                      " Left way is glowing"
                      " while Right is not."
                      " Which One Will you choose?")
                turn = str(input("L/R :> "))
                if turn == "R":
                    print("You are safe till now.")
                    print("Ok now you are moving on and you found a box there"
                          " with a key inside you picked it up and went"
                          " from there.")
                    print("Do you want to keep moving or go back to the box ?")
                    back = str(input("M(Move)/B(Box) :> "))
                    if back == "M":
                        print("There are three Doors and the key will "
                              "disappear after single use. Which door will "
                              "you choose?")
                        door = str(input("D1/D2/D3 :> "))
                        if door == "D2":
                            print("Hurrah! you are Out now. GO and Enjoy!")
                            break
                        elif door == "D1" or door == "D3":
                            print("You will be here forever now!!")
                            break
                        else:
                            print("Cave is not for you, go to hell!!")
                            break
                    elif back == "B":
                        print("It's Nothing There Why Did you come back.")
                        print("Now be here forever.")
                        break
                    else:
                        print("Cave is not for you, go to hell!!")
                        break
                elif turn == "L":
                    print("You chooses Lava. It is not easy to get out.")
                    break
                else:
                    print("Cave is not for you, go to hell!!")
                    break
            elif follow == "N":
                print("Then Stay Stuck Here, I am Going!")
                break
            else:
                print("Cave is not for you, go to hell!!")
                break
        except KeyboardInterrupt:
            print("Exiting the Program!")
            sys.exit()
        except ValueError:
            print("I think you can't read it or don't want to read.")
            sys.exit()
