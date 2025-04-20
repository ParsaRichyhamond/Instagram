def Story_Details(Username, username, n):
    f = open("Data.txt", "r")
    Y = f.read()
    if Y == "":
        Dict_of_all_Data = {}
    else:
        Dict_of_all_Data = eval(Y)
    f.close()
    while True:
        os.system('cls')
        number_of_likes = len(
            Dict_of_all_Data[username]["Stories"][n]["Liked_list"])
        if username == Username:
            console.print("You", style="bold blue")
        else:
            console.print(username, style="bold blue")
        console.print(50*"-", style="bold red")
        console.print(Dict_of_all_Data[username]
                      ["Stories"][n]["Content"], style="bold")
        console.print(50*"-", style="bold red")
        console.print("[bold yellow]1.    ", end="")
        console.print("Liked by "+str(number_of_likes)+" Users", style="bold")
        console.print("[bold yellow]2.    ", end="")
        console.print("Comments", style="bold")
        console.print("[bold yellow]3.    ", end="")
        console.print("Tag someone", style="bold")
        console.print("[bold yellow]4.    ", end="")
        console.print("Back", style="bold yellow")
        console.print("Enter Your choice", style="bold", end="")
        console.print("[1/2/3/4]:", style="bold blue", end="")
        In = input()
        if In == "1":
            os.system('cls')
            console.print(50*"-", style="bold red")
            console.print(Dict_of_all_Data[username]
                          ["Stories"][n]["Content"], style="bold")
            console.print(50*"-", style="bold red")
            if number_of_likes > 0:
                for o in range(0, number_of_likes):
                    console.print("[bold yellow]"+str(o+1)+". ", end="")
                    user = Dict_of_all_Data[username]["Stories"][n]["Liked_list"][o]
                    if user == Username:
                        console.print("You", style="bold green")
                    else:
                        console.print(user, style="bold")
                console.print(
                    "Enter 'L' to like the Story or 'B' to go back to View Stories:", style="bold orange4", end="")
                Inp1 = input()
                if Inp1 == "L":
                    if Username not in Dict_of_all_Data[username]["Stories"][n]["Liked_list"]:
                        Dict_of_all_Data[username]["Stories"][n]["Liked_list"].append(
                            Username)
                        console.print("You liked this story!",
                                      style="bold sea_green3", end="")
                        time.sleep(1)
                    else:
                        console.print(
                            "You have already liked this story!", style="bold sea_green3", end="")
                        time.sleep(1)

            else:
                console.print("No one has liked this story,",
                              style="bold green", end="")
                console.print(
                    " Enter 'L' to Like or 'B' to go back to Story Details:", style="bold blue_violet", end="")
                Inp = input()
                if Inp == "L":
                    if Username not in Dict_of_all_Data[username]["Stories"][n]["Liked_list"]:
                        Dict_of_all_Data[username]["Stories"][n]["Liked_list"].append(
                            Username)
                        console.print("You liked this story!",
                                      style="bold sea_green3", end="")
                        time.sleep(1)
                    else:
                        console.print(
                            "You have already liked this story!", style="bold sea_green3", end="")
                        time.sleep(1)
                elif Inp == "B":
                    break
                else:
                    console.print("Error: Check your input", style="bold red")
                    time.sleep(1)

        elif In == "2":
            while True:
                os.system('cls')
                console.print(50*"-", style="bold red")
                console.print(
                    Dict_of_all_Data[username]["Stories"][n]["Content"], style="bold")
                console.print(50*"-", style="bold red")
                List_of_comments = Dict_of_all_Data[username]["Stories"][n]["Comments"]
                number_of_comments = len(List_of_comments)
                if number_of_comments > 0:
                    for o in range(0, number_of_comments):
                        if List_of_comments[o][0] == Username:
                            console.print("You: ", style="bold green", end="")
                        else:
                            console.print(
                                List_of_comments[o][0]+": ", style="bold", end="")
                        console.print(
                            List_of_comments[o][1], style="bold aquamarine3")
                    console.print(
                        "Enter 'C' to add a comment or 'B' to go back to Story Details:", style="bold blue_violet", end="")
                    Inp1 = input()
                    if Inp1 == "C":
                        console.print("Type your comment:",
                                      style="bold green", end="")
                        comment = input()
                        Dict_of_all_Data[username]["Stories"][n]["Comments"].append(
                            [Username, comment])
                    elif Inp1 == "B":
                        break
                    else:
                        console.print("Error: Check your input",
                                      style="bold red")
                        time.sleep(0.5)

                else:
                    console.print(
                        "There are No comments for this story,", style="bold green", end="")
                    console.print(
                        " Enter 'C' to add a comment or 'B' to go back to Story Details:", style="bold blue_violet", end="")
                    Inp = input()
                    if Inp == "C":
                        console.print("Type your comment:",
                                      style="bold wheat4", end="")
                        comment = input()
                        Dict_of_all_Data[username]["Stories"][n]["Comments"].append(
                            [Username, comment])
                    elif Inp == "B":
                        break
                    else:
                        console.print("Error: Check your input",
                                      style="bold red")
                        time.sleep(1)
        elif In == "4":
            break
        elif In == "3":
            if len(Dict_of_all_Data[Username]["Following"]) > 0:
                for i, k in enumerate(Dict_of_all_Data[Username]["Following"]):
                    console.print(f"{i}.{k}", style="bold blue")
                chose = input("Choose who to tag by their index: ")
                try:
                    tagged = Dict_of_all_Data[Username]["Following"][int(
                        chose)]
                    console.print(f"has been taged {tagged}", style="bold")
                    Dict_of_all_Data[tagged]["notifications"].append(
                        f"{Username} tagged you in a story: {Dict_of_all_Data[username]["Stories"][n]["Content"]} by {username}")
                    time.sleep(1)
                except:
                    console.print("Eror :wrong input !!!!", style="bold red")
                    time.sleep(1)
            else:
                console.print("you dont have anyone to tag")
                time.sleep(1)

        else:
            console.print("Error: Check your input", style="bold red")
            time.sleep(1)
        f = open("Data.txt", "w")
        f.write(str(Dict_of_all_Data))
        f.close()
