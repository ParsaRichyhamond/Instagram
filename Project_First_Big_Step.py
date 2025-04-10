import rich
import time
import os
import keyboard
import copy
from rich.console import Console
from rich.table import Table
console = Console()
#os.remove("Data.txt")
#f = open("Data.txt" , "x")

def Timer(t,color) :
    for i in range(int(t)) :
        console.print("[bold "+color+"]"+str(i+1) , end="\r")
        time.sleep(1)

def color(x,color) :
    console.print("[bold "+color+"]"+str(x),end="")

def Valid_email(Email) :
    return True

def biography() :
    Bio = ""
    Bol = False
    list = []
    while len(Bio) < 20 :
        print("",end="\r")
        console.print(f"Add biography(less than {20-len(Bio)} characters): " , style="bold blue" , end="")
        console.print(Bio+" " , end="")
        time.sleep(0.25)
        In = keyboard.read_key()
        list.append(In)
        if len(Bio) > 1 :
            if list[len(Bio)-1] == list[len(Bio)] :
                time.sleep(0.25)
        if In == "backspace" :
            Bio = Bio[:-1]
        elif In == "space" :
            Bio += " "
        elif In == "shift" :
            Bol = True
        elif Bol :
            Bio += In.capitalize()
            Bol = False
        elif In == "caps lock" :
            pass
        elif In == "enter" :
            break
        else :
            Bio += In
    return Bio

def Registeration() :
    os.system('cls')
    f = open("Data.txt" , "r")
    Y = f.read()
    if Y == "" :
        Dict_of_all_Data = {}
    else :
        Dict_of_all_Data = eval(Y)
    f.close()
    Profile = {}
    while True :    #_getting Username
        console.print("Enter Your Username: " , style="bold blue" , end="")
        Username = input()
        bol = True
        for key in Dict_of_all_Data.keys() :
            if Username == key :
                bol = False
                break
        if bol :
            Profile["Username"] = Username
            break
        else :
            console.print("Error: Username already Exists " , style="bold yellow" )
            time.sleep(2)
    
    console.print("Do You want your Acount to be privet?" , style="bold green" , end="")
    console.print("[Y/N]" , style="bold blue" , end="")
    Acount_type = input()
    if Acount_type == "Y" :
      Profile["Privet"] = True
    else :
        Profile["Privet"] = False

    while True:    #_getting email
        console.print("Enter Your Email address: " , style="bold blue" , end="")
        Email = input()
        if Valid_email(Email) :
            bol = True
            for dict in Dict_of_all_Data.values() :
                if "Email" in dict.keys() :
                    if dict["Email"] == Email :
                        bol = False
                        break
            if bol :
                Profile["Email"] = Email
                break
            else :
                console.print("Error: Email address already Exists " , style="bold yellow")
                time.sleep(2)             
        else :
            console.print("Error: Unvalid Email address " , style="bold red" , end="")
            time.sleep(2)
            
    while True :    #_getting password
        console.print("Enter Your Password: " , style="bold yellow" , end="")
        password1 = input()
        console.print("Enter Your Password again: " , style="bold yellow" , end="")
        password2 = input()
        if password1 == password2 :
            Profile["Password"] = password1
            break
        else :
            console.print("Error: Your two passwords do not match " , style="bold red")
            time.sleep(2)

    Bio = biography()
 
    Dict_of_all_Data[Profile["Username"]] = {"Email": Profile["Email"] , "Password": Profile["Password"] , "Biography": Bio , "Privet": Profile["Privet"], "Block_list": [] , "Posts": [] , "Followers": [] , "Following": []}
    f = open("Data.txt" , "w")
    f.write(str(Dict_of_all_Data))
    f.close() 
    os.system('cls')
        
def Login() :
    os.system('cls')
    f = open("Data.txt" , "r")
    Y = f.read()
    if Y == "" :
        Dict_of_all_Data = {}
    else :
        Dict_of_all_Data = eval(Y)
    f.close()
    
    Profile = {}
    while True :
        console.print("Enter Your Username: " , style="bold blue" , end="")
        Username = input()
        if Username not in Dict_of_all_Data.keys():
            console.print("Error: Username not found " , style="bold red")
            time.sleep(2)
        else :
            break
