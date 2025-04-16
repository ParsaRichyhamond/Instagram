def Requests(Username):
    f = open("Data.txt", "r")
    Y = f.read()
    if Y == "":
        Dict_of_all_Data = {}
    else:
        Dict_of_all_Data = eval(Y)
    f.close()
    while True:
        os.system('cls')
        console.print("Your Requests", style="bold blue")
        counter = 1
        Len = len(Dict_of_all_Data[Username]["Requests"])
        if Len > 0:
            for user in Dict_of_all_Data[Username]["Requests"]:
                console.print("[bold green]"+str(counter)+".    ", end="")
                console.print(user, style="bold cyan")
                counter += 1
            console.print(
                "Enter number to Accept a Request or 'B' to go back to Profile", style="bold", end="")
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
                        "You accepted "+Dict_of_all_Data[Username]["Requests"][i-1]+"'s Request!", style="bold green")
                    time.sleep(1.5)
                    Dict_of_all_Data[Username]["Followers"].append(
                        Dict_of_all_Data[Username]["Requests"][i-1])
                    Dict_of_all_Data[Dict_of_all_Data[Username]
                                     ["Requests"][i-1]]["Following"].append(Username)
                    Dict_of_all_Data[Username]["Requests"].remove(
                        Dict_of_all_Data[Username]["Requests"][i-1])
                    f = open("Data.txt", "w")
                    f.write(str(Dict_of_all_Data))
                    f.close()
                    break
            if boool:
                break
        else:
            console.print("You do not have any Requests!", style="bold yellow")
            time.sleep(1)
            console.print("Press Enter to go back to Profile", style="bold")
            k = keyboard.wait("enter")
            break
