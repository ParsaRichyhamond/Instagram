import rich
import time
import os
import keyboard
import copy
from datetime import datetime
from rich.console import Console
from rich.table import Table
console = Console()
# os.remove("Data.txt")
# f = open("Data.txt" , "x")

# Parsa


def Timer(t, color):
    for i in range(int(t)):
        console.print("[bold "+color+"]"+str(i+1), end="\r")
        time.sleep(1)

# Parsa


def color(x, color):
    console.print("[bold "+color+"]"+str(x), end="")


# Mahdieh
def Valid_email(Email):
    if ((Email[-10:] == "@gmail.com") or (Email[-10:] == "@yahoo.com")) and len(Email) > 10:
        return True
    else:
        return False

# Parsa


def biography():
    Bio = ""
    Bol = False
    list = []
    while len(Bio) < 20:
        print("", end="\r")
        console.print(
            f"Add Biography(less than {20-len(Bio)} characters): ", style="bold blue", end="")
        console.print(Bio+" ", end="")
        time.sleep(0.25)
        In = keyboard.read_key()
        list.append(In)
        if len(Bio) > 1:
            if list[len(Bio)-1] == list[len(Bio)]:
                time.sleep(0.25)
        if In == "backspace":
            Bio = Bio[:-1]
        elif In == "space":
            Bio += " "
        elif In == "shift":
            Bol = True
        elif Bol:
            Bio += In.capitalize()
            Bol = False
        elif In == "caps lock":
            pass
        elif In == "enter":
            break
        else:
            Bio += In
    return Bio

# Parsa


def Registeration():
    os.system('cls')
    f = open("Data.txt", "r")
    Y = f.read()
    if Y == "":
        Dict_of_all_Data = {}
    else:
        Dict_of_all_Data = eval(Y)
    f.close()
    Profile = {}
    while True:  # _getting Username
        console.print("Enter Your Username: ", style="bold blue", end="")
        Username = input()
        bol = True
        for key in Dict_of_all_Data.keys():
            if Username == key:
                bol = False
                break
        if bol:
            Profile["Username"] = Username
            break
        else:
            console.print("Error: Username already Exists ",
                          style="bold yellow")
            time.sleep(2)

    console.print("Do You want your Account to be Private?",
                  style="bold green", end="")
    console.print("[Y/N]", style="bold blue", end="")
    Acount_type = input()
    if Acount_type == "Y":
        Profile["Privet"] = True
    else:
        Profile["Privet"] = False

    while True:  # _getting email
        console.print("Enter Your Email Address: ", style="bold blue", end="")
        Email = input()
        if Valid_email(Email):
            bol = True
            for dict in Dict_of_all_Data.values():
                if "Email" in dict.keys():
                    if dict["Email"] == Email:
                        bol = False
                        break
            if bol:
                Profile["Email"] = Email
                break
            else:
                console.print(
                    "Error: Email Address Already Exists ", style="bold yellow")
                time.sleep(1)
        else:
            console.print("Error: Unvalid Email Address ", style="bold red")
            time.sleep(1)

    while True:  # _getting password
        console.print("Enter Your Password: ", style="bold yellow", end="")
        password1 = input()
        console.print("Enter Your Password Again: ",
                      style="bold yellow", end="")
        password2 = input()
        if password1 == password2:
            Profile["Password"] = password1
            break
        else:
            console.print(
                "Error: Your Two Passwords Do Not Match ", style="bold red")
            time.sleep(1)

    Bio = biography()
    Dict_of_all_Data[Profile["Username"]] = {"Email": Profile["Email"], "Password": Profile["Password"], "Biography": Bio, "Privet": Profile["Privet"],
                                             "Block_list": [], "Posts": {"My_Posts": [], "Saved_Posts": []}, "Stories": [], "Followers": [], "Following": [], "Requests": [], "Chats": {"Groups": {}, "Personal": {}}, "Saved_Posts": [], "notifications": []}
    f = open("Data.txt", "w")
    f.write(str(Dict_of_all_Data))
    f.close()

# Parsa


