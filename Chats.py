def Chats(Username):
    f = open("Data.txt", "r")
    Y = f.read()
    if Y == "":
        Dict_of_all_Data = {}
    else:
        Dict_of_all_Data = eval(Y)
    f.close()
    while True:
        os.system('cls')
        console.print("Your Chats", style="bold blue")
        console.print("[bold yellow]1.    ", end="")
        console.print("Personal", style="bold")
        console.print("[bold yellow]2.    ", end="")
        console.print("Groups", style="bold")
        console.print("[bold yellow]3.    ", end="")
        console.print("Back to Home Page", style="bold")
        console.print("Enter Your choice", style="bold", end="")
        console.print("[1/2/3]: ", style="bold blue", end="")
        In = input()
        if In == "1":
            os.system('cls')
            Len1 = len(Dict_of_all_Data[Username]["Chats"]["Personal"])
            counter = 1
            if Len1 > 0:
                for username in Dict_of_all_Data[Username]["Chats"]["Personal"]:
                    console.print("[bold green]"+str(counter)+".    ", end="")
                    console.print(username, style="bold yellow", end="")
                    num_new_massage = Dict_of_all_Data[Username]["Chats"]["Personal"][username][0]
                    space = " "*(10-len(username))
                    if num_new_massage > 0:
                        console.print(
                            space+"(You have "+str(num_new_massage)+" new massages)", style="bold")
                    else:
                        print()
                    counter += 1
                console.print(
                    "Enter a number to start chat or 'B' to go back to Chat or 'C' to creat new chat", style="bold", end="")
                string = "["
                for i in range(1, Len1):
                    string += str(i)+"/"
                string += (str(Len1)+"/B/S]:")
                console.print(string, style="bold blue", end="")
                bool2 = True
                In = input()
                for i in range(1, Len1+1):
                    if str(i) == In:
                        Open_Chat(Username, list(
                            Dict_of_all_Data[Username]["Chats"]["Personal"].keys())[i-1], "Personal")
                        f = open("Data.txt", "r")
                        Y = f.read()
                        Dict_of_all_Data = eval(Y)
                        f.close()
                        bool2 = False
                if In == "B":
                    pass
                elif In == "C":
                    while True:
                        os.system('cls')
                        console.print("Creat chat", style="bold blue")
                        console.print("[bold yellow]1.    ", end="")
                        console.print("Enter Username", style="bold")
                        console.print("[bold yellow]2.    ", end="")
                        console.print("Back to Chats", style="bold")
                        console.print("Enter Your choice",
                                      style="bold", end="")
                        console.print("[1/2]: ", style="bold blue", end="")
                        In = input()
                        if In == "1":
                            console.print(
                                "Enter Username to creat a chat: ", style="bold blue", end="")
                            username = input()
                            if username in Dict_of_all_Data.keys():
                                if username in Dict_of_all_Data[Username]["Following"]:
                                    Dict_of_all_Data[Username]["Chats"]["Personal"][username] = [
                                        0]
                                    Dict_of_all_Data[username]["Chats"]["Personal"][Username] = [
                                        0]
                                    f = open("Data.txt", "w")
                                    f.write(str(Dict_of_all_Data))
                                    f.close()
                                    console.print(
                                        "A chat with "+username+" created successfuly!", style="bold green")
                                    time.sleep(1)
                                else:
                                    console.print(
                                        "You have to follow "+username+" first!", style="bold yellow")
                                    time.sleep(1)
                            else:
                                console.print(
                                    "Error: Username does not exist", style="bold red")
                                time.sleep(1)
                        elif In == "2":
                            break
                        else:
                            console.print(
                                "Error: Please check your input", style="bold red")
                            time.sleep(1)

                elif bool2:
                    console.print(
                        "Error: Please check your input", style="bold red")
                    time.sleep(1)

            else:
                while True:
                    os.system('cls')
                    console.print(
                        "You Have no Chats yet, enter 'C' to creat one or 'B' to go back to Chats:", style="bold green")
                    console.print("Enter your choice", style="bold", end="")
                    console.print("[C/B]: ", style="bold blue", end="")
                    In1 = input()
                    if In1 == "C":
                        while True:
                            os.system('cls')
                            console.print(
                                "Enter Username to creat a chat: ", style="bold blue", end="")
                            username = input()
                            if username in Dict_of_all_Data.keys():
                                if username in Dict_of_all_Data[Username]["Following"]:
                                    if username not in Dict_of_all_Data[Username]["Chats"]["Personal"].keys():
                                        Dict_of_all_Data[Username]["Chats"]["Personal"][username] = [
                                            0]
                                        Dict_of_all_Data[username]["Chats"]["Personal"][Username] = [
                                            0]
                                        f = open("Data.txt", "w")
                                        f.write(str(Dict_of_all_Data))
                                        f.close()
                                        console.print(
                                            "A chat with "+username+" created successfuly!", style="bold green")
                                        time.sleep(1)
                                    else:
                                        console.print(
                                            "You already have a chat with "+username+"!", style="bold green")
                                        time.sleep(1)
                                    break
                                else:
                                    console.print(
                                        "You have to follow "+username+" first!", style="bold yellow")
                                    time.sleep(1)
                                    break
                            else:
                                console.print(
                                    "Error: Username does not exist", style="bold red")
                                time.sleep(1)
                    elif In1 == "B":
                        break
                    else:
                        console.print(
                            "Error: Please check your input", style="bold red")
                        time.sleep(1)

        elif In == "2":
            os.system('cls')
            Len1 = len(Dict_of_all_Data[Username]["Chats"]["Groups"])
            counter = 1
            if Len1 > 0:
                for chat_name in Dict_of_all_Data[Username]["Chats"]["Groups"]:
                    console.print("[bold green]"+str(counter)+".    ", end="")
                    console.print(chat_name, style="bold yellow", end="")
                    Num_new_massage = Dict_of_all_Data[Username]["Chats"]["Groups"][chat_name][0]
                    if Num_new_massage > 0:
                        Space = " "*(10-len(chat_name))
                        console.print(
                            Space+"(You have "+str(Num_new_massage)+" new massages)", style="bold ")
                    else:
                        print()
                    counter += 1
                console.print(
                    "Enter a number to start a chat or 'B' to go back to Chat or 'C' to creat new Group", style="bold", end="")
                string = "["
                for i in range(1, Len1):
                    string += str(i)+"/"
                string += (str(Len1)+"/B/S]:")
                console.print(string, style="bold blue", end="")
                bool2 = True
                In = input()
                for i in range(1, Len1+1):
                    if str(i) == In:
                        Open_Chat(Username, list(
                            Dict_of_all_Data[Username]["Chats"]["Groups"].keys())[i-1], "Groups")
                        f = open("Data.txt", "r")
                        Y = f.read()
                        Dict_of_all_Data = eval(Y)
                        f.close()
                        bool2 = False
                if In == "B":
                    pass
                elif In == "C":
                    while True:
                        os.system('cls')
                        console.print("Creat New Group", style="bold blue")
                        console.print("[bold yellow]1.    ", end="")
                        console.print("Enter Group name", style="bold")
                        console.print("[bold yellow]2.    ", end="")
                        console.print("Back to Chats", style="bold")
                        console.print("Enter Your choice",
                                      style="bold", end="")
                        console.print("[1/2]: ", style="bold blue", end="")
                        In = input()
                        if In == "1":
                            while True:
                                console.print("Enter group name:",
                                              style="bold green", end="")
                                Chat_name = input()
                                if Chat_name not in Dict_of_all_Data[Username]["Chats"]["Groups"].keys():
                                    break
                                else:
                                    console.print(
                                        "Error: Chat name already exists", style="bold red")
                                    time.sleep(1)
                            Dict_of_all_Data[Username]["Chats"]["Groups"][Chat_name] = [
                                0, []]
                            counter2 = 1
                            while True:
                                os.system('cls')
                                console.print(
                                    "Add members to "+"[bold yelow]"+Chat_name, style="bold blue")
                                console.print("[bold yellow]1.    ", end="")
                                console.print("Add member", style="bold")
                                console.print("[bold yellow]2.    ", end="")
                                console.print("Back to Chats", style="bold")
                                console.print("Enter Your choice",
                                              style="bold", end="")
                                console.print(
                                    "[1/2]: ", style="bold blue", end="")
                                In = input()
                                if In == "1":
                                    console.print(
                                        "Enter "+str(counter2)+"th member: ", style="bold blue", end="")
                                    counter2 += 1
                                    username = input()
                                    if username in Dict_of_all_Data.keys():
                                        if username in Dict_of_all_Data[Username]["Following"]:
                                            Dict_of_all_Data[Username]["Chats"]["Groups"][Chat_name][1].append(
                                                username)
                                            console.print(
                                                "Member "+username+" Added to "+Chat_name+" successfuly!", style="bold green")
                                            time.sleep(1)
                                        else:
                                            console.print(
                                                "You have to follow "+username+" first!", style="bold yellow")
                                            time.sleep(1)
                                    else:
                                        console.print(
                                            "Error: Username does not exist", style="bold red")
                                        time.sleep(1)
                                elif In == "2":
                                    break
                                else:
                                    console.print(
                                        "Error: Please check your input", style="bold red")
                                    time.sleep(1)
                            Set_add_users = set(
                                Dict_of_all_Data[Username]["Chats"]["Groups"][Chat_name][1])
                            List_of_members = list(Set_add_users)
                            List_of_members.append(Username)
                            Dict_of_all_Data[Username]["Chats"]["Groups"][Chat_name][1] = copy.copy(
                                List_of_members)
                            List = copy.copy(
                                Dict_of_all_Data[Username]["Chats"]["Groups"][Chat_name][1])
                            for user in Dict_of_all_Data[Username]["Chats"]["Groups"][Chat_name][1]:
                                Dict_of_all_Data[user]["Chats"]["Groups"][Chat_name] = [
                                    0, copy.copy(List)]
                            f = open("Data.txt", "w")
                            f.write(str(Dict_of_all_Data))
                            f.close()

                        elif In == "2":
                            break
                        else:
                            console.print(
                                "Error: Please check your input", style="bold red")
                            time.sleep(1)

                elif bool2:
                    console.print(
                        "Error: Please check your input", style="bold red")
                    time.sleep(1)

            else:
                while True:
                    os.system('cls')
                    console.print(
                        "You Have no Group yet, enter 'C' to creat one or 'B' to go back to Chats:", style="bold green")
                    console.print("Enter your choice", style="bold", end="")
                    console.print("[C/B]: ", style="bold blue", end="")
                    In1 = input()
                    if In1 == "C":
                        while True:
                            os.system('cls')
                            console.print("Creat New Group", style="bold blue")
                            console.print("[bold yellow]1.    ", end="")
                            console.print("Enter Group name", style="bold")
                            console.print("[bold yellow]2.    ", end="")
                            console.print("Back", style="bold")
                            console.print("Enter Your choice",
                                          style="bold", end="")
                            console.print("[1/2]: ", style="bold blue", end="")
                            In = input()
                            if In == "1":
                                while True:
                                    console.print(
                                        "Enter group name:", style="bold green", end="")
                                    Chat_name = input()
                                    if Chat_name not in Dict_of_all_Data[Username]["Chats"]["Groups"].keys():
                                        break
                                Dict_of_all_Data[Username]["Chats"]["Groups"][Chat_name] = [
                                    0]
                                counter2 = 1
                                members = [Username]
                                while True:
                                    os.system('cls')
                                    console.print(
                                        "Add members to "+"[bold yelow]"+Chat_name, style="bold blue")
                                    console.print(
                                        "[bold yellow]1.    ", end="")
                                    console.print("Add member", style="bold")
                                    console.print(
                                        "[bold yellow]2.    ", end="")
                                    console.print(
                                        "Back to Chats", style="bold")
                                    console.print(
                                        "Enter Your choice", style="bold", end="")
                                    console.print(
                                        "[1/2]: ", style="bold blue", end="")
                                    In = input()
                                    if In == "1":
                                        console.print(
                                            "Enter "+str(counter2)+" th member: ", style="bold blue", end="")
                                        counter2 += 1
                                        username = input()
                                        if username in Dict_of_all_Data.keys():
                                            if username in Dict_of_all_Data[Username]["Following"]:
                                                members.append(username)
                                                console.print(
                                                    "Member "+username+" Added to "+Chat_name+" successfuly!", style="bold green")
                                                time.sleep(1)
                                            else:
                                                console.print(
                                                    "You have to follow "+username+" first!", style="bold yellow")
                                                time.sleep(1)
                                        else:
                                            console.print(
                                                "Error: Username does not exist", style="bold red")
                                            time.sleep(1)
                                    elif In == "2":
                                        break
                                    else:
                                        console.print(
                                            "Error: Please check your input", style="bold red")
                                        time.sleep(1)
                                for user in members:
                                    Dict_of_all_Data[user]["Chats"]["Groups"][Chat_name] = [
                                        0, members]
                                f = open("Data.txt", "w")
                                f.write(str(Dict_of_all_Data))
                                f.close()

                            elif In == "2":
                                break
                            else:
                                console.print(
                                    "Error: Please check your input", style="bold red")
                                time.sleep(1)

                    elif In1 == "B":
                        break
                    else:
                        console.print(
                            "Error: Please check your input", style="bold red")
                        time.sleep(1)

        elif In == "3":
            break
        else:
            console.print("Error: Please check your input", style="bold red")
            time.sleep(1)
