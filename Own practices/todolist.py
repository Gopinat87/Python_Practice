def show_task(tasks):
    if tasks :
        print("Your Tasks Are: ")
        for task in tasks :
            print(f"\t- {task}")
        
    else:
        print("\n Your Tasks Are Empty")

def add_task(tasks):
    task = input("Enter New Task: ")
    tasks.append(task)
    print("task added Successfully")

def remove_task(tasks):
    show_task(tasks)
    if tasks :
        try:
            num = int(input("Enter a Remove task number : "))
            removed = tasks.pop(num-1)
            print("Your Tasks are removed successfully")
        except:
            print("Invalid task number")    

tasks = []

while True :

    print("---------To do List--------")
    print("Choose the option ")
    print("1. Show Task")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

    option = input("Enter a Option: ")

    if option == "1" :
        show_task(tasks)
    elif option == "2":
        add_task(tasks)
    elif option == '3' :
        remove_task(tasks)
    elif option == "4":
        break
    else :
        print("Sorry Invalid option ")