#_________________Getting Password from the user___________________________________________________________________
    attempts = 0
    bool = True
    counter = 1
    while bool :
        while (attempts < 3*counter) and bool:
            console.print(f"Enter Your Password(Your {attempts+1} th attempt): " , style="bold yellow" , end="")
            Password = input()
            if Password != Dict_of_all_Data[Username]["Password"] :
                console.print("Error: Password incorect " , style="bold red")
                time.sleep(1)
                attempts += 1
            else :
                bool = False
        timer = 60*counter
        while (timer > 0 ) and bool :
            console.print("You failed 3 times, please wait for " , style="bold yellow" , end="")
            console.print(timer , style="bold blue" , end="")
            console.print(" seconds then try again" , style="bold yellow" , end="")
            timer -= 1
            time.sleep(1)
            print("",end="\r")
        print("                                                                 ",end="\r")
        counter+=1
    return Username

def Profile(Username) :
    f = open("Data.txt" , "r")
    Y = f.read()
    if Y == "" :
        Dict_of_all_Data = {}
    else :
        Dict_of_all_Data = eval(Y)
    f.close()
    while True  :
        os.system('cls')
        console.print("Profile" , style="bold blue")
        console.print("[bold yellow]1.    " , end="")
        console.print(Username , style="bold")
        console.print("[bold yellow]2.    " , end="")
        console.print(Dict_of_all_Data[Username]["Email"] , style="bold")
        console.print("[bold yellow]3.    " , end="")
        console.print("Biography: " , style="bold" , end="")
        console.print(Dict_of_all_Data[Username]["Biography"] , style="bold red")
        console.print("[bold yellow]4.    " , end="")
        console.print("Acount type: " , style="bold" , end="")
        if Dict_of_all_Data[Username]["Privet"] :
            console.print("Private", style="bold" , end="")
            console.print("(Chose to change to Public)", style="bold blue")
        else :
            console.print("Public", style="bold" , end="")
            console.print("(Chose to change to Private)", style="bold blue")
        console.print("[bold yellow]5.    " , end="")
        console.print("Your Followers: ", style="bold green" ,end="")
        console.print(str(len(Dict_of_all_Data[Username]["Followers"])), style="bold blue")
        console.print("[bold yellow]6.    " , end="")
        console.print("Your Following: ", style="bold green" ,end="")
        console.print(str(len(Dict_of_all_Data[Username]["Following"])), style="bold blue")
        console.print("[bold yellow]7.    " , end="")
        console.print("Blocked Users: " , style="bold" , end="")
        console.print(str(len(Dict_of_all_Data[Username]["Block_list"])), style="bold blue")
        console.print("[bold yellow]8.    " , end="")
        console.print("Back to Home Page" , style="bold")
        console.print("Enter Your choice to Edit Information" , style="bold" , end="")
        console.print("[1/2/3/4/5/6/7/8]: " , style="bold blue" , end="")
        In = input()
        if In == "1" :
            console.print("Enter Username: " , style="bold yellow" , end="")
            Newusername = input()
            bol = True
            for key in Dict_of_all_Data.keys() :
                if Newusername == key :
                    bol = False
                    break
            if bol :
                console.print("Are You sure You wanna change Your Usrename to " , style="bold blue" , end="")
                console.print(Newusername , style="bold yellow" , end="")
                console.print(" ?" , style="bold blue" , end="")
                console.print("[Y/N]" , style="bold red" , end="")
                B = input()
                if B == "Y" :
                    if Username != Newusername :
                        Dict_of_all_Data[Newusername] = copy.copy(Dict_of_all_Data[Username])
                        Dict_of_all_Data.pop(Username)
                        Username = Newusername
                    console.print("Username changed successfully!" , style="bold red" , end="")
                    time.sleep(2)
                else :
                    console.print("OK Fine!" , style="bold Yellow" , end="")
                    time.sleep(2)
            else :
                console.print("Error: Username already Exists " , style="bold red" )
                time.sleep(2)

        elif In == "2" :
            console.print("Enter Email address: " , style="bold yellow" , end="")
            NewEmail = input()
            if Valid_email(NewEmail)  :
                bol = True
                for dict in Dict_of_all_Data.values() :
                    if "Email" in dict.keys() :
                        if dict["Email"] == NewEmail :
                            bol = False
                            break
                if bol :
                    console.print("Are You sure You wanna change Your Email address to " , style="bold blue" , end="")
                    console.print(NewEmail , style="bold yellow" , end="")
                    console.print(" ?" , style="bold blue" , end="")
                    console.print("[Y/N]" , style="bold red" , end="")
                    B = input()
                    if B == "Y" :
                        if Dict_of_all_Data[Username]["Email"] != NewEmail :
                            Dict_of_all_Data[Username]["Email"] = NewEmail
                        console.print("Email address changed successfully!" , style="bold red" , end="")
                        time.sleep(2)
                    else :
                        console.print("OK Fine!" , style="bold Yellow" , end="")
                        time.sleep(2)
                else:
                    console.print("Error: Email address already Exists " , style="bold red")
                    time.sleep(2)             
            else :
                console.print("Error: Unvalid Email address " , style="bold red" , end="")
                time.sleep(2)
                
        elif In == "3" :
            Bio = biography()
            print()
            console.print("Biography changed successfully!" , style="bold red" , end="")
            time.sleep(1.5)
            Dict_of_all_Data[Username]["Biography"] = Bio

        elif In == "4" :
            if Dict_of_all_Data[Username]["Privet"] :
                Dict_of_all_Data[Username]["Privet"] = False   
            else :
                Dict_of_all_Data[Username]["Privet"] = True
            console.print("Acount type changed successfully!" , style="bold green" , end="")
            time.sleep(1.5)
   
        elif In == "5" :
            os.system('cls')
            console.print("Your Followers" , style="bold blue")
            Counter = 1
            Len = len(Dict_of_all_Data[Username]["Followers"])
            if Len > 0 :
                for user in Dict_of_all_Data[Username]["Followers"] :
                    console.print("[bold yellow]"+str(Counter)+".    " , end="")
                    if user != Username :
                        console.print(user, style="bold")
                    else :
                        console.print("You", style="bold")
                    Counter += 1
            else :
                console.print("You Have no Followers!" , style="bold green")
            console.print("Press Enter to go back to Profile" , style="bold yellow")
            k = keyboard.wait("enter")
        
        elif In == "6" :
            os.system('cls')
            console.print("Your Followings" , style="bold blue")
            Counter = 1
            Len = len(Dict_of_all_Data[Username]["Following"])
            if Len > 0 :
                for user in Dict_of_all_Data[Username]["Following"] :
                    console.print("[bold yellow]"+str(Counter)+".    " , end="")
                    if user != Username :
                        console.print(user, style="bold")
                    else :
                        console.print("You", style="bold")
                    Counter += 1
            else :
                console.print("You Have no Following!" , style="bold green")
            console.print("Press Enter to go back to Profile" , style="bold yellow")
            k = keyboard.wait("enter")

        elif In == "7" :
            Blocked_Users(Username)
            f = open("Data.txt" , "r")
            Y = f.read()
            if Y == "" :
                Dict_of_all_Data = {}
            else :
                Dict_of_all_Data = eval(Y)
            f.close()
        elif In == "8" :
            break

        else :
            console.print("Error: Please check your input" , style="bold red")
            time.sleep(2)

        f = open("Data.txt" , "w")
        f.write(str(Dict_of_all_Data))
        f.close()  

