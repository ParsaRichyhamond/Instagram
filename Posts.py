def Posts(Username):
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
        console.print("Posts", style="bold blue")
        console.print("[bold yellow]1.    ", end="")
        console.print("My Posts", style="bold")
        console.print("[bold yellow]2.    ", end="")
        console.print("View Posts", style="bold")
        console.print("[bold yellow]3.    ", end="")
        console.print("Back to Home Page", style="bold")
        console.print("Enter Your choice", style="bold", end="")
        console.print("[1/2/3]:", style="bold blue", end="")
        In = input()
        if In == "1":
            Bool2 = True
            while Bool2:
                os.system('cls')
                console.print("My Posts", style="bold blue")
                Len = len(Dict_of_all_Data[Username]["Posts"]["My_Posts"])
                if Len > 0:
                    for i in range(0, Len):
                        console.print(50*"=", style="grey37")
                        console.print("[bold green]"+str(i+1)+".", end="")
                        console.print(
                            Dict_of_all_Data[Username]["Posts"]["My_Posts"][i]["Content"], style="bold plum2")
                    console.print(50*"=", style="medium_purple4")
                    console.print(
                        "Enter a number to view posts details, 'C' to creat a post or 'B' to go back to Posts menu:", style="bold", end="")
                    string = "["
                    for i in range(1, Len):
                        string += str(i)+"/"
                    string += (str(Len)+"/C/B]:")
                    console.print(string, style="bold blue", end="")
                    In = input()
                    CHECK = True
                    for i in range(1, Len+1):
                        if str(i) == In:
                            CHECK = False
                            Post_Details(Username, Username, i-1)
                    if In == "B":
                        Bool2 = False
                    elif In == "C":
                        console.print("Type you Post: ",
                                      style="bold green", end="")
                        now = datetime.now()
                        Time = "["+str(now)[:19]+"]:  "
                        post = input()
                        Dict_of_all_Data[Username]["Posts"]["My_Posts"].append(
                            {"Content": Time+post, "Liked_list": [], "Comments": []})
                        f = open("Data.txt", "w")
                        f.write(str(Dict_of_all_Data))
                        f.close()
                    elif CHECK:
                        console.print("Error: Check your input",
                                      style="bold red")
                        time.sleep(1)

                else:
                    console.print(
                        "You have no Posts yet, Enter 'C' to Creat a post or 'B' to go back to Posts:", style="bold", end="")
                    console.print("[C/B]:", style="bold blue", end="")
                    Inp = input()
                    if Inp == "C":
                        Creat_Post(Username)
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
                console.print("View Posts", style="bold blue")
                are_there_any_posts = False
                list_of_followings_who_have_post = []
                for username in Dict_of_all_Data[Username]["Following"]:
                    if len(Dict_of_all_Data[username]["Posts"]["My_Posts"]) > 0:
                        list_of_followings_who_have_post.append(username)
                        are_there_any_posts = True
                if are_there_any_posts:
                    Len2 = len(list_of_followings_who_have_post)
                    for i in range(0, Len2):
                        console.print("[bold green]"+str(i+1)+". ", end="")
                        console.print(
                            list_of_followings_who_have_post[i], style="bold light_sea_green")
                    console.print(
                        "Enter a number to view users posts or 'B' to go back to Posts menu:", style="bold", end="")
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
                                username = list_of_followings_who_have_post[i-1]
                                console.print(
                                    username, style="bold green", end="")
                                console.print("'s Posts", style="bold blue")
                                Len = len(
                                    Dict_of_all_Data[username]["Posts"]["My_Posts"])
                                for j in range(0, Len):
                                    console.print(50*"=", style="grey37")
                                    console.print(
                                        "[bold green]"+str(j+1)+".", end="")
                                    console.print(
                                        Dict_of_all_Data[username]["Posts"]["My_Posts"][j]["Content"], style="bold plum2")
                                console.print(50*"=", style="medium_purple4")
                                console.print(
                                    "Enter a number to view posts details or 'B' to go back to Posts menu:", style="bold", end="")
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
                                        Post_Details(Username, username, j-1)
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
                        "There are no posts for you :(", style="bold cyan")
                    time.sleep(2)
                    break
        elif In == "3":
            break
