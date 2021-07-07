#hard coded user details
def create_users():
    user_list = []

    user = {"User ID": "1234", "PIN Code": "1100", "Balance": 6700.00, "Overdraft": True}
    user_list.append(user)
    user_list.append({"User ID": "5678", "PIN Code": "3322", "Balance": 2494.00, "Overdraft": True})
    user_list.append({"User ID": "9012", "PIN Code": "5544", "Balance": 1039.00, "Overdraft": False})
    user_list.append({"User ID": "3456", "PIN Code": "7766", "Balance": 2800.00, "Overdraft": False})
    user_list.append({"User ID": "7890", "PIN Code": "9988", "Balance": 1496.00, "Overdraft": False})
    return user_list


