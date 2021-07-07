# ATM
ATM program using python

My Program is a Version 1- It is basic in its functionality and menu options 
I found importing from one file to another was causing me problems towards the final stages of my program due to the amount of funtionality and definitions I felt was necessary to create. Because of this my program contains only 3 main modules, Datastore containing the list of users and details, Login which holds the login functionality of a user entering their unique PIN and User ID and to verify that as a valid user, and the ATMProgram which is where the application launches from and also where the user menu is located. The CSV file holds the written text data for each users transactions, I found this to be the most suitable form of storage.
I thought the finished product to be quite user friendly and fucntional, however there are still some parts of the program that need work like the clear screen function after a menu option's transaction is executed. Additional functionality could also be added, but will be considered for Verion 2.

USER GUIDE:
When a user opens the application they will first be asked to enter their details consisting of a USER 1D number and a PIN number. A user will only be granted 3 attempts, and a clear warning message, before the system will exit. 

Once a user has logged in successfully, they will the be displayed with a welcome message containing their USER ID and a statement of their current balance and their overdraft status.Underneath will be an option menu with 7 options.
Each option will be acessible by typing the corresponding number into the 'Choose an Option' field.

If a user wishes to see their balance they will select option'1)' this will then display their balance and the option menu will reappear.

If a user wishes to make a deposit they will select option '2)' and input their deposit amount. Deposits are restricted to 1 up-to 1000 euro. Any deposit made beyond or under that amount will not be processed and a message explaining the maximum deposit amount has been reached or an invalid deposit amount has been inputted will appear. If the deposit is successful, an updated balance with be printed to the screen. The deposit transaction will then be written to the file containing transactional data and will be included in the list of transactions for that user.

If a user wishes to make a withdrawal they will select option '3)' and input their withdrawal amount. If a user is eligible for an overdraft (contained in the user datastore) they can withdraw any amount beyond their current balance. If an user is not eligible they will be displayed with a message saying they have insufficient funds. If the withdrawal is successful, an updated balance with be printed to the screen. The withdrawal transaction will then be written to the file containing transactional data and will be included in the list of transactions for that user.

If a user wishes to change their PIN, they will select option '4)'. Then they will have to enter theyre new PIN into the field displayed. If the user enters a PIN longer than 4 digits, a message will be displayed saying a PIN must be 4 digits. Once the PIN change is successful, the PIN transaction will be added to their list of transactions.

If a user wishes to make a service call theyw ill select option '6)'. This will return a print statement along with the service number for the bank

If user wishes to exit the app (at any stage) they will select option '7)' and the system will exit and display a 'Goodbye!' message.


