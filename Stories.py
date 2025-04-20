def Stories(Username):
    Bool = True
    while Bool:
        os.system('cls')
        f = open("Data.txt", "r")
        Y = f.read()
        if Y == "":
            Dict_of_all_Data = {}
        else:
            Dict_of_all_Data = eval(Y)
        f.close()
        # _______________________________________Deleting expaierd stories______________________________
        Now = datetime.now()
        string_time1 = "["+str(Now)[:19]+"]:  "
        Time1 = datetime(int(string_time1[1:5]), int(string_time1[6:8]), int(string_time1[9:11]), int(
            string_time1[12:14]), int(string_time1[15:17]), int(string_time1[18:20]))
        for User in Dict_of_all_Data.keys():
            for story in Dict_of_all_Data[User]["Stories"]:
                f = open("Data.txt", "r")
                Y = f.read()
                if Y == "":
                    Dict_of_all_Data = {}
                else:
                    Dict_of_all_Data = eval(Y)
                f.close()
                string_time2 = story["Time"]
                Time2 = datetime(int(string_time2[1:5]), int(string_time2[6:8]), int(string_time2[9:11]), int(
                    string_time2[12:14]), int(string_time2[15:17]), int(string_time2[18:20]))
                difference = Time1 - Time2
                minutes = divmod(difference.seconds, 60)
                if int(minutes[0]) > 2:
                    Dict_of_all_Data[User]["Stories"].remove(story)
                    f = open("Data.txt", "w")
                    f.write(str(Dict_of_all_Data))
                    f.close()

        console.print("Stories", style="bold blue")
        console.print("[bold yellow]1.    ", end="")
        console.print("My Stories", style="bold")
        console.print("[bold yellow]2.    ", end="")
        console.print("View Stories", style="bold")
        console.print("[bold yellow]3.    ", end="")
        console.print("Back to Home Page", style="bold")
        console.print("Enter Your choice", style="bold", end="")
        console.print("[1/2/3]:", style="bold blue", end="")
        In = input()
        if In == "1":
            Bool2 = True
            while Bool2:
                os.system('cls')
                console.print("My Storeis", style="bold blue")
                Len = len(Dict_of_all_Data[Username]["Stories"])
                if Len > 0:
                    for i in range(0, Len):
                        console.print(50*"-", style="grey37")
                        console.print("[bold green]"+str(i+1)+".", end="")
                        console.print(
                            Dict_of_all_Data[Username]["Stories"][i]["Content"], style="bold plum2")
                    console.print(50*"-", style="medium_purple4")
                    console.print(
                        "Enter a number to view story details, 'S' to creat a story or 'B' to go back to Stories menu:", style="bold", end="")
                    string = "["
                    for i in range(1, Len):
                        string += str(i)+"/"
                    string += (str(Len)+"/S/B]:")
                    console.print(string, style="bold blue", end="")
                    In = input()
                    CHECK = True
                    for i in range(1, Len+1):
                        if str(i) == In:
                            CHECK = False
                            Story_Details(Username, Username, i-1)
                    if In == "B":
                        Bool2 = False
                    elif In == "S":
                        console.print("Type your Story: ",
                                      style="bold green", end="")
                        now = datetime.now()
                        Time = "["+str(now)[:19]+"]:  "
                        story = input()
                        Dict_of_all_Data[Username]["Stories"].append(
                            {"Time": Time, "Content": Time+story, "Liked_list": [], "Comments": []})
                        f = open("Data.txt", "w")
                        f.write(str(Dict_of_all_Data))
                        f.close()
                    elif CHECK:
                        console.print("Error: Check your input",
                                      style="bold red")
                        time.sleep(1)

                else:
                    console.print(
                        "You have no Story yet, Enter 'S' to Creat a Story or 'B' to go back to Stories menu:", style="bold", end="")
                    console.print("[C/B]:", style="bold blue", end="")
                    Inp = input()
                    if Inp == "S":
                        Creat_Stories(Username)
                        f = open("Data.txt", "r")
                        Y = f.read()
                        if Y == "":
                            Dict_of_all_Data = {}
                        else:
                            Dict_of_all_Data = eval(Y)
                        f.close()
                    elif Inp == "B":
                        Bool2 = False
                    else:
                        console.print("Error: Check your input",
                                      style="bold red")
                        time.sleep(1)
        elif In == "2":
            while True:
                os.system('cls')
                console.print("View Stories", style="bold blue")
                are_there_any_stories = False
                list_of_followings_who_have_story = []
                for username in Dict_of_all_Data[Username]["Following"]:
                    if len(Dict_of_all_Data[username]["Stories"]) > 0:
                        list_of_followings_who_have_story.append(username)
                        are_there_any_stories = True
                if are_there_any_stories:
                    Len2 = len(list_of_followings_who_have_story)
                    for i in range(0, Len2):
                        console.print("[bold green]"+str(i+1)+". ", end="")
                        console.print(
                            list_of_followings_who_have_story[i], style="bold light_sea_green")
                    console.print(
                        "Enter a number to view users stories or 'B' to go back to Stories menu:", style="bold", end="")
                    string = "["
                    for i in range(1, Len2):
                        string += str(i)+"/"
                    string += (str(Len2)+"/B]:")
                    console.print(string, style="bold blue", end="")
                    In = input()
                    check = True
                    for i in range(1, Len2+1):
                        if str(i) == In:
                            check = False
                            while True:
                                os.system('cls')
                                username = list_of_followings_who_have_story[i-1]
                                console.print(
                                    username, style="bold green", end="")
                                console.print("'s Stories", style="bold blue")
                                Len = len(
                                    Dict_of_all_Data[username]["Stories"])
                                for j in range(0, Len):
                                    console.print(50*"-", style="grey37")
                                    console.print(
                                        "[bold green]"+str(j+1)+".", end="")
                                    console.print(
                                        Dict_of_all_Data[username]["Stories"][j]["Content"], style="bold plum2")
                                console.print(50*"-", style="medium_purple4")
                                console.print(
                                    "Enter a number to view Stories details or 'B' to go back to Stories menu:", style="bold", end="")
                                string = "["
                                for j in range(1, Len):
                                    string += str(j)+"/"
                                string += (str(Len)+"/B]:")
                                console.print(
                                    string, style="bold blue", end="")
                                Inp = input()
                                CHECK = True
                                for j in range(1, Len+1):
                                    if str(j) == Inp:
                                        CHECK = False
                                        Story_Details(Username, username, j-1)
                                if Inp == "B":
                                    break

                    if In == "B":
                        break
                    elif check:
                        console.print("Error: Check your input",
                                      style="bold red")
                        time.sleep(1)

                else:
                    console.print(
                        "There are no Stories for you :(", style="bold cyan")
                    time.sleep(2)
                    break
        elif In == "3":
            break
