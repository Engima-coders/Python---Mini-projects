tasks=[]
def add_task(task):
    tasks.append({'task':task,'done':False})
def mark_task(i):
    i=i-1
    if 0<=i<len(tasks):
        tasks[i]['done']=True
    else:
        print('Invalid index number')
def remove_task(i):
    i=i-1
    if 0<=i<len(tasks):
        tasks.pop(i)
    else:
        print("Invalid task index")
def show_task():
    if len(tasks)==0:
        print('no task')
    else:
      for i in tasks:
        print(i)
def main():
    while True:
        print("Welcome to TODO LIST Application")
        print("Menu:")
        print("1.Add Task")
        print("2.Mark Task As Done")
        print("3.Remove Task")
        print("4.Show Task")
        print("5.EXIT")
        c=int(input("Enter a choice"))
        match(c):
            case 1:
                task=input("Enter a Task")
                add_task(task)
           
            case 2:
                index=int(input('Enter task index'))
                mark_task(index)
            
            case 3:
                index=int(input('Enter task index'))
                remove_task(index)
            
            case 4:
                show_task()
           
            case 5:
                break
            case default:
                print('invalid choice')
main()



            


        
    

