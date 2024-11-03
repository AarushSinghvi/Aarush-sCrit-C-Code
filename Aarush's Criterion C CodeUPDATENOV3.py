import pyfiglet
import re


#Title and Outro for the Program
title = pyfiglet.figlet_format("HAP - For History", font="banner4", width=150)
print(title)

outro = pyfiglet.figlet_format("Thanks For Using HAP!", font="xtty", width=250)

# Initialize User database
user_database = {
   "1": {
        "email": "aarushsinghvi2010@gmail.com",
        "password": "123456"
    },
    "2": {
        "email": "singhviaarush7@gmail.com",
        "password": "123456"
    },
    "3": {
        "email": "aarush_singhvi@my.ofs.edu.sg",
        "password": "HAP@12"
    }
}

print(user_database);

# Simulated session storage
sessions = {}

# Example search data
search_database = [
    {"title": "India:History","Category": "India", "Author":"Britannica"},
    {"title": "Ancient Civilisations","Category":"History","Author":"Encyclopedia"},
    {"title": "Physics Fundamentals", "Category": "Science", "Author": "OpenStax"},
    {"title": "Singapore History", "Category": "Singapore", "Author": "Mediacorp"}
]


#Function for User Interface
def user_function():
    while True:
        #Check if user is already logged in
        if sessions.get("logged_in_user"):
            print( "\nOptions:\n1. Search..\n2. Logout\n3. Exit Program")
            try:
                choice = int(input("Enter your choice (1, 2 or 3): "))
                if choice == 1:
                    search_database_function()  # Allow search without re-login
                elif choice == 2:
                    logout_user()      # Logout the user
                elif choice == 3:
                    print("Exiting Program...", outro)
                    break             # Exit the program
                else:
                    print("Invalid choice. Please enter 1, 2, or 3.")
            except ValueError:
                print("Invalid input type. Please enter either 1, 2, or 3.")
        else:
            # Login or Signup options if no user is logged in
            print("\nWelcome to HAP! Would you like to Login or Sign Up?")
            print("Press 1 for Login, 2 for Signup, or 3 to Exit.")
            try:
                choice = int(input("Enter your choice (1, 2, or 3): "))
                if choice == 1:
                    login_user()
                elif choice == 2:
                    register_user()
                elif choice == 3:
                    print("Exiting Program...", outro)
                    break
                else:
                    print("Invalid choice. Please enter 1, 2, or 3.")
            except ValueError:
                print("Invalid input. Please enter a number.")

 #Function for User Login     
def login_user():
    email = input("Please Enter Your Email Address: ").strip()
    password = input("Please Enter Your Password: ").strip()
    
    # Check credentials
    for user_id, details in user_database.items():
        if details["email"] == email and details["password"] == password:
            sessions["logged_in_user"] = user_id
            print("Login successful...Welcome Back", email, "!")
            return
    
    print("Incorrect credentials. Please try again.")
    


#Function for new user registration
def register_user():
    email = input("Please Enter your Email Address to register with: ").strip()
    if email in user_database:
            print("This Email Is Already Registered With HAP")
    elif email == "":
            print("Please Input A Valid Email Address")

    password = input("Please Enter a 6-Digit Password (Caps, Lower, Numbers and Special Characters):").strip()
    if len(password) == 6 and re.search(r'[A-Za-z]', password) and re.search(r'[0-9]', password):
                new_id = str(len(user_database) + 1)
                user_database[new_id] = {"email": email, "password": password}
                print(f"The Email", email, "Has Successfully been registered with HAP! Please log in to continue.")
                return password
    else:
            print("The Password Must Be only 6-Characters Long and contain a mixture of Letters and Numbers.")
    

 
# Function to handle logout
def logout_user():
    if "logged_in_user" in sessions:
        del sessions["logged_in_user"]
        print("You have been logged out successfully!.")
    else:
        print("No user is currently logged into HAP.")

#Function to search the simulated database
def search_database_function():
    # Ensure the user is logged in before searching
    if "logged_in_user" not in sessions:
        print("You must be logged in to perform a search.")
        return
    
    # Get keywords from user input and split them for more flexible searching
    keywords = input("What Would You Like To Search Today (e.g., 'India History'): ").lower().split()
    results = []

    # Search for any keyword match in each field
    for entry in search_database:
        if any(keyword in entry["title"].lower() or keyword in entry["Category"].lower() or keyword in entry["Author"].lower() for keyword in keywords):
            results.append(entry)

    # Display search results or offer suggestions
    if results:
        print("\nSearch Results:")
        for result in results:
            print(f"Title: {result['title']}, Author: {result['Author']}, Category: {result['Category']}")
    else:
        print(f"No results found for your search. Did you mean: ")
        suggest_keywords()   
    
    print("Search term cannot be empty. Please try again.")

# Function to suggest available keywords if no results are found
def suggest_keywords():
    print("\nSuggested keywords based on available data:")
    # Extract unique keywords from titles, categories, and authors
    keywords = set()
    for entry in search_database:
        keywords.update(entry["title"].split())
        keywords.add(entry["Category"])
        keywords.add(entry["Author"])

    # Display keywords for user selection
    keyword_list = list(keywords)
    for i, keyword in enumerate(keyword_list, 1):
        print(f"{i}. {keyword}")
    
    # Prompt user to select a keyword to search again
    try:
        choice = int(input("\nSelect a keyword number to search again, or 0 to exit: "))
        if choice > 0 and choice <= len(keyword_list):
            selected_keyword = keyword_list[choice - 1]
            print(f"\nSearching for '{selected_keyword}'...\n")
            perform_search(selected_keyword)
        elif choice == 0:
            print("Returning to main menu.")
        else:
            print("Invalid choice. Returning to main menu.")
    except ValueError:
        print("Invalid input. Returning to main menu.")

# Function to perform search with a single keyword
def perform_search(keyword):
    results = []
    keyword = keyword.lower()

    for entry in search_database:
        if keyword in entry["title"].lower() or keyword in entry["Category"].lower() or keyword in entry["Author"].lower():
            results.append(entry)

    if results:
        print("Search Results:")
        for result in results:
            print(f"Title: {result['title']}, Author: {result['Author']}, Category: {result['Category']}")
    else:
        print("No results found for your search.")

# Run the main user function to start the program
user_function()