def Blocked_Users(Username) :
    f = open("Data.txt" , "r")
    Y = f.read()
    if Y == "" :
        Dict_of_all_Data = {}
    else :
        Dict_of_all_Data = eval(Y)
    f.close()
    while True :
        os.system('cls')
        console.print("Blocked Users" , style="bold blue")
        counter = 1
        Len = len(Dict_of_all_Data[Username]["Block_list"])
        if Len > 0 :
            for blocked_user in Dict_of_all_Data[Username]["Block_list"] :
                console.print("[bold green]"+str(counter)+".    " , end="")
                console.print(blocked_user , style="bold red")
                counter += 1
            console.print("Enter a number to Unblock User or 'B' to go back to Profile" , style="bold", end="")
            string = "["
            for i in range(1,Len) :
                string += str(i)+"/"
            string += (str(Len)+"/B]:")
            console.print(string , style="bold blue", end="")
            boool = True
            In = input()
            for i in range(1,Len+1) :
                if str(i) == In :
                    boool = False
                    console.print("User "+Dict_of_all_Data[Username]["Block_list"][i-1]+" unblocked successfully!" , style="bold green")
                    Dict_of_all_Data[Username]["Block_list"].remove(Dict_of_all_Data[Username]["Block_list"][i-1])
                    f = open("Data.txt" , "w")
                    f.write(str(Dict_of_all_Data))
                    f.close()  
                    break
            if boool :
                break
        else :
            console.print("You have not Blocked any one!" , style="bold yellow")
            time.sleep(1)
            console.print("Press Enter to go back to Profile" , style="bold")
            k = keyboard.wait("enter")
            break

