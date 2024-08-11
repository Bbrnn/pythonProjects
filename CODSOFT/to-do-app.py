import tkinter as tk
from tkinter import messagebox
import json
import os

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.tasks = []
        self.load_tasks()

        # Task entry frame
        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        self.title_label = tk.Label(self.frame, text="Task Title:")
        self.title_label.pack(side=tk.LEFT)

        self.entry = tk.Entry(self.frame, width=50)
        self.entry.pack(side=tk.LEFT, padx=10)

        self.add_btn = tk.Button(self.frame, text="Add Task", command=self.add_task)
        self.add_btn.pack(side=tk.LEFT)

        # Task list frame
        self.list_frame = tk.Frame(root)
        self.list_frame.pack(pady=10)

        self.listbox = tk.Listbox(self.list_frame, width=75, height=15, selectmode=tk.SINGLE)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        self.scrollbar = tk.Scrollbar(self.list_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)

        # Buttons frame
        self.btn_frame = tk.Frame(root)
        self.btn_frame.pack(pady=10)

        self.edit_btn = tk.Button(self.btn_frame, text="Edit Task", command=self.edit_task)
        self.edit_btn.pack(side=tk.LEFT, padx=10)

        self.del_btn = tk.Button(self.btn_frame, text="Delete Task", command=self.delete_task)
        self.del_btn.pack(side=tk.LEFT, padx=10)

        self.mark_btn = tk.Button(self.btn_frame, text="Mark as Complete", command=self.mark_task)
        self.mark_btn.pack(side=tk.LEFT, padx=10)

        self.load_task_list()

    def add_task(self):
        task = self.entry.get()
        if task:
            self.tasks.append({"title": task, "completed": False})
            self.save_tasks()
            self.load_task_list()
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def edit_task(self):
        selected_task_index = self.listbox.curselection()
        if selected_task_index:
            task = self.tasks[selected_task_index[0]]
            new_task = self.entry.get()
            if new_task:
                task['title'] = new_task
                self.save_tasks()
                self.load_task_list()
                self.entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "You must enter a task.")
        else:
            messagebox.showwarning("Warning", "You must select a task to edit.")

    def delete_task(self):
        selected_task_index = self.listbox.curselection()
        if selected_task_index:
            del self.tasks[selected_task_index[0]]
            self.save_tasks()
            self.load_task_list()
        else:
            messagebox.showwarning("Warning", "You must select a task to delete.")

    def mark_task(self):
        selected_task_index = self.listbox.curselection()
        if selected_task_index:
            task = self.tasks[selected_task_index[0]]
            task['completed'] = not task['completed']
            self.save_tasks()
            self.load_task_list()

    def load_task_list(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            display_text = task['title']
            if task['completed']:
                display_text += " (Completed)"
            self.listbox.insert(tk.END, display_text)

    def save_tasks(self):
        with open("tasks.json", "w") as file:
            json.dump(self.tasks, file)

    def load_tasks(self):
        if os.path.exists("tasks.json"):
            with open("tasks.json", "r") as file:
                self.tasks = json.load(file)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()

