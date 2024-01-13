class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({'task': task, 'completed': False})
        print(f"Task '{task}' added successfully.")

    def view_tasks(self):
        print("\nTo-Do List:")
        for index, task in enumerate(self.tasks, start=1):
            status = "Complete" if task['completed'] else "Incomplete"
            print(f"{index}. {task['task']} - {status}")

    def mark_complete(self, index):
        if 1 <= index <= len(self.tasks):
            self.tasks[index - 1]['completed'] = True
            print(f"Task '{self.tasks[index - 1]['task']}' marked as complete.")
        else:
            print("Invalid task index.")

    def delete_task(self, index):
        if 1 <= index <= len(self.tasks):
            deleted_task = self.tasks.pop(index - 1)
            print(f"Task '{deleted_task['task']}' deleted.")
        else:
            print("Invalid task index.")

todo_list = ToDoList()

while True:
    print("\nTO-DO LIST MENU:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Complete")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        task = input("Enter the task: ")
        todo_list.add_task(task)

    elif choice == '2':
        todo_list.view_tasks()

    elif choice == '3':
        index = int(input("Enter the task index to mark as complete: "))
        todo_list.mark_complete(index)

    elif choice == '4':
        index = int(input("Enter the task index to delete: "))
        todo_list.delete_task(index)

    elif choice == '5':
        print("Exiting the To-Do List. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
