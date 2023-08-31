class TodoApp:
    def __init__(self):
        self.tasks = []
    
    def display_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            print("Tasks:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")
    
    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added successfully.")
    
    def edit_task(self, task_index, new_task):
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1] = new_task
            print(f"Task {task_index} updated successfully.")
        else:
            print("Invalid task index.")
    
    def delete_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            removed_task = self.tasks.pop(task_index - 1)
            print(f"Task '{removed_task}' removed successfully.")
        else:
            print("Invalid task index.")

# Create a new instance of the TodoApp class
todo_app = TodoApp()

while True:
    print("\nMenu:")
    print("1. Display Tasks")
    print("2. Add Task")
    print("3. Edit Task")
    print("4. Delete Task")
    print("5. Exit")
    
    choice = input("Enter your choice (1/2/3/4/5): ")
    
    if choice == '1':
        todo_app.display_tasks()
    elif choice == '2':
        task = input("Enter task: ")
        todo_app.add_task(task)
    elif choice == '3':
        task_index = int(input("Enter task index to edit: "))
        new_task = input("Enter new task: ")
        todo_app.edit_task(task_index, new_task)
    elif choice == '4':
        task_index = int(input("Enter task index to delete: "))
        todo_app.delete_task(task_index)
    elif choice == '5':
        print("Exiting the To-Do app.")
        break
    else:
        print("Invalid choice. Please choose again.")

