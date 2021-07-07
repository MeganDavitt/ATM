import os
import csv
from login import attempt_login
#from datetime import datetime #this is where I got confused with the datetime import


transaction_filename = "sample_data.csv"

def main_menu():
    print("1) Show current balance: ")
    print("2) Make a deposit: ")
    print("3) Make a withdrawal: ")
    print("4) Change PIN code: ")
    print("5) Show transactions: ")
    print("6) Service Call")
    print("7) Exit ")
    choice = input("Choose an option: ")
    return choice

def get_users_transactions(user): 
    with open(transaction_filename) as data:
        transactions = csv.DictReader(data)  

        print(f'\nAll Account Transactions for User ID: {user["User ID"]}')
        for row in transactions:
            if row["USERID"] == user["User ID"]:
                
 
                print(f'{row["DATE"]:<12}: {row["TRANSACTION"]:<12} amount €{float(row["BALANCE_AFTER"]) - float(row["BALANCE_BEFORE"]):.2f} Balance:€{row["BALANCE_AFTER"]}')
    print(f'End of Account Transactions for User ID: {user["User ID"]}\n')


def append_transaction(user, transaction_type, amount):
    from datetime import datetime
    with open(transaction_filename, "a") as file:  
        date = datetime.now().strftime("%Y-%m-%d") #took a while to get this working due to importing and naming of module still not sure if this is the best way?
        userid = int(user["User ID"])

        balance_after = user['Balance']

        if transaction_type == "Lodgement" :
            balance_before = user['Balance'] - amount
            transaction_details = f'{date},{userid},{transaction_type},{amount},{balance_before},{balance_after}\n'
        elif transaction_type == "Withdrawal":
            balance_before = user['Balance'] + amount
            transaction_details = f'{date},{userid},{transaction_type},{amount},{balance_before},{balance_after}\n'
        else:
            transaction_type = "PIN Change"
            transaction_details = f'{date},{userid},{transaction_type},,{balance_after},{balance_after}\n'
        
        file.write(transaction_details) #Writes the new changes to the transactions and should print new transactions while the program is running


def get_balance(user):
    print(f"Balance €{user['Balance']:.2f}") #users current balance

def print_user_account_details(user):
    print(f"User ID: {user['User ID']}")
    print(f"Balance €{user['Balance']:.2f}")

    if(user["Overdraft"]):
        print("Overdraft facility: Yes")
    else:
        print("Overdraft facility: No")


def make_deposit(active_user, amount): # setting +1 euro minimum
    if(amount <= 0):
        print("Invalid deposit amount") #code for maximum amount needs to be added 
        return False
    if(amount >= 1000):
        print("Maximum deposit amount has been reached.")
    else:
        active_user["Balance"] = active_user["Balance"] + amount
        return True           


def make_withdrawal(active_user, amount): 
    
    if(amount > active_user["Balance"] ): #depending if user is eligible for overdraft based on user list info
        if ( active_user["Overdraft"] == True):
            active_user["Balance"] = active_user["Balance"] - amount
            return True
        else:
            print("Sorry, you have insufficient funds to complete this transaction. Please contact Molloy Bank for more Information ")
            return False
    else:
        active_user["Balance"] = active_user["Balance"] - amount 
        return True

def changePin(user, newPIN):
    user["PIN Code"] = newPIN
    print("Your PIN number has been changed")
    
def print_service_call(user):
    print(f'Hello User: {user["User ID"]} if you would like to speak to a member of our team please call: 01-555-123')
 

def clear_screen():
    os.system('cls')

def exit():
    print("Goodbye")
    clear_screen
    

def print_failed_login():
     print("Good bye!")

#Program launches from here
def application_start():

    clear_screen()

    #Logged in user =
    active_user = ""
          
  
    active_user = attempt_login() #to return user dictionary or None

    # print(active_user) # testing #if I use details that arent from a user should show none 

    #if login is successful set active user and show main menu
    #else exit app
    if(active_user != None):

        print_user_account_details(active_user)
        
        choice = ""               
    	
        while(choice != "7"):
            
            #show the main menu and menu options
            choice = main_menu() 
            clear_screen()
            if(choice == "1"):
                
                get_balance(active_user)

            elif(choice == "2"):
                amount = float(input("Enter deposit amount: "))
                clear_screen()
                if(make_deposit(active_user, amount)):
                    append_transaction(active_user, "Lodgement", amount) #to write the transactions into the file
                    get_balance(active_user) 

            elif(choice == "3"):
                amount = float(input("Enter withdrawal amount: "))
                clear_screen()
                if(make_withdrawal(active_user, amount)):
                    append_transaction(active_user, "Withdrawal", amount)
                    get_balance(active_user)

            elif(choice == "4"):
                while(True):
                    new_pin = input("Enter new PIN: ")
                    clear_screen()
                    if( len(new_pin) == 4 and new_pin.isnumeric() ): #handling the string as a numerical value, setting PIN for only 4 digits
                        changePin(active_user, new_pin)
                        append_transaction(active_user, "PIN Change", 0)
                        break
                    else:
                        print("PIN must be exactly 4 digits")
                
            elif(choice == "5"):
                get_users_transactions(active_user)
                
            elif(choice == "6"):
                print_service_call(active_user) #simple print statement as didnt want to create more complexity at this stage
            
            elif(choice == "7"):
                exit()
          
            
            

    else:
       print_failed_login()


application_start()