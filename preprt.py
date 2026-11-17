# import os
# import time

# def clear_screen():
#     os.system("cls" if os.name == "nt" else "clear")

# class User():
#     def __init__(self, first_name, last_name, email, password, status = "Inactive"):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.email = email
#         self.password = password
#         self.status = status

#     def display_user(self):
#         print(f"\nFirst Name: {self.first_name}")
#         print(f"Last Name: {self.last_name}")
#         print(f"Email: {self.email}")
#         print(f"Password: {self.password}")
#         print(f"Status: {self.status}")
#         print("_" * 20)
        

# def create_user():
#     first_name = input("\nEnter your name: ")
#     last_name = input("Enter your last name: ")
#     email = input("Eter email: ")
#     password = input("Enter password: ")

#     return User(first_name, last_name, email, password)

# new_users = []
# while True:
#     clear_screen()
#     print("\nWelcome to user management")
#     print("\nChoose an Action:\n")
#     print("1. Add new user")
#     print("2. Displsy all users")
#     print("3. Exit")

#     choice = input("\nEnter your Choice: ")

#     if choice == "1":
#         new_users.append(create_user())
#         print("\n User added Successefully")
#         time.sleep(2)

#     elif choice == "2":
#         clear_screen()
#         if len(new_users)>0:
#             print("\nDisplaying all Users...")
#             time.sleep(2)

#             for i in new_users:
#                 i.display_user()
#             time.sleep(2)
#         else:
#             print("\nThere is not Users")
#             time.sleep(2)

        
#     elif choice  == "3":
#         print("\nExiting...")
#         time.sleep(0.5)
#         clear_screen()
#         break
    
#     else:
#         print("\nInvalid action. please try Again")
#         time.sleep(0.5)

#******************************
# import time
# import os

# def clear_screen():
#     os.system("cls" if os.name == "nt" else "clear")

# class Member():
#     def __init__(self, first_name, last_name, membership_id, status):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.membership_id = membership_id
#         self.status = status

#     def display_member(self):
#         print(f"\nFirst Name: {self.first_name}")
#         print(f"Last Name: {self.last_name}")
#         print(f"Membership ID: {self.membership_id}")
#         print(f"Membership Status: {self.status}")
#         print("-" * 20)



# def creat_member():
#     clear_screen()
#     print("Create new member:")
#     print("-" * 18)
#     first_name = input("\nEnter first name: ")
#     last_name = input("Enter last name: ")
#     membership_id = input("Enter mebership ID: ")
#     status = input("Enter membership status: ")

#     return Member(first_name, last_name, membership_id, status)

# new_member = []

# while True:
#     clear_screen()
#     print("\nwelcome to Gym Membership Management")
#     print("\n\nChoose an Action")
#     print("\n1. Add new member")
#     print("2. Display all members")
#     print("3. Search for a member")
#     print("4. Exit")

#     choice = input("\nEnter your choice: ")

#     if choice == "1":
#         new_member.append(creat_member())
#         print("\nAdded member Successfully.!!")
#         time.sleep(2)
        
#     elif choice == "2":
#         clear_screen()
#         if new_member:
#             print("\nDisplaing all Memebership...")
#             time.sleep(2)
#             for i in new_member:
#                 i.display_member()
#             time.sleep(3)
#         else:
#             print("\nThere is not Membership. Please try Again")
#             time.sleep(1)
        
#     elif choice == "3":
#         print("\nWe working about That.")
#         time.sleep(1)

#     elif choice == "4":
#             print("\nExiting...")
#             time.sleep(0.5)
#             clear_screen()
#             break
#     else:
#         print("\nInvalid Action.!! pllease try Again.")
#         time.sleep(1)


#-----------------------------------------
#--Build with Python Desktop Application--
#-----------------------------------------
# from tkinter import Tk, Label, Button, Entry, END
# import os

# def clear_screen():
#     os.system("cls" if os.name == "nt" else "clear")


# def say_hello():
#     user_name = entery_label.get()
#     greeting_label.config(text=f"Hello,{user_name}! to MedDev")
#     entery_label.delete(0, END)


# clear_screen()

# window = Tk()
# window.title("MedDev Interactive App")
# window.geometry("500x350")

# title_label = Label(window, text="Enter your name below:", font=("Arial", 14))
# title_label.pack(pady=18)

# entery_label = Entry(window, width="40")
# entery_label.pack(pady=10)

# submit_button = Button(window, text="Say Hello", font=("Arial", 12), width="10", command=say_hello)
# submit_button.pack(pady=20)

# greeting_label = Label(window, text="Waiting for your name...", font=("Arial", 16))
# greeting_label.pack(pady=20)



# window.mainloop()

#----------------------
#--Python GUI project--
#----------------------

import tkinter
import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

clear_screen()

window = tkinter.Tk()
window.title("Data Entry From")
window.geometry("500x350")

frame = tkinter.Frame(window)
frame.pack()

#-Saving User Info
user_info_frame = tkinter.LabelFrame(frame, text="User Information")
user_info_frame.grid(row= 0, column= 0, padx=20, pady=20)

first_name_label = tkinter.Label(user_info_frame, text="First Name")
first_name_label.grid(row=0, column=0)

last_name_label = tkinter.Label(user_info_frame, text="Last Name")
last_name_label.grid(row=0, column=1)

first_name_entry = tkinter.Entry(user_info_frame)
last_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)



window.mainloop()