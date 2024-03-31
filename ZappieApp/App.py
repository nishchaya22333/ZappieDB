import pyfiglet
from pyfiglet import Figlet
import art
import admin_menu
import customer_menu

# Text color
colour = ["\033[94m",'\033[92m', "\033[91m"] #blue, green, red
colour_end = "\033[0m"


# Welcome text
f = pyfiglet.figlet_format("Zappie", font="slant")
print(art.cow)
print("        ____________________")
print(colour[0], f,colour_end)
print(colour[1] + "            Welcome" + colour_end)

print("Choose an option to proceed: ")
while(True):
    choice = (input("1. Open Admin Portal \n2. Open Customer Portoal\n3. Exit \nEnter you choice: "))
    if choice == "1":
        admin_menu.main()
        continue
    elif choice == "2":
        customer_menu.main()
    elif choice == "3":
        break
    else:
        print(colour[2],"Invalid Choice", colour_end)
        continue
