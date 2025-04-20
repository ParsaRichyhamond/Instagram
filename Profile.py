def Profile(Username):
    f = open("Data.txt", "r")
    Y = f.read()
    if Y == "":
        Dict_of_all_Data = {}
    else:
        Dict_of_all_Data = eval(Y)
    f.close()
    while True:
        os.system('cls')
        console.print("Profile", style="bold blue")
        console.print("[bold yellow]1.    ", end="")
        console.print("Username: ", style="bold", end="")
        console.print(Username, style="bold green")
        console.print("[bold yellow]2.    ", end="")
        console.print("Email address: ", style="bold", end="")
        console.print(Dict_of_all_Data[Username]["Email"], style="bold green")
        console.print("[bold yellow]3.    ", end="")
        console.print("Password: ", style="bold", end="")
        console.print(Dict_of_all_Data[Username]["Password"], style="bold")
        console.print("[bold yellow]4.    ", end="")
        console.print("Biography: ", style="bold", end="")
        console.print(Dict_of_all_Data[Username]
                      ["Biography"], style="bold red")
        console.print("[bold yellow]5.    ", end="")
        console.print("Acount type: ", style="bold", end="")
        if Dict_of_all_Data[Username]["Privet"]:
            console.print("Private", style="bold", end="")
            console.print("(Chose to change to Public)", style="bold blue")
        else:
            console.print("Public", style="bold", end="")
            console.print("(Choose to change to Private)", style="bold blue")
        console.print("[bold yellow]6.    ", end="")
        console.print("Your Followers: ", style="bold green", end="")
        console.print(
            str(len(Dict_of_all_Data[Username]["Followers"])), style="bold blue")
        console.print("[bold yellow]7.    ", end="")
        console.print("Your Following: ", style="bold green", end="")
        console.print(
            str(len(Dict_of_all_Data[Username]["Following"])), style="bold blue")
        console.print("[bold yellow]8.    ", end="")
        console.print("Requests: ", style="bold green", end="")
        console.print(
            str(len(Dict_of_all_Data[Username]["Requests"])), style="bold blue")
        console.print("[bold yellow]9.    ", end="")
        console.print("Blocked Users: ", style="bold", end="")
        console.print(
            str(len(Dict_of_all_Data[Username]["Block_list"])), style="bold blue")
        console.print("[bold yellow]10.   ", end="")
        console.print(
            f"Check Notifications ({len(Dict_of_all_Data[Username]["notifications"])})", style="bold")
        console.print("[bold yellow]11.   ", end="")
        console.print("Back to Home Page", style="bold")
        console.print("Enter Your choice to Edit Information",
                      style="bold", end="")
        console.print("[1/2/3/4/5/6/7/8/9/10/11]: ", style="bold blue", end="")
        In = input()
        if In == "1":
            console.print("Enter Username: ", style="bold yellow", end="")
            Newusername = input()
            bol = True
            for key in Dict_of_all_Data.keys():
                if Newusername == key:
                    bol = False

            if bol:
                console.print(
                    "Are You sure You Want to Change Your Username to ", style="bold blue", end="")
                console.print(Newusername, style="bold yellow", end="")
                console.print(" ?", style="bold blue", end="")
                console.print("[Y/N]", style="bold red", end="")
                B = input()
                if B == "Y":
                    if Username != Newusername:
                        Dict_of_all_Data[Newusername] = copy.copy(
                            Dict_of_all_Data[Username])
                        Dict_of_all_Data.pop(Username)
                        Username = Newusername
                    console.print("Username Changed Successfully!",
                                  style="bold red", end="")
                    time.sleep(1)
                else:
                    console.print("OK Fine!", style="bold Yellow", end="")
                    time.sleep(1)
            else:
                console.print("Error: Username already Exists ",
                              style="bold red")
                time.sleep(1)

        elif In == "2":
            console.print("Enter Email address: ", style="bold yellow", end="")
            NewEmail = input()
            if Valid_email(NewEmail):
                bol = True
                for dict in Dict_of_all_Data.values():
                    if "Email" in dict.keys():
                        if dict["Email"] == NewEmail:
                            bol = False
                            break
                if bol:
                    console.print(
                        "Are You sure You wanna change Your Email address to ", style="bold blue", end="")
                    console.print(NewEmail, style="bold yellow", end="")
                    console.print(" ?", style="bold blue", end="")
                    console.print("[Y/N]", style="bold red", end="")
                    B = input()
                    if B == "Y":
                        if Dict_of_all_Data[Username]["Email"] != NewEmail:
                            Dict_of_all_Data[Username]["Email"] = NewEmail
                        console.print(
                            "Email address changed successfully!", style="bold red", end="")
                        time.sleep(1)
                    else:
                        console.print("OK Fine!", style="bold Yellow", end="")
                        time.sleep(1)
                else:
                    console.print(
                        "Error: Email address already Exists ", style="bold red")
                    time.sleep(1)
            else:
                console.print("Error: Unvalid Email address ",
                              style="bold red", end="")
                time.sleep(1)

        elif In == "3":
            console.print("Enter Your Password: ", style="bold green", end="")
            password1 = input()
            console.print("Enter Your Password again: ",
                          style="bold green", end="")
            password2 = input()
            if password1 == password2:
                Dict_of_all_Data[Username]["Password"] = password1
                console.print("Password", style="bold yellow", end="")
                console.print(" changed successfully!",
                              style="bold green", end="")
                time.sleep(1)
            else:
                console.print(
                    "Error: Your two passwords do not match ", style="bold red")
                time.sleep(1)

        elif In == "4":
            Bio = biography()
            print()
            console.print("Biography changed successfully!",
                          style="bold red", end="")
            time.sleep(1.5)
            Dict_of_all_Data[Username]["Biography"] = Bio

        elif In == "5":
            if Dict_of_all_Data[Username]["Privet"]:
                Dict_of_all_Data[Username]["Privet"] = False
            else:
                Dict_of_all_Data[Username]["Privet"] = True
            console.print("Acount type changed successfully!",
                          style="bold green", end="")
            time.sleep(1.5)

        elif In == "6":
            Followers(Username)

        elif In == "7":
            Following(Username)

        elif In == "8":
            Requests(Username)
            f = open("Data.txt", "r")
            Y = f.read()
            if Y == "":
                Dict_of_all_Data = {}
            else:
                Dict_of_all_Data = eval(Y)
            f.close()

        elif In == "9":
            Blocked_Users(Username)
            f = open("Data.txt", "r")
            Y = f.read()
            if Y == "":
                Dict_of_all_Data = {}
            else:
                Dict_of_all_Data = eval(Y)
            f.close()
        elif In == "10":
            if len(Dict_of_all_Data[Username]["notifications"]) > 0:
                for i in Dict_of_all_Data[Username]["notifications"]:
                    console.print(i, style="bold green")
                Dict_of_all_Data[Username]["notifications"] = []
                Inp3 = input()

            else:
                console.print("You have no notifications", style="bold red")
                time.sleep(1)
        elif In == "11":
            break

        else:
            console.print("Error: Please check your input", style="bold red")
            time.sleep(1)

        f = open("Data.txt", "w")
        f.write(str(Dict_of_all_Data))
        f.close()
