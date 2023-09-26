import tkinter as tk
from tkinter import messagebox

class TodoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Todo List")

        self.task_list = []

        self.create_widgets()

    def create_widgets(self):
        self.task_entry = tk.Entry(self.master, width=50)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        self.add_button = tk.Button(self.master, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=10, pady=10)

        self.task_listbox = tk.Listbox(self.master, width=50)
        self.task_listbox.grid(row=1, column=0, padx=10, pady=10, rowspan=5)

        self.update_button = tk.Button(self.master, text="Update Task", command=self.update_task)
        self.update_button.grid(row=1, column=1, padx=10, pady=10)

        self.delete_button = tk.Button(self.master, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=2, column=1, padx=10, pady=10)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.task_list.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def update_task(self):
        selected_task = self.task_listbox.curselection()
        if selected_task:
            selected_task = selected_task[0]
            updated_task = self.task_entry.get()
            if updated_task:
                self.task_list[selected_task] = updated_task
                self.task_listbox.delete(selected_task)
                self.task_listbox.insert(selected_task, updated_task)
                self.task_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "Please enter an updated task.")
        else:
            messagebox.showwarning("Warning", "Please select a task to update.")

    def delete_task(self):
        selected_task = self.task_listbox.curselection()
        if selected_task:
            selected_task = selected_task[0]
            self.task_list.pop(selected_task)
            self.task_listbox.delete(selected_task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please select a task to delete.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()