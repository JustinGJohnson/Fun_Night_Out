# restaurant api caller
# ui.py

def display_menu():

    # Display choices for user, return users selection
    print('''
        1. Pick a place to eat
        2. Pick a movie
        3. Pick some music??
        q. Quit
    ''')

    choice = input("Enter your selection: ")
    return choice

# prompts user for y or n, returns choice
def prompt_for_more():
    choice = input("Want info on another restaurant? (y/n) ")
    return choice

def message(msg):
    # get message from somewhere else in project, print to user
    print(msg)