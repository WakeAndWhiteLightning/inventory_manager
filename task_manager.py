#=====importing libraries===========
'''This is the section where you will import libraries'''
from datetime import date

#====Login Section====
'''Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file.
    - Use a while loop to validate your user name and password.
'''
#Create database for user information and break condition variable
user_database = {}
find = False
#Take the information from the user.txt and put it into a dictionary, then check the user inputs against the dictionary
users = open('user.txt', 'r')
for line in users:
    user_list = line.split(', ')
    user_database.update({f'{user_list[0]}' : f'{user_list[1]}'})
#This while loop gets the username and password from the user then checks to see if they match the provided user.txt file
while True:
    if find == True:
        break  
    username = input('Please enter your username: ')
    password = input('Please enter your password: ')

    for item in user_database.items():
        if username == str(item[0]):
            if password == str(item[1]).strip('\n'):
                print('Login success!')
                find = True
                break
            else:
                print('Incorrect password, please try again')
                break
        elif item[0] == list(user_database)[-1]:
            print('Username not recognised, please try again')
users.close()

while True:
    #presenting the menu to the user and 
    #making sure that the user input is coneverted to lower case.
    if username == 'admin': 
        menu = input('''Select one of the following Options below:
        s - display statistics
        r - Registering a user
        a - Adding a task
        va - View all tasks
        vm - view my task
        e - Exit
        : ''').lower()
    else:
        menu = input('''Select one of the following Options below:
        a - Adding a task
        va - View all tasks
        vm - view my task
        e - Exit
        : ''').lower()

    if menu == 'r' and username == 'admin':
        #Get user to enter the username and password they would like to add, confirming the password
        while True:
            print('You have chosen to register a new user')
            username_add = input('Please enter the username: ')
            password_add = input('Please enter the password: ')
            password_confirmation = input('Please confirm the password: ')

            #Check both password entries match
            if password_add == password_confirmation:
                with open('user.txt', 'a') as users:
                    users.write(f'\n{username_add}, {password_add}')
                    break
            else:
                print('Passwords do not match, please try again')
                continue


            '''In this block you will write code to add a new user to the user.txt file
            - You can follow the following steps:
                - Request input of a new username
                - Request input of a new password
                - Request input of password confirmation.
                - Check if the new password and confirmed password are the same.
                - If they are the same, add them to the user.txt file,
                - Otherwise you present a relevant message.'''

    elif menu == 'a':
        assignee = input('You have chosen to add a new task. Who will this task be assigned to: ')
        task_title = input('What is the title of the task: ')
        task_description = input('Enter a description of the task: ')
        due_date = input('What date is the task due: ')
        todays_date = date.today()

        with open('tasks.txt', 'a') as tasks:
            tasks.write(f'\n{assignee}, {task_title}, {task_description}, {todays_date}, {due_date}, No')
            print('''
____________________________________________________
            
Your task has been added to the tasks.txt file!
            
____________________________________________________

            ''')


        '''In this block you will put code that will allow a user to add a new task to task.txt file
        - You can follow these steps:
            - Prompt a user for the following: 
                - A username of the person whom the task is assigned to,
                - A title of a task,
                - A description of the task and 
                - the due date of the task.
            - Then get the current date.
            - Add the data to the file task.txt and
            - You must remember to include the 'No' to indicate if the task is complete.'''

    elif menu == 'va':
        with open('tasks.txt', 'r') as tasks:
            for line in tasks:
                task_properties = line
                task_list = task_properties.split(', ')
                print(f'''
                
______________________________________________________________________________

Task:               {task_list[1]}
Assigned to:        {task_list[0]}
Date Assigned:      {task_list[3]}
Due Date:           {task_list[4]}
Task Complete?:     {task_list[5]}
Task Description:   {task_list[2]}
______________________________________________________________________________
                
                
                ''')

        '''In this block you will put code so that the program will read the task from task.txt file and
         print to the console in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
         You can do it in this way:
            - Read a line from the file.
            - Split that line where there is comma and space.
            - Then print the results in the format shown in the Output 2 
            - It is much easier to read a file using a for loop.'''

    elif menu == 'vm':
        with open('tasks.txt', 'r') as tasks:
            for line in tasks:
                task_properties = line
                task_list = task_properties.split(', ')
                if task_list[0] == username:
                    print(f'''
                    
______________________________________________________________________________

Task:               {task_list[1]}
Assigned to:        {task_list[0]}
Date Assigned:      {task_list[3]}
Due Date:           {task_list[4]}
Task Complete?:     {task_list[5]}
Task Description:   {task_list[2]}
______________________________________________________________________________
                    
                    
                    ''')
        '''In this block you will put code the that will read the task from task.txt file and
         print to the console in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
         You can do it in this way:
            - Read a line from the file
            - Split the line where there is comma and space.
            - Check if the username of the person logged in is the same as the username you have
            read from the file.
            - If they are the same print it in the format of Output 2 in the task PDF'''

#Checks the user is logged in as admin and displays the number of tasks and users
    elif menu == 's' and username == 'admin':
        with open('tasks.txt', 'r') as tasks:
            number_of_tasks = tasks.readlines()
        
        with open('user.txt', 'r') as users:
            number_of_users = users.readlines()

        print(f'''
___________________________________________
                    
Number of users:   {len(number_of_users)}
Number of tasks:   {len(number_of_tasks)}
___________________________________________

''')

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")