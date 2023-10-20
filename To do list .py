#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Initialize an empty list to store tasks
tasks = []

# Function to display the current tasks
def show_tasks():
    if tasks:
        print("Your To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    else:
        print("Your to-do list is empty.")

# Function to add a task
def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"Task '{task}' has been added to your to-do list.")

# Function to remove a task
def remove_task():
    show_tasks()
    if tasks:
        task_number = int(input("Enter the task number to remove: "))
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f"Task '{removed_task}' has been removed from your to-do list.")
        else:
            print("Invalid task number.")
    else:
        print("Your to-do list is empty, nothing to remove.")

# Main loop to interact with the to-do list
while True:
    print("\nTo-Do List Menu:")
    print("1. Show Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Quit")
    
    choice = input("Enter your choice (1/2/3/4): ")
    
    if choice == '1':
        show_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option (1/2/3/4).")


# In[ ]:




