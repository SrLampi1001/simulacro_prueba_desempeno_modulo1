# Program in progress

The program will use POO to create a enviroment for a simulated system of borrowing in a Tech Company, in a very simplistic way.  
The interfaz for admin will allow to navegate all of the users and see all the borrowed equipment, the program works with time. (Time can be accelerated and stopped but no returned)  
Exist 3 types of user (excluding admin): administrarive, student and instructor. This user type can't access to the other user's information, but can see all the avaible equipment, borrow it and return it, the student can borrow for 3 days, the instructor for 7 days and administrative for 10 days.  
The admin user can allow for request to borrow equipment, solicite repairment and accept returning.  
The admin can create reports on the month and year  

## How to use the program (expectatives)

It can only be used on console, and a simulator, so only one user on a computer will be connected to the program.  
The program will ask for a time to start, inside, insert a date and time, this will allow the program to have a start point (start point is stored outside memory, the archive type is not decided yet).  
The user MUST create a admin user account first, if it doesn't exist already (The respective csv archives with the accounts, including the admin one, should be in this repository when it's finished, along with the passwords without encriptation)  
As an admin, if no equipment on the csv archives, needs to create the equipment  
The admin CANNOT borrow equipment, to borrow, the user must log out and create a new account, be it in role student, instructor or administrative, when created, a new menu should appear, in which borrow request can be made.  
If a borrow request is made, the user need's to log out and access in the admin account, select the option to see pending request, select the request you want and decide if accept it or don't  
When loggin in an account, if the user does not insert the correct password in 3 oportunities, the program will close  

## Implementations at future vs current state

- Only one admin user can exists on the program, the verifications for this are not implemented yet.  
- The user and equipment classes are used inside each one, to mark the reference from the user in posesion of the equipment and viceversa (Realistically, only one is necesary, and is going to simplify the process for csv saving)  
- For the csv storing is necesary to use ID, it's only obligatory for the equipment to have an ID, the user class either has ID or unique user name (Probably unique user name is going to make easer manage the logins)  
- The time is planned to be inserted manually on the console menu when making a borrow, instead, should create a time enviroment variable and set timeout and promises to solve at the adecuate time  
- If the time is to be inside the program, since the program can not be running on background, there should be a first input inside a program that sets the start execution time, and based on that, should make the pertaining calcules for the late returning and pending aprovations  
- If the function for repairing is created, it should be a simple request with a set timeout until the equipment is to be available again.  
- Currently the program does not await for aprovation via de admin user, it needs to be done, the information of the pending aprovations for borrowing should be saved on the csv archives pertaining the users (new state for pending), there's the need to create inside the main a function to initialize and create the objects with the data on the csv  