def Posts(Username) :
    pass

def Stories(Username) :
    pass

def Massages(Username) :
    pass

def Search_Users(Username) :
    f = open("Data.txt" , "r")
    Y = f.read()
    if Y == "" :
        Dict_of_all_Data = {}
    else :
        Dict_of_all_Data = eval(Y)
    f.close()
    while True :
        os.system('cls')
        console.print("Search Username" , style="bold blue")
        console.print("[bold yellow]1.    " , end="")
        console.print("Find a Username" , style="bold")
        console.print("[bold yellow]2.    " , end="")
        console.print("Back to Home page" , style="bold")
        console.print("Enter Your choice" , style="bold" , end="")
        console.print("[1/2]:" , style="bold blue" , end="")
        In = input()
        if In == "1" :
            console.print("Enter Username: " , style="bold yellow" , end="")
            username = input()
            if (username in Dict_of_all_Data.keys()) and (username not in Dict_of_all_Data[Username]["Block_list"]) and (not Dict_of_all_Data[username]["Privet"]) :
                while True :
                    os.system('cls')
                    console.print("[bold yellow]1.    " , end="")
                    console.print("Username: ", style="bold green" ,end="")
                    console.print(username, style="bold blue")
                    console.print("[bold yellow]2.    " , end="")
                    console.print("Email: ", style="bold green" ,end="")
                    console.print(Dict_of_all_Data[username]["Email"], style="bold")
                    console.print("[bold yellow]3.    " , end="")
                    console.print("Biography ", style="bold green" ,end="")
                    console.print(Dict_of_all_Data[username]["Biography"], style="bold red")
                    console.print("[bold yellow]4.    " , end="")
                    console.print("Followers: ", style="bold green" ,end="")
                    console.print(str(len(Dict_of_all_Data[username]["Followers"])), style="bold blue")
                    console.print("[bold yellow]5.    " , end="")
                    console.print("Following: ", style="bold green" ,end="")
                    console.print(str(len(Dict_of_all_Data[username]["Following"])), style="bold blue")
                    console.print("[bold yellow]6.    " , end="")
                    console.print("Follow ", style="bold green" , end="")
                    console.print(username, style="bold red")
                    console.print("[bold yellow]7.    " , end="")
                    console.print("Unfollow ", style="bold green" , end="") 
                    console.print(username, style="bold red")
                    console.print("[bold yellow]8.    " , end="")
                    console.print("View Posts", style="bold green")
                    console.print("[bold yellow]9.    " , end="")
                    console.print("Block User", style="bold red") 
                    console.print("[bold yellow]10.   " , end="")
                    console.print("Back", style="bold green")
                    console.print("Enter Your choice" , style="bold" , end="")
                    console.print("[4/5/6/7/8/9/10]:" , style="bold blue" , end="")    
                    In = input() 
                    if In == "4" :
                        os.system('cls')
                        console.print("Followers" , style="bold blue")
                        Counter = 1
                        Len = len( Dict_of_all_Data[username]["Followers"])
                        if Len > 0 :
                            for user in Dict_of_all_Data[username]["Followers"] :
                                console.print("[bold yellow]"+str(Counter)+".    " , end="")
                                if user != Username :
                                    console.print(user, style="bold")
                                else :
                                    console.print("You", style="bold")
                                Counter += 1
                        else :
                            console.print("User Has no Followers" , style="bold green")
                        console.print("Press Enter to go back to User's Profile" , style="bold yellow")
                        k = keyboard.wait("enter")
                    elif In == "5" :
                        os.system('cls')
                        console.print("Following" , style="bold blue")
                        Counter = 1
                        Len = len( Dict_of_all_Data[username]["Following"])
                        if Len > 0 :
                            for user in Dict_of_all_Data[username]["Following"] :
                                console.print("[bold yellow]"+str(Counter)+".    " , end="")
                                if user != Username :
                                    console.print(user, style="bold")
                                else :
                                    console.print("You", style="bold")
                                Counter += 1
                        else :
                            console.print("User Has no Following" , style="bold green")
                        console.print("Press Enter to go back to User's Profile" , style="bold yellow")
                        k = keyboard.wait("enter")
                    elif In == "6" :
                        if Username not in Dict_of_all_Data[username]["Followers"] :
                            Dict_of_all_Data[username]["Followers"].append(Username)
                            Dict_of_all_Data[Username]["Following"].append(username)
                            f = open("Data.txt" , "w")
                            f.write(str(Dict_of_all_Data))
                            f.close()  
                            console.print("You followed "+username+"!" , style="bold green")
                            time.sleep(2)
                        else :
                            console.print("You have already followed "+username+"!" , style="bold green")
                            time.sleep(2)
                    elif In == "7" :
                        if username in Dict_of_all_Data[Username]["Following"] :
                            Dict_of_all_Data[username]["Followers"].remove(Username)
                            Dict_of_all_Data[Username]["Following"].remove(username)
                            f = open("Data.txt" , "w")
                            f.write(str(Dict_of_all_Data))
                            f.close()  
                            console.print("You Unfollowed "+username+"!" , style="bold green")
                            time.sleep(2)
                        else :
                            console.print("You have not followed "+username+" yet!" , style="bold green")
                            time.sleep(2)
                    
                    elif In == "9" :
                        if username not in Dict_of_all_Data[Username]["Block_list"] :
                            Dict_of_all_Data[Username]["Block_list"].append(username)
                            f = open("Data.txt" , "w")
                            f.write(str(Dict_of_all_Data))
                            f.close()  
                            console.print("You Blocked "+username+"!" , style="bold red")
                            time.sleep(1.5)
                        else :
                            console.print("You have already Blocked "+username+"!" , style="bold green")
                            time.sleep(2)

                    elif In == "10" :
                        break

                    else :
                        console.print("Error: Please check your input" , style="bold red")
                        time.sleep(2)

            elif username in Dict_of_all_Data[Username]["Block_list"] :
                console.print("You have blocked "+username, style="bold red" , end="")
                time.sleep(2)

            else :
                console.print("Error: Username not found", style="bold red" , end="")
                time.sleep(1.5)
        elif In == "2" :
            break
    
