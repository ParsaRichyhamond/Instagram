def Blocked_Users(Username):
    f = open("Data.txt", "r")
    Y = f.read()
    if Y == "":
        Dict_of_all_Data = {}
    else:
        Dict_of_all_Data = eval(Y)
    f.close()
    while True:
        os.system('cls')
        console.print("Blocked Users", style="bold blue")
        counter = 1
        Len = len(Dict_of_all_Data[Username]["Block_list"])
        if Len > 0:
            for blocked_user in Dict_of_all_Data[Username]["Block_list"]:
                console.print("[bold green]"+str(counter)+".    ", end="")
                console.print(blocked_user, style="bold red")
                counter += 1
            console.print(
                "Enter a number to Unblock User or 'B' to go back to Profile", style="bold", end="")
            string = "["
            for i in range(1, Len):
                string += str(i)+"/"
            string += (str(Len)+"/B]:")
            console.print(string, style="bold blue", end="")
            boool = True
            In = input()
            for i in range(1, Len+1):
                if str(i) == In:
                    boool = False
                    console.print(
                        "User "+Dict_of_all_Data[Username]["Block_list"][i-1]+" unblocked successfully!", style="bold green")
                    Dict_of_all_Data[Username]["Block_list"].remove(
                        Dict_of_all_Data[Username]["Block_list"][i-1])
                    f = open("Data.txt", "w")
                    f.write(str(Dict_of_all_Data))
                    f.close()
                    break
            if boool:
                break
        else:
            console.print("You have not Blocked any one!", style="bold yellow")
            time.sleep(1)
            console.print("Press Enter to go back to Profile", style="bold")
            k = keyboard.wait("enter")
            break
