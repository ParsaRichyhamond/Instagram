def Open_Chat(Username, chat_name, Mood):
    Username2 = chat_name
    f = open("Data.txt", "r")
    Y = f.read()
    if Y == "":
        Dict_of_all_Data = {}
    else:
        Dict_of_all_Data = eval(Y)
    f.close()

    if Mood == "Personal":
        Dict_of_all_Data[Username]["Chats"]["Personal"][Username2][0] = 0
        List = Dict_of_all_Data[Username]["Chats"]["Personal"][Username2]
        List2 = Dict_of_all_Data[Username2]["Chats"]["Personal"][Username]
        while True:
            os.system('cls')
            console.print(Username2, style="bold blue")
            for tuple in List[1:]:
                console.print(tuple[1][0], style="bold green", end="")
                if tuple[0] == Username:
                    console.print("  You: ", style="bold green", end="")
                else:
                    console.print("  "+Username2+": ",
                                  style="bold yellow", end="")
                console.print(tuple[1][1], style="bold")
            console.print(
                "Enter 'T' for typeing or 'B' to go back to Personal chats: ", style="bold", end="")
            In = input()
            if In == "T":
                console.print("Type a massage: ", style="bold green", end="")
                string = input()
                now = datetime.now()
                Massage = "["+str(now)[:19]+"]"
                List.append((Username, (Massage, string)))
                List2.append((Username, (Massage, string)))
                Dict_of_all_Data[Username2]["Chats"]["Personal"][Username][0] += 1
            elif In == "B":
                break
            else:
                console.print("Error: Check your input ", style="bold red")
                time.sleep(0.75)

        f = open("Data.txt", "w")
        f.write(str(Dict_of_all_Data))
        f.close()

    else:
        Dict_of_all_Data[Username]["Chats"]["Groups"][chat_name][0] = 0
        while True:
            Massages = copy.copy(
                Dict_of_all_Data[Username]["Chats"]["Groups"][chat_name][2:])
            Members = copy.copy(
                Dict_of_all_Data[Username]["Chats"]["Groups"][chat_name][1])
            # List2.append(Username)
            os.system('cls')
            console.print(chat_name, style="bold blue")
            for tuple in Massages:
                if tuple[0] == Username:
                    console.print(tuple[1][0], style="bold green", end="")
                    console.print("  You: ", style="bold green", end="")
                    console.print(tuple[1][1], style="bold")
                else:
                    console.print(tuple[1][0], style="bold green", end="")
                    console.print("  "+tuple[0]+": ",
                                  style="bold yellow", end="")
                    console.print(tuple[1][1], style="bold")
            console.print(
                "Enter 'T' for typeing or 'B' to go back to Personal chats: ", style="bold", end="")
            In = input()
            if In == "T":
                console.print("Type a massage: ", style="bold green", end="")
                string = input()
                now = datetime.now()
                Massage = "["+str(now)[:19]+"]"
                for username in Members:
                    Dict_of_all_Data[username]["Chats"]["Groups"][chat_name].append(
                        (Username, (Massage, string)))
                    Dict_of_all_Data[username]["Chats"]["Groups"][chat_name][0] += 1
                Dict_of_all_Data[Username]["Chats"]["Groups"][chat_name][0] -= 1
                f = open("Data.txt", "w")
                f.write(str(Dict_of_all_Data))
                f.close()
            elif In == "B":
                break
            else:
                console.print("Error: Check your input ", style="bold red")
                time.sleep(0.75)

        f = open("Data.txt", "w")
        f.write(str(Dict_of_all_Data))
        f.close()
