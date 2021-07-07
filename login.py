from user_datastore import create_users

# list of ATM users
user_list = create_users()


def get_user_Id():
    user_id = input("Enter ID: ")
    return user_id


def get_user_Pin():
    user_pin = input("Enter PIN: ")
    return user_pin



# check if a User exists otherwise return None
def verify_user(user_id, pin):

    for user in user_list:

        # does the user_id match a user id in the dictionary
        if(user['User ID'] == user_id):

            if(user['PIN Code'] == pin):
                # Success!                
                return user # as a dictionary

    return None # None is like null in C#


def welcome_user(active_user):
    print(f"Welcome user: {active_user['User ID']} to Molloy Banking's ATM System")    


def attempt_login():

    max_login_attempts = 3
    current_login_attempts = 0

    while(current_login_attempts < max_login_attempts):
        
        entered_id = get_user_Id()
        entered_pin = get_user_Pin()

        verified_user = verify_user(entered_id,entered_pin)
        
        if(verified_user != None):
            welcome_user(verified_user)
            return verified_user
        else:
            print("Access denied. User/Pin combination does not exist.")
            
            current_login_attempts = current_login_attempts + 1
    
    return None







        





    


