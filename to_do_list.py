tasks=[]

def add_task():
    task = input("Input Your Task: ")
    tasks.append(task)
    print(f"Task '{task}' has been added to the list.")

def ListTask():
    if not tasks:
        print("This List Is Empty")
    else :
        print("Your Tasks Are :")
        for index , i in enumerate(tasks):
            print(f'{index}.{i}')

def DeleteTask():
    try:   
        number_of_deleted_task=int(input("Choose Numbers of Task You Want To delete :"))
        if number_of_deleted_task < len(tasks):
            deleted_task=input("Choose Task You Want To delete :" *int(number_of_deleted_task))
            if deleted_task in tasks:
                dele=deleted_task.lower().strip()
                y=tasks.remove(dele)
                print(f'{deleted_task} Is Been Deleted')
            else:
                print("Sorry We Can't find What You Are looking For")
        else:
            print("Sorry No You Want To delete Tasks More Than You Have.....")
    except:
        print("Sorry Invalid Input")

if __name__=="__main__":
    #Creat The Loop For App
    print("Welcome To Do_List Application")
while True:
    print("\n")
    print("Pleas select On Of The following")
    print("-"*134)
    print("1. Add a new Item")
    print("2. Delete a task")
    print("3. List tasks")
    print("4. Quit")

    choice=int(input("Choose What You Want To Do :"))
    
    
    if (choice==1):
        add_task()
    elif(choice==2):
        DeleteTask()
    elif(choice==3):
        ListTask()
    elif(choice==4):
        print("Goody Bey ")
        break
    else:
        print("Sorry input .... Pleas Try Again")
    

