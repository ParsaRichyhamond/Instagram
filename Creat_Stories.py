def Creat_Stories(Username):
    f = open("Data.txt", "r")
    Y = f.read()
    if Y == "":
        Dict_of_all_Data = {}
    else:
        Dict_of_all_Data = eval(Y)
    f.close()
    os.system('cls')
    console.print("Creat Stories", style="bold blue")
    console.print(
        "Enter 'S' to creat a story or 'B' to go back to Stories menu:", style="bold", end="")
    In = input()
    if In == "S":
        console.print("Type you Story: ", style="bold green", end="")
        now = datetime.now()
        Time = "["+str(now)[:19]+"]:  "
        story = input()
        Dict_of_all_Data[Username]["Stories"].append(
            {"Time": Time, "Content": Time+story, "Liked_list": [], "Comments": []})
    elif In == "B":
        pass
    else:
        console.print("Error: Check your input", style="bold red")
        time.sleep(1)
    f = open("Data.txt", "w")
    f.write(str(Dict_of_all_Data))
    f.close()