def Login():
    f = open("Data.txt", "r")
    Y = f.read()
    if Y == "":
        Dict_of_all_Data = {}
    else:
        Dict_of_all_Data = eval(Y)
    f.close()
    Profile = {}
    bool = True
    while bool:
        os.system('cls')
        console.print("Login", style="bold blue")
        console.print("[bold yellow]1.    ", end="")
        console.print("Enter Username", style="bold")
        console.print("[bold yellow]2.    ", end="")
        console.print("Back to Welcome", style="bold")
        console.print("Enter Your Choice to Continue", style="bold", end="")
        console.print("[1/2]: ", style="bold blue", end="")
        In = input()
        if In == "1":
            console.print("Enter Your Username: ", style="bold blue", end="")
            Username = input()
            if Username not in Dict_of_all_Data.keys():
                console.print("Error: Username Not Found ", style="bold red")
                time.sleep(2)
            else:
                attempts = 0
                bool = True
                counter = 1
                while bool:
                    while (attempts < 3*counter) and bool:
                        console.print(
                            f"Enter Your Password(Your {attempts+1} th Attempt): ", style="bold yellow", end="")
                        Password = input()
                        if Password != Dict_of_all_Data[Username]["Password"]:
                            console.print(
                                "Error: Password is Incorrect ", style="bold red")
                            time.sleep(1)
                            attempts += 1
                        else:
                            bool = False
                        timer = 60*counter
                    while (timer > 0) and bool:
                        console.print(
                            "You Failed 3 Times, Please Wait For ", style="bold yellow", end="")
                        console.print(timer, style="bold blue", end="")
                        console.print(" Seconds then Try Again",
                                      style="bold yellow", end="")
                        timer -= 1
                        time.sleep(1)
                        print("", end="\r")
                    print(
                        "                                                                 ", end="\r")
                    counter += 1
                return Username
        elif In == "2":
            bool = False
            return None
        else:
            console.print("Error: Input is Invalid ", style="bold red")
            time.sleep(1)


# Mehraveh

