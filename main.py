print(20*"="+" Welcome To My Personal_Data_Protection_Program "+"="*20)

import pyautogui as auto

def the_file():

    name = input("please enter your name: ").lower().strip()
    mother_name = input("please enter your mother name: ").lower().strip()
    email = input("please enter your email: ")
    try:
        phone_num = int(input("please enter your phone number: "))
    except:
        print("the phone number should be integer ❗")
        phone_num = int(input("please enter your phone number: "))
    password = input("please enter your password: ")

    details = {}

    details["name"] = name
    details["mother name"] = mother_name
    details["email"] = email
    details["phone number"] = phone_num
    details["password"] = password
    
    with open(f"{password}.txt","w") as file:
        for key , value in details.items():
            file.write(f"{key} => {value}\n")

the_file()

answer = input("Do you want to access your file (yes,no): ").lower().strip()

if answer == "no":
    exit() 
elif answer == "yes":
    the_pass = auto.password(text="Please Enter Your Password",title="The Password",default=None,mask="x")
    try:
        with open(f"{the_pass}.txt","r") as file:
            data = file.readlines()
            for i in data:
                print(i)
    except:
        print("Unfortunately, you do not have a file. Please create one and try again ❗")
        exit()
else:
    print("Error. Please do not write anything other than what is written in the question ❗")

# This Is My Personal_Data_Protection_Program_Project 