def Home_page(Username) :
    Bool = True
    while Bool:
        os.system('cls')
        console.print("Home Page" , style="bold blue")
        console.print("[bold yellow]1.    " , end="")
        console.print("Posts" , style="bold")
        console.print("[bold yellow]2.    " , end="")
        console.print("Stories" , style="bold")
        console.print("[bold yellow]3.    " , end="")
        console.print("Massages" , style="bold")
        console.print("[bold yellow]4.    " , end="")
        console.print("Profile" , style="bold")
        console.print("[bold yellow]5.    " , end="")
        console.print("Search Users" , style="bold")
        console.print("[bold yellow]6.    " , end="")
        console.print("Exit" , style="bold")
        console.print("Enter Your choice" , style="bold" , end="")
        console.print("[1/2/3/4/5]:" , style="bold blue" , end="")
        In = input()
        if In == "1" :
            Posts(Username)
        elif In == "2" :
            Stories(Username)
        elif In == "3" :
            Massages(Username)
        elif In == "4" :
            Profile(Username)
        elif In == "5" :
            Search_Users(Username)
        elif In == "6" :
            os.system('cls')
            Bool = False
        else :
            console.print("Error: Please check your input" , style="bold red")
            time.sleep(2)
    
def main() :
    while True :
        os.system('cls')
        console.print("Welcome to Instagram!" , style="bold blue")
        time.sleep(0.5)
        console.print("[bold yellow]1.    " , end="")
        console.print("Registration" , style="bold")
        console.print("[bold yellow]2.    " , end="")
        console.print("Login" , style="bold")
        console.print("Enter Your choice" , style="bold" , end="")
        console.print("[1/2]:" , style="bold blue" , end="")
        In = input()
        if In == "1" :
            Registeration()     
        elif In == "2" :
            Home_page(Login())
        else :
            console.print("Error: Please check your input" , style="bold red")
            time.sleep(0.75)
        
main()