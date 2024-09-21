import tkinter as tk
from tkinter import messagebox

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, name):
        if name in self.accounts:
            return False
        self.accounts[name] = 0
        return True

    def get_balance(self, name):
        return self.accounts.get(name, None)

    def deposit(self, name, amount):
        if name in self.accounts and amount > 0:
            self.accounts[name] += amount
            return True
        return False

    def withdraw(self, name, amount):
        if name in self.accounts and 0 < amount <= self.accounts[name]:
            self.accounts[name] -= amount
            return True
        return False

    def transfer(self, from_name, to_name, amount):
        if from_name in self.accounts and to_name in self.accounts and 0 < amount <= self.accounts[from_name]:
            self.accounts[from_name] -= amount
            self.accounts[to_name] += amount
            return True
        return False

class BankApp:
    def __init__(self, root):
        self.bank = Bank()
        self.root = root
        self.root.title("Bank App")

        # Widgets for account management
        tk.Label(root, text="Account Name:").pack()
        self.account_name_entry = tk.Entry(root)
        self.account_name_entry.pack()

        tk.Button(root, text="Create Account", command=self.create_account).pack()

        tk.Label(root, text="Account Name for Balance/Transfer/Withdrawal:").pack()
        self.account_name_action_entry = tk.Entry(root)
        self.account_name_action_entry.pack()

        tk.Button(root, text="Check Balance", command=self.check_balance).pack()
        tk.Label(root, text="Amount:").pack()
        self.amount_entry = tk.Entry(root)
        self.amount_entry.pack()

        tk.Button(root, text="Deposit", command=self.deposit).pack()
        tk.Button(root, text="Withdraw", command=self.withdraw).pack()

        tk.Label(root, text="Transfer To Account:").pack()
        self.transfer_to_entry = tk.Entry(root)
        self.transfer_to_entry.pack()

        tk.Button(root, text="Transfer", command=self.transfer).pack()

        tk.Button(root, text="Quit", command=self.root.quit).pack()

    def create_account(self):
        name = self.account_name_entry.get()
        if self.bank.create_account(name):
            messagebox.showinfo("Success", f"Account '{name}' created successfully!")
        else:
            messagebox.showerror("Error", "Account already exists.")

    def check_balance(self):
        name = self.account_name_action_entry.get()
        balance = self.bank.get_balance(name)
        if balance is not None:
            messagebox.showinfo("Balance", f"Balance for '{name}': ${balance:.2f}")
        else:
            messagebox.showerror("Error", "Account not found.")

    def deposit(self):
        name = self.account_name_action_entry.get()
        try:
            amount = float(self.amount_entry.get())
            if self.bank.deposit(name, amount):
                messagebox.showinfo("Success", "Deposit successful!")
            else:
                messagebox.showerror("Error", "Invalid account or deposit amount.")
        except ValueError:
            messagebox.showerror("Error", "Invalid amount entered.")

    def withdraw(self):
        name = self.account_name_action_entry.get()
        try:
            amount = float(self.amount_entry.get())
            if self.bank.withdraw(name, amount):
                messagebox.showinfo("Success", "Withdrawal successful!")
            else:
                messagebox.showerror("Error", "Insufficient funds or invalid account.")
        except ValueError:
            messagebox.showerror("Error", "Invalid amount entered.")

    def transfer(self):
        from_name = self.account_name_action_entry.get()
        to_name = self.transfer_to_entry.get()
        try:
            amount = float(self.amount_entry.get())
            if self.bank.transfer(from_name, to_name, amount):
                messagebox.showinfo("Success", "Transfer successful!")
            else:
                messagebox.showerror("Error", "Transfer failed. Check account details or balance.")
        except ValueError:
            messagebox.showerror("Error", "Invalid amount entered.")

if __name__ == "__main__":
    root = tk.Tk()
    app = BankApp(root)
    root.mainloop()
 