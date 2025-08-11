from register import User  # Assuming you have a User class in register.py
from usermanager import Usermanager  # Assuming this manages user storage

class Auth:
    def login(self):
        email =input("Email")
        password =input("Password")
        user=Usermanager.finduser(email=email,password=password)

        if user:
            print("Login Succesfull")
        else:
            print("user not found")


    def Register(self):
        try:
            name = input("Name: ")
            email = input("Email: ")
            password = input("Password: ")
            phone_no = input("Phone No: ")

            user = User(name=name, email=email, password=password, phone_no=phone_no)
            Usermanager.adduser(user)

            print(f"User {name} registered successfully!")
        except Exception as e:
            print("Error during registration:", e)

    def Guest(self):
        print("Continuing as guest...")

    def Validate(self, option):
        if option == 1:
            self.login()
        elif option == 2:
            self.Register()
        elif option == 3:
            self.Guest()
        elif option == 4:
            print("Exiting the app. Goodbye!")
            exit()  # Exit the program cleanly
        else:
            print("Invalid option")


class FoodApp(Auth):
    loginoptions = {1: "Login", 2: "Register", 3: "Guest", 4: "Exit"}

    @staticmethod
    def Init():
        print("<< Welcome to Online Food Ordering >>")
        auth = FoodApp()

        while True:
            print("\nChoose an option:")
            for option in FoodApp.loginoptions:
                print(f"{option}. {FoodApp.loginoptions[option]}",end = " ")
            print()
            try:
                choice = int(input("Please Enter Your Choice: "))
                auth.Validate(choice)
            except ValueError:
                print("Invalid input. Please enter a number.")

# Call the Init method
if __name__ == "__main__":
    FoodApp.Init()
