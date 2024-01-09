import tkinter as tk
from tkinter import ttk, messagebox

class ExpenseTracker:
    def __init__(self, master):
        self.master = master
        self.master.title("Expense Tracker")

        # Variables
        self.date_var = tk.StringVar()
        self.amount_var = tk.DoubleVar()
        self.description_var = tk.StringVar()

        # Entry Widgets
        tk.Label(master, text="Date:").grid(row=0, column=0, padx=10, pady=5)
        tk.Entry(master, textvariable=self.date_var).grid(row=0, column=1, padx=10, pady=5)

        tk.Label(master, text="Amount:").grid(row=1, column=0, padx=10, pady=5)
        tk.Entry(master, textvariable=self.amount_var).grid(row=1, column=1, padx=10, pady=5)

        tk.Label(master, text="Description:").grid(row=2, column=0, padx=10, pady=5)
        tk.Entry(master, textvariable=self.description_var).grid(row=2, column=1, padx=10, pady=5)

        # Button
        tk.Button(master, text="Add Expense", command=self.add_expense).grid(row=3, column=0, columnspan=2, pady=10)

        # Expense Table
        columns = ("Date", "Description", "Amount")
        self.tree = ttk.Treeview(master, columns=columns, show="headings", selectmode="browse")

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100, anchor="center")

        self.tree.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        # Total Expenses Label
        self.total_label = tk.Label(master, text="Total Expenses: $0.00")
        self.total_label.grid(row=5, column=0, columnspan=2, pady=5)

        # Initialize total expenses
        self.total_expenses = 0.0

    def add_expense(self):
        try:
            date = self.date_var.get()
            amount = self.amount_var.get()
            description = self.description_var.get()

            if date and amount and description:
                # Update table
                self.tree.insert("", "end", values=(date, description, f"${amount:.2f}"))

                # Update total expenses
                self.total_expenses += amount
                self.total_label.config(text=f"Total Expenses: ${self.total_expenses:.2f}")

                # Clear entry fields
                self.date_var.set("")
                self.amount_var.set(0.0)
                self.description_var.set("")
            else:
                messagebox.showwarning("Warning", "Please fill in all the fields.")
        except ValueError:
            messagebox.showwarning("Warning", "Please enter a valid amount.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTracker(root)
    root.mainloop()