def Profile(Username):
    f = open("Data.txt", "r")
    Y = f.read()
    if Y == "":
        Dict_of_all_Data = {}
    else:
        Dict_of_all_Data = eval(Y)
    f.close()
    while True:
        os.system('cls')
        console.print("Profile", style="bold blue")
        console.print("[bold yellow]1.    ", end="")
        console.print("Username: ", style="bold", end="")
        console.print(Username, style="bold green")
        console.print("[bold yellow]2.    ", end="")
        console.print("Email Address: ", style="bold", end="")
        console.print(Dict_of_all_Data[Username]["Email"], style="bold green")
        console.print("[bold yellow]3.    ", end="")
        console.print("Password: ", style="bold", end="")
        console.print(Dict_of_all_Data[Username]["Password"], style="bold")
        console.print("[bold yellow]4.    ", end="")
        console.print("Biography: ", style="bold", end="")
        console.print(Dict_of_all_Data[Username]
                      ["Biography"], style="bold red")
        console.print("[bold yellow]5.    ", end="")
        console.print("Account Type: ", style="bold", end="")
        if Dict_of_all_Data[Username]["Privet"]:
            console.print("Private", style="bold", end="")
            console.print("(Choose to Change to Public)", style="bold blue")
        else:
            console.print("Public", style="bold", end="")
            console.print("(Choose to Change to Private)", style="bold blue")
        console.print("[bold yellow]6.    ", end="")
        console.print("Followers: ", style="bold green", end="")
        console.print(
            str(len(Dict_of_all_Data[Username]["Followers"])), style="bold blue")
        console.print("[bold yellow]7.    ", end="")
        console.print("Followings: ", style="bold green", end="")
        console.print(
            str(len(Dict_of_all_Data[Username]["Following"])), style="bold blue")
        console.print("[bold yellow]8.    ", end="")
        console.print("Requests: ", style="bold green", end="")
        console.print(
            str(len(Dict_of_all_Data[Username]["Requests"])), style="bold blue")
        console.print("[bold yellow]9.    ", end="")
        console.print("Blocked Users: ", style="bold", end="")
        console.print(
            str(len(Dict_of_all_Data[Username]["Block_list"])), style="bold blue")
        console.print("[bold yellow]10.   ", end="")
        console.print(
            f"Check Notifications ({len(Dict_of_all_Data[Username]["notifications"])})", style="bold")
        console.print("[bold yellow]11.   ", end="")
        console.print("Back to Home Page", style="bold")
        console.print("Enter Your Choice to Edit Information",
                      style="bold", end="")
        console.print("[1/2/3/4/5/6/7/8/9/10/11]: ", style="bold blue", end="")
        In = input()
        if In == "1":
            console.print("Enter Your New Username: ",
                          style="bold yellow", end="")
            Newusername = input()
            bol = True
            for key in Dict_of_all_Data.keys():
                if Newusername == key:
                    bol = False

            if bol:
                console.print(
                    "Are You sure You Want to Change Your Username to ", style="bold blue", end="")
                console.print(Newusername, style="bold yellow", end="")
                console.print(" ?", style="bold blue", end="")
                console.print("[Y/N]", style="bold red", end="")
                B = input()
                if B == "Y":
                    if Username != Newusername:
                        Dict_of_all_Data[Newusername] = copy.copy(
                            Dict_of_all_Data[Username])
                        Dict_of_all_Data.pop(Username)
                        Username = Newusername
                    console.print("Username Changed Successfully!",
                                  style="bold red", end="")
                    time.sleep(1)
                else:
                    console.print("Username Did Not Change!",
                                  style="bold Yellow", end="")
                    time.sleep(1)
            else:
                console.print("Error: Username Already Exists",
                              style="bold red")
                time.sleep(1)

        elif In == "2":
            console.print("Enter Your New Email address: ",
                          style="bold yellow", end="")
            NewEmail = input()
            if Valid_email(NewEmail):
                bol = True
                for dict in Dict_of_all_Data.values():
                    if "Email" in dict.keys():
                        if dict["Email"] == NewEmail:
                            bol = False
                            break
                if bol:
                    console.print(
                        "Are You sure You Want to Change Your Email Address to ", style="bold blue", end="")
                    console.print(NewEmail, style="bold yellow", end="")
                    console.print(" ?", style="bold blue", end="")
                    console.print("[Y/N]", style="bold red", end="")
                    B = input()
                    if B == "Y":
                        if Dict_of_all_Data[Username]["Email"] != NewEmail:
                            Dict_of_all_Data[Username]["Email"] = NewEmail
                        console.print(
                            "Email Address Changed Successfully!", style="bold red", end="")
                        time.sleep(1)
                    else:
                        console.print("Email Address Did Not Change!",
                                      style="bold Yellow", end="")
                        time.sleep(1)
                else:
                    console.print(
                        "Error: Email address Already Exists ", style="bold red")
                    time.sleep(1)
            else:
                console.print("Error: Invalid Email Address ",
                              style="bold red", end="")
                time.sleep(1)

        elif In == "3":
            console.print("Enter Your New Password: ",
                          style="bold green", end="")
            password1 = input()
            console.print("Enter Your New Password Again: ",
                          style="bold green", end="")
            password2 = input()
            if password1 == password2:
                Dict_of_all_Data[Username]["Password"] = password1
                console.print("Password", style="bold yellow", end="")
                console.print("Password Changed successfully!",
                              style="bold green", end="")
                time.sleep(1)
            else:
                console.print(
                    "Error: Your Two Passwords Do Not Match ", style="bold red")
                time.sleep(1)

        elif In == "4":
            Bio = biography()
            print()
            console.print("Biography Changed Successfully!",
                          style="bold red", end="")
            time.sleep(1.5)
            Dict_of_all_Data[Username]["Biography"] = Bio

        elif In == "5":
            if Dict_of_all_Data[Username]["Privet"]:
                Dict_of_all_Data[Username]["Privet"] = False
            else:
                Dict_of_all_Data[Username]["Privet"] = True
            console.print("Account Type Changed Successfully!",
                          style="bold green", end="")
            time.sleep(1.5)

        elif In == "6":
            Followers(Username)

        elif In == "7":
            Following(Username)

        elif In == "8":
            Requests(Username)
            f = open("Data.txt", "r")
            Y = f.read()
            if Y == "":
                Dict_of_all_Data = {}
            else:
                Dict_of_all_Data = eval(Y)
            f.close()

        elif In == "9":
            Blocked_Users(Username)
            f = open("Data.txt", "r")
            Y = f.read()
            if Y == "":
                Dict_of_all_Data = {}
            else:
                Dict_of_all_Data = eval(Y)
            f.close()
        elif In == "10":
            if len(Dict_of_all_Data[Username]["notifications"]) > 0:
                for i in Dict_of_all_Data[Username]["notifications"]:
                    console.print(i, style="bold green")
                Dict_of_all_Data[Username]["notifications"] = []
                Inp3 = input()

            else:
                console.print("You Have No Notifications", style="bold red")
                time.sleep(1)
        elif In == "11":
            break

        else:
            console.print("Error: Please Enter a Valid Input!",
                          style="bold red")
            time.sleep(1)

        f = open("Data.txt", "w")
        f.write(str(Dict_of_all_Data))
        f.close()

# Parsa


def Followers(Username):
    os.system('cls')
    f = open("Data.txt", "r")
    Y = f.read()
    if Y == "":
        Dict_of_all_Data = {}
    else:
        Dict_of_all_Data = eval(Y)
    f.close()
    console.print("Your Followers", style="bold blue")
    Counter = 1
    Len = len(Dict_of_all_Data[Username]["Followers"])
    if Len > 0:
        for user in Dict_of_all_Data[Username]["Followers"]:
            console.print("[bold yellow]"+str(Counter)+".    ", end="")
            if user != Username:
                console.print(user, style="bold")
            else:
                console.print("You", style="bold")
            Counter += 1
    else:
        console.print("You Have no Followers!", style="bold green")
    console.print("Press Enter to go back to Profile", style="bold yellow")
    k = keyboard.wait("enter")

