print("Welcome to the buisness Chatbot")
name = input("What is your name? ")
age = input("Hello " + name + ", how old are u?")

print(f"Great! Nice to meet you, {name}. Let's get started.")

# -------------------------------
# Task 3: Implement User Information Collection
# -------------------------------
email = input("Please enter your email: ")
company = input("What company do you work for? ")

print(f"Thanks, {name}. We've recorded your email as {email} and company as {company}.")

# -------------------------------
# Task 4: Design Conversation Menu
# -------------------------------
def show_menu():
    print("\n--- Conversation Menu ---")
    print("1. Learn about our services")
    print("2. Contact customer support")
    print("3. Business hours information")
    print("4. Placeholder options")
    print("5. Exit")

# -------------------------------
# Task 5: Develop User Assistance Query
# -------------------------------
def handle_query(option):
    if option == "1":
        print("We provide consulting, tech solutions, and business automation.")
    elif option == "2":
        print("You can reach our customer support at support@business.com.")
    elif option == "3":
        print("Our business hours are Monday to Friday, 9 AM to 6 PM.")
    elif option == "4":
        placeholder_options()
    elif option == "5":
        print("Thank you for using the Business Chatbot. Goodbye!")
        return False
    else:
        print("Invalid choice, please try again.")
    return True

# -------------------------------
# Task 6: Implement Placeholder Options
# -------------------------------
def placeholder_options():
    print("\n--- Placeholder Options ---")
    print("A. Coming soon: Live Chat support")
    print("B. Coming soon: Order tracking")
    print("C. Coming soon: Account management")

# -------------------------------
# Task 7: Add Exit Option in Menu
# -------------------------------
# (Already included in menu and handle_query with option "5")

# -------------------------------
# Run Chatbot Loop
# -------------------------------
running = True
while running:
    show_menu()
    user_choice = input("Please select an option (1-5): ")
    running = handle_query(user_choice)