import os

def load_tasks():
  """Loads tasks from a file.

  Returns:
    A list of tasks.
  """

  try:
    with open("tasks.txt", "r") as file:
      tasks = file.readlines()
      return [task.strip() for task in tasks]
  except FileNotFoundError:
    return []

def save_tasks(tasks):
  """Saves tasks to a file.

  Args:
    tasks: A list of tasks.
  """

  with open("tasks.txt", "w") as file:
    for task in tasks:
      file.write(task + "\n")

def display_menu():
  """Displays the main menu."""

  print("To-Do List App")
  print("1. Add a task")
  print("2. View tasks")
  print("3. Mark task as completed")
  print("4. Remove a task")
  print("5. Quit")

def main():
  tasks = load_tasks()

  while True:
    display_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
      task = input("Enter the task: ")
      tasks.append(task)
      save_tasks(tasks)
    elif choice == "2":
      if tasks:
        for i, task in enumerate(tasks, 1):
          print(f"{i}. {task}")
      else:
        print("No tasks found.")
    elif choice == "3":
      if tasks:
        index = int(input("Enter the task number to mark as completed: ")) - 1
        if 0 <= index < len(tasks):
          tasks[index] = f"✅ {tasks[index]}"
          save_tasks(tasks)
        else:
          print("Invalid task number.")
      else:
        print("No tasks found.")
    elif choice == "4":
      if tasks:
        index = int(input("Enter the task number to remove: ")) - 1
        if 0 <= index < len(tasks):
          tasks.pop(index)
          save_tasks(tasks)
        else:
          print("Invalid task number.")
      else:
        print("No tasks found.")
    elif choice == "5":
      print("Goodbye!")
      break
    else:
      print("Invalid choice. Please try again.")

if __name__ == "__main__":
  main()