# Parsa


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


# Mehraveh
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
                    console.print("[bold green]"+str(counter)+".", end="")
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
                    console.print("[bold green]"+str(counter)+".", end="")
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
# Mehraveh


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


# Mahdieh

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


# Mahdieh
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


# Mehraveh
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
        console.print("Enter Your Choice", style="bold", end="")
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
                        "Enter a Number to View Posts' Details, 'C' to Creat a Post or 'B' to Go Back to Posts' Menu:", style="bold", end="")
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
                        console.print("What Do You Want to Share as a Post: ",
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
                        console.print("Error: Please Enter a Valid Input!",
                                      style="bold red")
                        time.sleep(1)

                else:
                    console.print(
                        "You have No Posts yet, Enter 'C' to Creat a Post or 'B' to Go Back to Posts:", style="bold", end="")
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
                        console.print("Error: Please Enter a Valid Input!",
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
                        "Enter a Number to view User's Posts or 'B' to Go Back to Posts' Menu:", style="bold", end="")
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
                                    "Enter a Number to View Posts' Details or 'B' to Go Back to Posts' Menu:", style="bold", end="")
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
                        console.print("Error: Please Enter a Valid Input!",
                                      style="bold red")
                        time.sleep(1)

                else:
                    console.print(
                        "There are no posts for you :(", style="bold cyan")
                    time.sleep(2)
                    break
        elif In == "3":
            break


