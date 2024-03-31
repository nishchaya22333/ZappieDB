import art
import GUI_boot

def main():
    choice = input("1. Boot server and create database \nEnter your choice: ")
    if (choice == "1"):
        warning_message = "Proceed only if server is in initial state. Attempt to duplicate database will lead to termination."
        print("\u26A0"+"\033[91mWarning: \033[0m" + " " + warning_message)
        proceed = int(input("1. Continue\n2. Cancel\nEnter your choice: "))
        if proceed == 1:
            GUI_boot.main()
    else:
        print(art.dog)
        print("Invalid Choice. \nMore options coing soon!")
# main()