def Creat_Post(Username):
    f = open("Data.txt", "r")
    Y = f.read()
    if Y == "":
        Dict_of_all_Data = {}
    else:
        Dict_of_all_Data = eval(Y)
    f.close()
    os.system('cls')
    console.print("Creat Post", style="bold blue")
    console.print(
        "Enter 'P' to Post or 'B' to go back to Posts menu:", style="bold", end="")
    In = input()
    if In == "P":
        console.print("Type you Post: ", style="bold green", end="")
        now = datetime.now()
        Time = "["+str(now)[:19]+"]:  "
        post = input()
        Dict_of_all_Data[Username]["Posts"]["My_Posts"].append(
            {"Content": Time+post, "Liked_list": [], "Comments": []})
    elif In == "B":
        pass
    else:
        console.print("Error: Check your input", style="bold red")
        time.sleep(1)
    f = open("Data.txt", "w")
    f.write(str(Dict_of_all_Data))
    f.close()