# n is the index of the post in 'Post' section of key Username
# Mehraveh
def Post_Details(Username, username, n):
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
            Dict_of_all_Data[username]["Posts"]["My_Posts"][n]["Liked_list"])
        if username == Username:
            console.print("You", style="bold blue")
        else:
            console.print(username, style="bold blue")
        console.print(50*"=", style="bold red")
        console.print(Dict_of_all_Data[username]["Posts"]
                      ["My_Posts"][n]["Content"], style="bold")
        console.print(50*"=", style="bold red")
        console.print("[bold yellow]1.    ", end="")
        console.print("Liked by "+str(number_of_likes)+" Users", style="bold")
        console.print("[bold yellow]2.    ", end="")
        console.print("Comments", style="bold")
        console.print("[bold yellow]3.    ", end="")
        console.print("Save this Post", style="bold")
        console.print("[bold yellow]4.    ", end="")
        console.print("Forward to someone", style="bold")
        console.print("[bold yellow]5.    ", end="")
        console.print("Tag someone", style="bold")
        console.print("[bold yellow]6.    ", end="")
        console.print("Back", style="bold yellow")
        console.print("Enter Your choice", style="bold", end="")
        console.print("[1/2/3/4/5/6]:", style="bold blue", end="")
        In = input()
        if In == "1":
            os.system('cls')
            console.print(50*"=", style="bold red")
            console.print(
                Dict_of_all_Data[username]["Posts"]["My_Posts"][n]["Content"], style="bold")
            console.print(50*"=", style="bold red")
            if number_of_likes > 0:
                for o in range(0, number_of_likes):
                    console.print("[bold yellow]"+str(o+1)+". ", end="")
                    user = Dict_of_all_Data[username]["Posts"]["My_Posts"][n]["Liked_list"][o]
                    if user == Username:
                        console.print("You", style="bold green")
                    else:
                        console.print(user, style="bold")
                console.print(
                    "Enter 'L' to like the Post or 'B' to go back to View Post:", style="bold orange4", end="")
                Inp1 = input()
                if Inp1 == "L":
                    if Username not in Dict_of_all_Data[username]["Posts"]["My_Posts"][n]["Liked_list"]:
                        Dict_of_all_Data[username]["Posts"]["My_Posts"][n]["Liked_list"].append(
                            Username)
                        console.print("You liked this post!",
                                      style="bold sea_green3", end="")
                        time.sleep(1)
                    else:
                        console.print(
                            "You Have Already Liked this Post!", style="bold sea_green3", end="")
                        time.sleep(1)

            else:
                console.print("No One Has Liked this Post,",
                              style="bold green", end="")
                console.print(
                    " Enter 'L' to Like or 'B' to Go Back to Posts' Details:", style="bold blue_violet", end="")
                Inp = input()
                if Inp == "L":
                    if Username not in Dict_of_all_Data[username]["Posts"]["My_Posts"][n]["Liked_list"]:
                        Dict_of_all_Data[username]["Posts"]["My_Posts"][n]["Liked_list"].append(
                            Username)
                        console.print("You Liked this Post!",
                                      style="bold sea_green3", end="")
                        time.sleep(1)
                    else:
                        console.print(
                            "You Have Already Liked this Post!", style="bold sea_green3", end="")
                        time.sleep(1)
                elif Inp == "B":
                    break
                else:
                    console.print(
                        "Error: Please Enter a Valid Input!", style="bold red")
                    time.sleep(1)

        elif In == "2":
            while True:
                os.system('cls')
                console.print(50*"=", style="bold red")
                console.print(
                    Dict_of_all_Data[username]["Posts"]["My_Posts"][n]["Content"], style="bold")
                console.print(50*"=", style="bold red")
                List_of_comments = Dict_of_all_Data[username]["Posts"]["My_Posts"][n]["Comments"]
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
                        "Enter 'C' to Add a Comment or 'B' to Go Back to Posts' Details:", style="bold blue_violet", end="")
                    Inp1 = input()
                    if Inp1 == "C":
                        console.print("Type Your Comment:",
                                      style="bold green", end="")
                        comment = input()
                        Dict_of_all_Data[username]["Posts"]["My_Posts"][n]["Comments"].append([
                                                                                              Username, comment])
                    elif Inp1 == "B":
                        break
                    else:
                        console.print("Error: Please Enter a Valid Input!",
                                      style="bold red")
                        time.sleep(0.5)

                else:
                    console.print(
                        "There Are No Comments for this Post,", style="bold green", end="")
                    console.print(
                        " Enter 'C' to Add a Comment or 'B' to Go Back to Post Details:", style="bold blue_violet", end="")
                    Inp = input()
                    if Inp == "C":
                        console.print("Type Your Comment:",
                                      style="bold wheat4", end="")
                        comment = input()
                        Dict_of_all_Data[username]["Posts"]["My_Posts"][n]["Comments"].append([
                                                                                              Username, comment])
                    elif Inp == "B":
                        break
                    else:
                        console.print("Error: Please Enter a Valid Input!",
                                      style="bold red")
                        time.sleep(1)
        elif In == "3":
            Dict_of_all_Data[Username]["Posts"]["Saved_Posts"].append(
                [username, Dict_of_all_Data[username]["Posts"]["My_Posts"][n]])
            console.print("Post is Saved !", style="bold sea_green3")
            time.sleep(1)
        elif In == "4":
            Forward_Post(Username, username,
                         Dict_of_all_Data[username]["Posts"]["My_Posts"][n])
            f = open("Data.txt", "r")
            Y = f.read()
            if Y == "":
                Dict_of_all_Data = {}
            else:
                Dict_of_all_Data = eval(Y)
            f.close()
        elif In == "6":
            break
        elif In == "5":
            if len(Dict_of_all_Data[Username]["Following"]) > 0:
                for i, k in enumerate(Dict_of_all_Data[Username]["Following"]):
                    console.print(f"{i}.{k}", style="bold blue")
                chose = input("Choose who to tag by their index: ")
                try:
                    tagged = Dict_of_all_Data[Username]["Following"][int(
                        chose)]
                    console.print(
                        f"{tagged} Has been tagged ", style="bold green")
                    Dict_of_all_Data[tagged]["notifications"].append(
                        f"{Username} tagged you in: {Dict_of_all_Data[username]["Posts"]["My_Posts"][n]["Content"]} by {username}")
                    Inp3 = input()
                except:
                    console.print("Error: Check your input", style="bold red")
                    time.sleep(1)
            else:
                console.print("You Don't Have Anyone to Tag")
                time.sleep(2)

        else:
            console.print("Error: Please Enter a Valid Input!",
                          style="bold red")
            time.sleep(1)

        f = open("Data.txt", "w")
        f.write(str(Dict_of_all_Data))
        f.close()


# Mahdieh
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
        console.print("Error: Please Enter a Valid Input!", style="bold red")
        time.sleep(1)
    f = open("Data.txt", "w")
    f.write(str(Dict_of_all_Data))
    f.close()


# Mehraveh
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
                        "Enter a number to view users stories or 'B' to go back to Stories' menu:", style="bold", end="")
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
                                    "Enter a Number to View Stories' Details or 'B' to Go Back to Stories' Menu:", style="bold", end="")
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
                        console.print("Error: Please Enter a Valid Input!",
                                      style="bold red")
                        time.sleep(1)

                else:
                    console.print(
                        "There Are No Stories for You :(", style="bold cyan")
                    time.sleep(2)
                    break
        elif In == "3":
            break


# Mehraveh
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
                    console.print(f"{tagged} has been tagged ", style="bold")
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

# Mehraveh


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


