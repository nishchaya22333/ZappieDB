import art
import customer_analysis

def main():
    while True:
        print("Menu:")
        print("1. Sign In")
        print("2. Sign Up")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            custID = customer_analysis.signIn()
            if (custID != -1):
                shopNow(custID)
        elif choice == "2":
            customer_analysis.signUp()
        elif choice == "3":
            print("Exiting the program...")
            break
        else:
            print(art.dog)
            print("Invalid choice. Please try again.")

def shopNow(custID):
    while True:
        print("Menu:")
        print("1. Add Product")
        print("2. Remove Product")
        print("3. Place Order")
        print("4. My Analysis")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            customer_analysis.addProduct(custID)
        elif choice == "2":
            customer_analysis.removeProduct(custID)
        elif choice == "3":
            customer_analysis.placeOrder(custID)
        elif choice == "4":
            customer_analysis.menuForCustomerAnalysis(custID)
        elif choice == "5":
            print("Exiting the program...")
            break
        else:
            print(art.dog)
            print("Invalid choice. Please try again.")