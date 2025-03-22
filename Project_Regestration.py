import time
import os
#os.remove("Data.txt")
#f = open("Data.txt" , "x")                         #if this is the first time you are runnig this code,
#                                                    uncomment line 4 and then comment it again after the
#                                                    first run
def Registration() :
    f = open("Data.txt" , "r")
    Y = f.read()
    if Y == "" :
        Dict_of_all_Data = {}
    else :
        Dict_of_all_Data = eval(Y)
    f.close()
    print("Hi there New User!")
    time.sleep(2)
    print("How do you prefer for Registration?")
    time.sleep(2)
    print('Enter "E" for Email, "U" for Username and Password or "B" for both: ' , end="")
    number_of_current_users = len(Dict_of_all_Data)
    String = "User_"+str(number_of_current_users+1)
    X = input() 
    if X=="E" :
        print("Enter your Email address: " , end="")
        Email = input()
        B = True
        for x in Dict_of_all_Data.keys() :
            if Dict_of_all_Data[x]["Acount"]["Email address"] == Email :
                print("This Email address already exists, Try siging in")
                B = False
                break
        if B :
            Dict_of_all_Data[String] = {"Acount":
                                                {"Email address" : Email ,
                                                 "Username" : ""         ,
                                                 "Password" : ""}
                                        }  
    elif X=="U" :
        print("Enter your Username: " , end="")
        Username = input()
        B = True
        for x in Dict_of_all_Data.keys() :
            if Dict_of_all_Data[x]["Acount"]["Username"] == Username :
                print("This Username already exists, Try siging in")
                B = False
                break
        if B :
            while True :
                print("Enter your password: " , end="")
                P1 = input()
                print("Enter your password again: " , end="")
                P2 = input()
                if P1==P2 :
                    Dict_of_all_Data[String] = {"Acount":
                                                    {"Email address" : ""  ,
                                                     "Username" : Username ,
                                                     "Password" : P1}
                                                }  
                    break
                else :
                    print("Your two passwords do not match, Please try again!")
                    time.sleep(2)
    elif X=="B" :
        print("Enter your Email address: " , end="")
        Email = input()
        B1 = True
        for x in Dict_of_all_Data.keys() :
            if Dict_of_all_Data[x]["Acount"]["Email address"] == Email :
                print("This Email address already exists, Try siging in")
                B1 = False
                break
        if B1 :
            print("Enter your Username: " , end="")
            Username = input()
            B2 = True
            for x in Dict_of_all_Data.keys() :
                if Dict_of_all_Data[x]["Acount"]["Username"] == Username :
                    print("This Username already exists, Try siging in")
                    B2 = False
                    break
            if B2 :
                while True :
                    print("Enter your password: " , end="")
                    P1 = input()
                    print("Enter your password again: " , end="")
                    P2 = input()
                    if P1==P2 :
                        Dict_of_all_Data[String] = {"Acount":
                                                        {"Email address" : Email ,
                                                         "Username" : Username   ,
                                                         "Password" : P1}
                                                   }  
                        break
                    else :
                        print("Your two passwords do not match, Please try again!")
                        time.sleep(2)
    f = open("Data.txt" , 'w')
    f.write(str(Dict_of_all_Data))
    f.close()
        
Registration()
f = open("Data.txt" , 'r')
print(f.read())