# Mehraveh
def Search_Users(Username):
    f = open("Data.txt", "r")
    Y = f.read()
    if Y == "":
        Dict_of_all_Data = {}
    else:
        Dict_of_all_Data = eval(Y)
    f.close()
    while True:
        os.system('cls')
        console.print("Search Username", style="bold blue")
        console.print("[bold yellow]1.    ", end="")
        console.print("Find a Username", style="bold")
        console.print("[bold yellow]2.    ", end="")
        console.print("Back to Home page", style="bold")
        console.print("Enter Your choice", style="bold", end="")
        console.print("[1/2]:", style="bold blue", end="")
        In = input()
        if In == "1":
            console.print("Enter Username: ", style="bold yellow", end="")
            username = input()
            if username in Dict_of_all_Data.keys():
                if Username not in Dict_of_all_Data[username]["Block_list"]:
                    while True:
                        os.system('cls')
                        console.print("[bold yellow]1.    ", end="")
                        console.print("Username: ", style="bold green", end="")
                        console.print(username, style="bold blue")
                        console.print("[bold yellow]2.    ", end="")
                        console.print("Email: ", style="bold green", end="")
                        console.print(
                            Dict_of_all_Data[username]["Email"], style="bold")
                        console.print("[bold yellow]3.    ", end="")
                        console.print("Biography ", style="bold green", end="")
                        console.print(
                            Dict_of_all_Data[username]["Biography"], style="bold red")
                        console.print("[bold yellow]4.    ", end="")
                        console.print(
                            "Followers: ", style="bold green", end="")
                        console.print(
                            str(len(Dict_of_all_Data[username]["Followers"])), style="bold blue")
                        console.print("[bold yellow]5.    ", end="")
                        console.print(
                            "Following: ", style="bold green", end="")
                        console.print(
                            str(len(Dict_of_all_Data[username]["Following"])), style="bold blue")
                        console.print("[bold yellow]6.    ", end="")
                        if Dict_of_all_Data[username]["Privet"]:
                            console.print("Send a Request to ",
                                          style="bold green", end="")
                        else:
                            console.print(
                                "Follow ", style="bold green", end="")
                        console.print(username, style="bold red")
                        console.print("[bold yellow]7.    ", end="")
                        console.print("Unfollow ", style="bold green", end="")
                        console.print(username, style="bold red")
                        console.print("[bold yellow]8.    ", end="")
                        console.print("Block User", style="bold red")
                        console.print("[bold yellow]9.    ", end="")
                        console.print("Back", style="bold green")
                        console.print("Enter Your Choice",
                                      style="bold", end="")
                        console.print("[4/5/6/7/8/9]:",
                                      style="bold blue", end="")
                        In = input()
                        if In == "4":
                            os.system('cls')
                            console.print("Followers", style="bold blue")
                            Counter = 1
                            Len = len(Dict_of_all_Data[username]["Followers"])
                            if Len > 0:
                                for user in Dict_of_all_Data[username]["Followers"]:
                                    console.print(
                                        "[bold yellow]"+str(Counter)+".    ", end="")
                                    if user != Username:
                                        console.print(user, style="bold")
                                    else:
                                        console.print("You", style="bold")
                                    Counter += 1
                            else:
                                console.print(
                                    "User Has no Followers", style="bold green")
                            console.print(
                                "Press Enter to go back to User's Profile", style="bold yellow")
                            k = keyboard.wait("enter")

                        elif In == "5":
                            os.system('cls')
                            console.print("Following", style="bold blue")
                            Counter = 1
                            Len = len(Dict_of_all_Data[username]["Following"])
                            if Len > 0:
                                for user in Dict_of_all_Data[username]["Following"]:
                                    console.print(
                                        "[bold yellow]"+str(Counter)+".    ", end="")
                                    if user != Username:
                                        console.print(user, style="bold")
                                    else:
                                        console.print("You", style="bold")
                                    Counter += 1
                            else:
                                console.print(
                                    "User Has no Following", style="bold green")
                            console.print(
                                "Press Enter to go back to User's Profile", style="bold yellow")
                            k = keyboard.wait("enter")

                        elif In == "6":
                            if Dict_of_all_Data[username]["Privet"] and (Username not in Dict_of_all_Data[username]["Block_list"]) and (Username not in Dict_of_all_Data[username]["Followers"]):
                                if Username not in Dict_of_all_Data[username]["Requests"]:
                                    Dict_of_all_Data[username]["Requests"].append(
                                        Username)
                                    f = open("Data.txt", "w")
                                    f.write(str(Dict_of_all_Data))
                                    f.close()
                                    console.print(
                                        "Request is sent to "+username+"!", style="bold green")
                                    time.sleep(1)
                                else:
                                    console.print(
                                        "You Have Already Sent a Request to "+username+"!", style="bold green")
                                    time.sleep(1.5)
                            elif Username not in Dict_of_all_Data[username]["Block_list"]:
                                if Username not in Dict_of_all_Data[username]["Followers"]:
                                    Dict_of_all_Data[username]["Followers"].append(
                                        Username)
                                    Dict_of_all_Data[Username]["Following"].append(
                                        username)
                                    f = open("Data.txt", "w")
                                    f.write(str(Dict_of_all_Data))
                                    f.close()
                                    console.print(
                                        "You Followed "+username+"!", style="bold green")
                                    time.sleep(1)
                                else:
                                    console.print(
                                        "You Have Already Followed "+username+"!", style="bold green")
                                    time.sleep(1)
                            else:
                                console.print(
                                    "You Have Been Blocked by "+username+"!", style="bold red")
                                time.sleep(1)

                        elif In == "7":
                            if username in Dict_of_all_Data[Username]["Following"]:
                                Dict_of_all_Data[username]["Followers"].remove(
                                    Username)
                                Dict_of_all_Data[Username]["Following"].remove(
                                    username)
                                f = open("Data.txt", "w")
                                f.write(str(Dict_of_all_Data))
                                f.close()
                                console.print("You Unfollowed " +
                                              username+"!", style="bold green")
                                time.sleep(2)
                            else:
                                console.print(
                                    "You Have Not Followed "+username+" yet!", style="bold green")
                                time.sleep(1)

                        elif In == "8":
                            if username not in Dict_of_all_Data[Username]["Block_list"]:
                                Dict_of_all_Data[Username]["Block_list"].append(
                                    username)
                                if username in Dict_of_all_Data[Username]["Followers"]:
                                    Dict_of_all_Data[Username]["Followers"].remove(
                                        username)
                                    Dict_of_all_Data[username]["Following"].remove(
                                        Username)
                                f = open("Data.txt", "w")
                                f.write(str(Dict_of_all_Data))
                                f.close()
                                console.print("You Blocked " +
                                              username+"!", style="bold red")
                                time.sleep(1)
                            else:
                                console.print(
                                    "You Have Already Blocked "+username+"!", style="bold green")
                                time.sleep(1)

                        elif In == "9":
                            break

                        else:
                            console.print(
                                "Error: Please Enter a Valid Input!", style="bold red")
                            time.sleep(2)

                elif Username in Dict_of_all_Data[username]["Block_list"]:
                    console.print("You Have Been Blocked by " +
                                  username, style="bold red", end="")
                    time.sleep(1)

            else:
                console.print("Error: Username Not Found",
                              style="bold red", end="")
                time.sleep(1)
        elif In == "2":
            break


