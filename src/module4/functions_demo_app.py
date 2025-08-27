from src.module4.python_functions import greet_user, area_flow, roll_dice_flow, lambda_map_flow, future_feature, \
    translate_flow
"""
Author: Professor Lewis
Date: August 25, 2025
This module is directly execute and is the driver of the program.
It displays a menu options, listing each function to invoke. 
Azure AI Translator
"""

def show_menu():
    print("\n=== Functions Demo Menu ===")
    print("1) Greet (void function)")
    print("2) Area of a circle")
    print("3) Roll dice")
    print("4) Translate text (Azure)")
    print("5) Add to each number (lambda + map)")
    print("6) (Stub) Future feature (pass)")
    print("0) Exit")



def main():
    print("Welcome to the Functions Demo!")
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()  # show available actions
        if choice == "1":
            greet_user()
        elif choice == "2":
            area_flow()
        elif choice == "3":
            roll_dice_flow()
        elif choice == "4":
            translate_flow()
        elif choice == "5":
            lambda_map_flow()
        elif choice == "6":
            future_feature()
            print("(Stub called--no behavior yet.)")
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Please choose 0-6.")






if __name__ == "__main__":
    main()
