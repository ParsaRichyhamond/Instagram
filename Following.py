def Following(Username):
    os.system('cls')
    f = open("Data.txt", "r")
    Y = f.read()
    if Y == "":
        Dict_of_all_Data = {}
    else:
        Dict_of_all_Data = eval(Y)
    f.close()
    console.print("Your Followings", style="bold blue")
    Counter = 1
    Len = len(Dict_of_all_Data[Username]["Following"])
    if Len > 0:
        for user in Dict_of_all_Data[Username]["Following"]:
            console.print("[bold yellow]"+str(Counter)+".    ", end="")
            if user != Username:
                console.print(user, style="bold")
            else:
                console.print("You", style="bold")
            Counter += 1
    else:
        console.print("You Have no Following!", style="bold green")
    console.print("Press Enter to go back to Profile", style="bold yellow")
    k = keyboard.wait("enter")