# Mahdieh
def Saved_Posts(Username):
    f = open("Data.txt", "r")
    Y = f.read()
    if Y == "":
        Dict_of_all_Data = {}
    else:
        Dict_of_all_Data = eval(Y)
    f.close()
    os.system('cls')
    console.print("Saved Posts", style="bold blue")
    Len = len(Dict_of_all_Data[Username]["Posts"]["Saved_Posts"])
    if Len > 0:
        for i in range(0, Len):
            console.print(50*"=", style="grey37")
            console.print(Dict_of_all_Data[Username]["Posts"]
                          ["Saved_Posts"][i][0], style="bold light_slate_grey")
            console.print(Dict_of_all_Data[Username]["Posts"]
                          ["Saved_Posts"][i][1]["Content"], style="bold plum2")
            console.print(50*"=", style="medium_purple4")
        console.print("Press any key to go back to Home Page:",
                      style="bold", end="")
        Input = input()
    else:
        console.print("You have no saved Posts", style="bold cyan")
        time.sleep(2)


# Mahdieh
def Forward_Post(Username, username, post):
    f = open("Data.txt", "r")
    Y = f.read()
    if Y == "":
        Dict_of_all_Data = {}
    else:
        Dict_of_all_Data = eval(Y)
    f.close()
    while True:
        os.system('cls')
        console.print("Forward Post", style="bold blue")
        console.print(
            "Enter 'P' to forward to Personal Chat or 'G' for Group Chat or 'B' to go back: ", style="bold", end="")
        Choice = input()
        content = "\n"+"***********[Forwarded Post form "+username + \
            "] ***********\n"+50*"="+"\n"+post["Content"]+"\n"+50*"="
        if Choice == "P":
            console.print("Enter username to forward the post to: ",
                          style="bold green", end="")
            to_user = input()
            if to_user in Dict_of_all_Data.keys():
                if to_user in Dict_of_all_Data[Username]["Following"]:
                    if to_user not in Dict_of_all_Data[Username]["Chats"]["Personal"]:
                        Dict_of_all_Data[Username]["Chats"]["Personal"][to_user] = [
                            0]
                        Dict_of_all_Data[to_user]["Chats"]["Personal"][Username] = [
                            0]
                    now = datetime.now()
                    Massage = "[" + str(now)[:19] + "]"
                    Dict_of_all_Data[Username]["Chats"]["Personal"][to_user].append(
                        (Username, (Massage, content)))
                    Dict_of_all_Data[to_user]["Chats"]["Personal"][Username].append(
                        (Username, (Massage, content)))
                    Dict_of_all_Data[to_user]["Chats"]["Personal"][Username][0] += 1
                    console.print("Post forwarded successfully to " +
                                  to_user+"!", style="bold green")
                else:
                    console.print("You have to follow "+to_user +
                                  " first!", style="bold yellow")
            else:
                console.print("Error: Username does not exist",
                              style="bold red")
            time.sleep(1)

        elif Choice == "G":
            console.print("Enter group name to forward the post to: ",
                          style="bold green", end="")
            group_name = input()
            if group_name in Dict_of_all_Data[Username]["Chats"]["Groups"]:
                members = Dict_of_all_Data[Username]["Chats"]["Groups"][group_name][1]
                now = datetime.now()
                Massage = "[" + str(now)[:19] + "]"
                for user in members:
                    Dict_of_all_Data[user]["Chats"]["Groups"][group_name].append(
                        (Username, (Massage, content)))
                    Dict_of_all_Data[user]["Chats"]["Groups"][group_name][0] += 1
                Dict_of_all_Data[Username]["Chats"]["Groups"][group_name][0] -= 1
                console.print("Post forwarded to group " +
                              group_name+" successfully!", style="bold green")
                time.sleep(1)
            else:
                console.print("Error: Group does not exist", style="bold red")
                time.sleep(1)

        elif Choice == "B":
            break
        else:
            console.print("Error: Please check your input", style="bold red")
            time.sleep(1)

        f = open("Data.txt", "w")
        f.write(str(Dict_of_all_Data))
        f.close()

