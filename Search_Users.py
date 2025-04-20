def Search_Users(Username):
    f = open("Data.txt", "r")
    Y = f.read()
    if Y == "":
        Dict_of_all_Data = {}
    else:
        Dict_of_all_Data = eval(Y)
    f.close()
    while True:
        os.system('cls')
        console.print("Search Username", style="bold blue")
        console.print("[bold yellow]1.    ", end="")
        console.print("Find a Username", style="bold")
        console.print("[bold yellow]2.    ", end="")
        console.print("Back to Home page", style="bold")
        console.print("Enter Your choice", style="bold", end="")
        console.print("[1/2]:", style="bold blue", end="")
        In = input()
        if In == "1":
            console.print("Enter Username: ", style="bold yellow", end="")
            username = input()
            if username in Dict_of_all_Data.keys():
                if Username not in Dict_of_all_Data[username]["Block_list"]:
                    while True:
                        os.system('cls')
                        console.print("[bold yellow]1.    ", end="")
                        console.print("Username: ", style="bold green", end="")
                        console.print(username, style="bold blue")
                        console.print("[bold yellow]2.    ", end="")
                        console.print("Email: ", style="bold green", end="")
                        console.print(
                            Dict_of_all_Data[username]["Email"], style="bold")
                        console.print("[bold yellow]3.    ", end="")
                        console.print("Biography ", style="bold green", end="")
                        console.print(
                            Dict_of_all_Data[username]["Biography"], style="bold red")
                        console.print("[bold yellow]4.    ", end="")
                        console.print(
                            "Followers: ", style="bold green", end="")
                        console.print(
                            str(len(Dict_of_all_Data[username]["Followers"])), style="bold blue")
                        console.print("[bold yellow]5.    ", end="")
                        console.print(
                            "Following: ", style="bold green", end="")
                        console.print(
                            str(len(Dict_of_all_Data[username]["Following"])), style="bold blue")
                        console.print("[bold yellow]6.    ", end="")
                        if Dict_of_all_Data[username]["Privet"]:
                            console.print("Send a Request to ",
                                          style="bold green", end="")
                        else:
                            console.print(
                                "Follow ", style="bold green", end="")
                        console.print(username, style="bold red")
                        console.print("[bold yellow]7.    ", end="")
                        console.print("Unfollow ", style="bold green", end="")
                        console.print(username, style="bold red")
                        console.print("[bold yellow]8.    ", end="")
                        console.print("Block User", style="bold red")
                        console.print("[bold yellow]9.    ", end="")
                        console.print("Back", style="bold green")
                        console.print("Enter Your choice",
                                      style="bold", end="")
                        console.print("[4/5/6/7/8/9]:",
                                      style="bold blue", end="")
                        In = input()
                        if In == "4":
                            os.system('cls')
                            console.print("Followers", style="bold blue")
                            Counter = 1
                            Len = len(Dict_of_all_Data[username]["Followers"])
                            if Len > 0:
                                for user in Dict_of_all_Data[username]["Followers"]:
                                    console.print(
                                        "[bold yellow]"+str(Counter)+".    ", end="")
                                    if user != Username:
                                        console.print(user, style="bold")
                                    else:
                                        console.print("You", style="bold")
                                    Counter += 1
                            else:
                                console.print(
                                    "User Has no Followers", style="bold green")
                            console.print(
                                "Press Enter to go back to User's Profile", style="bold yellow")
                            k = keyboard.wait("enter")

                        elif In == "5":
                            os.system('cls')
                            console.print("Following", style="bold blue")
                            Counter = 1
                            Len = len(Dict_of_all_Data[username]["Following"])
                            if Len > 0:
                                for user in Dict_of_all_Data[username]["Following"]:
                                    console.print(
                                        "[bold yellow]"+str(Counter)+".    ", end="")
                                    if user != Username:
                                        console.print(user, style="bold")
                                    else:
                                        console.print("You", style="bold")
                                    Counter += 1
                            else:
                                console.print(
                                    "User Has no Following", style="bold green")
                            console.print(
                                "Press Enter to go back to User's Profile", style="bold yellow")
                            k = keyboard.wait("enter")

                        elif In == "6":
                            if Dict_of_all_Data[username]["Privet"] and (Username not in Dict_of_all_Data[username]["Block_list"]) and (Username not in Dict_of_all_Data[username]["Followers"]):
                                if Username not in Dict_of_all_Data[username]["Requests"]:
                                    Dict_of_all_Data[username]["Requests"].append(
                                        Username)
                                    f = open("Data.txt", "w")
                                    f.write(str(Dict_of_all_Data))
                                    f.close()
                                    console.print(
                                        "Request sent to "+username+"!", style="bold green")
                                    time.sleep(1)
                                else:
                                    console.print(
                                        "You have already sent a Request to "+username+"!", style="bold green")
                                    time.sleep(1.5)
                            elif Username not in Dict_of_all_Data[username]["Block_list"]:
                                if Username not in Dict_of_all_Data[username]["Followers"]:
                                    Dict_of_all_Data[username]["Followers"].append(
                                        Username)
                                    Dict_of_all_Data[Username]["Following"].append(
                                        username)
                                    f = open("Data.txt", "w")
                                    f.write(str(Dict_of_all_Data))
                                    f.close()
                                    console.print(
                                        "You followed "+username+"!", style="bold green")
                                    time.sleep(1)
                                else:
                                    console.print(
                                        "You have already followed "+username+"!", style="bold green")
                                    time.sleep(1)
                            else:
                                console.print(
                                    "You have been blocked by "+username+"!", style="bold red")
                                time.sleep(1)

                        elif In == "7":
                            if username in Dict_of_all_Data[Username]["Following"]:
                                Dict_of_all_Data[username]["Followers"].remove(
                                    Username)
                                Dict_of_all_Data[Username]["Following"].remove(
                                    username)
                                f = open("Data.txt", "w")
                                f.write(str(Dict_of_all_Data))
                                f.close()
                                console.print("You Unfollowed " +
                                              username+"!", style="bold green")
                                time.sleep(2)
                            else:
                                console.print(
                                    "You have not followed "+username+" yet!", style="bold green")
                                time.sleep(1)

                        elif In == "8":
                            if username not in Dict_of_all_Data[Username]["Block_list"]:
                                Dict_of_all_Data[Username]["Block_list"].append(
                                    username)
                                if username in Dict_of_all_Data[Username]["Followers"]:
                                    Dict_of_all_Data[Username]["Followers"].remove(
                                        username)
                                    Dict_of_all_Data[username]["Following"].remove(
                                        Username)
                                f = open("Data.txt", "w")
                                f.write(str(Dict_of_all_Data))
                                f.close()
                                console.print("You Blocked " +
                                              username+"!", style="bold red")
                                time.sleep(1)
                            else:
                                console.print(
                                    "You have already Blocked "+username+"!", style="bold green")
                                time.sleep(1)

                        elif In == "9":
                            break

                        else:
                            console.print(
                                "Error: Please check your input", style="bold red")
                            time.sleep(2)

                elif Username in Dict_of_all_Data[username]["Block_list"]:
                    console.print("You have been blocked by " +
                                  username, style="bold red", end="")
                    time.sleep(1)

            else:
                console.print("Error: Username not found",
                              style="bold red", end="")
                time.sleep(1)
        elif In == "2":
            break