# Parsa


def Home_page(Username):
    f = open("Data.txt", "r")
    Y = f.read()
    if Y == "":
        Dict_of_all_Data = {}
    else:
        Dict_of_all_Data = eval(Y)
    f.close()
    Bool = True
    while Bool:
        os.system('cls')
        console.print("Home Page", style="bold blue")
        console.print("[bold yellow]1.    ", end="")
        console.print("Posts", style="bold")
        console.print("[bold yellow]2.    ", end="")
        console.print("Stories", style="bold")
        console.print("[bold yellow]3.    ", end="")
        console.print("Chats", style="bold")
        console.print("[bold yellow]4.    ", end="")
        console.print("Profile", style="bold")
        console.print("[bold yellow]5.    ", end="")
        console.print("Search Users", style="bold")
        console.print("[bold yellow]6.    ", end="")
        console.print("Saved Posts", style="bold")
        console.print("[bold yellow]7.    ", end="")
        console.print("Delete Account", style="bold")
        console.print("[bold yellow]8.    ", end="")
        console.print("Exit", style="bold")
        console.print("Enter Your choice", style="bold", end="")
        console.print("[1/2/3/4/5/6/7]:", style="bold blue", end="")
        In = input()
        if In == "1":
            Posts(Username)
        elif In == "2":
            Stories(Username)
        elif In == "3":
            Chats(Username)
            f = open("Data.txt", "r")
            Y = f.read()
            if Y == "":
                Dict_of_all_Data = {}
            else:
                Dict_of_all_Data = eval(Y)
            f.close()
        elif In == "4":
            Profile(Username)
        elif In == "5":
            Search_Users(Username)
        elif In == "6":
            Saved_Posts(Username)
        elif In == "7":
            STRING = str(Dict_of_all_Data)
            STRING = STRING.replace(Username, "Deleted Account")
            f = open("Data.txt", "w")
            f.write(STRING)
            f.close()
            console.print("Account deleted :(", style="bold red")
            time.sleep(1.5)
            break
        elif In == "8":
            os.system('cls')
            Bool = False
        else:
            console.print("Error: Please check your input", style="bold red")
            time.sleep(1.5)

# Parsa


def main():
    while True:
        os.system('cls')
        console.print("Welcome to Instagram!", style="bold blue")
        time.sleep(0.2)
        console.print("[bold yellow]1.    ", end="")
        console.print("Registration", style="bold")
        console.print("[bold yellow]2.    ", end="")
        console.print("Login", style="bold")
        console.print("[bold yellow]3.    ", end="")
        console.print("Exit", style="bold red")
        console.print("Enter Your choice", style="bold", end="")
        console.print("[1/2/3]:", style="bold blue", end="")
        In = input()
        if In == "1":
            Registeration()
        elif In == "2":
            A = Login()
            if A != None:
                Home_page(A)
        elif In == "3":
            os.system('cls')
            break
        else:
            console.print("Error: Please check your input", style="bold red")
            time.sleep(0.5)


main()
