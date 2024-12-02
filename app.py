
import tkinter as tk
from tkinter import ttk, messagebox
import pyodbc
import json
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"
    
class AzureDBApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Azure DB Connector")
        self.geometry("400x500")
        self.resizable(True, True)
        
        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self, text="Azure Database Connector", font=("Helvetica", 16)).pack(pady=20)
        
        ttk.Label(self, text="Server Name:").pack(anchor="w", padx=20)
        self.server_entry = ttk.Entry(self, width=40)
        self.server_entry.pack(padx=20, pady=5)

        ttk.Label(self, text="Database Name:").pack(anchor="w", padx=20)
        self.database_entry = ttk.Entry(self, width=40)
        self.database_entry.pack(padx=20, pady=5)

        ttk.Label(self, text="Username:").pack(anchor="w", padx=20)
        self.username_entry = ttk.Entry(self, width=40)
        self.username_entry.pack(padx=20, pady=5)

        ttk.Label(self, text="Password:").pack(anchor="w", padx=20)
        self.password_entry = ttk.Entry(self, width=40, show="*")
        self.password_entry.pack(padx=20, pady=5)

        ttk.Button(self, text="Connect to Database", command=self.connect_to_db).pack(pady=20)
        ttk.Button(self, text="Load Default Credentials", command=self.load_credentials).pack()

    def load_credentials(self):
        try:
            with open("azure_credentials.json", "r") as file:
                creds = json.load(file)
                self.server_entry.delete(0, tk.END)
                self.server_entry.insert(0, creds["ServerName"])
                self.database_entry.delete(0, tk.END)
                self.database_entry.insert(0, creds["DatabaseName"])
                self.username_entry.delete(0, tk.END)
                self.username_entry.insert(0, creds["AdminUsername"])
                self.password_entry.delete(0, tk.END)
                self.password_entry.insert(0, creds["AdminPassword"])
                messagebox.showinfo("Success", "Default credentials loaded successfully!")
        except FileNotFoundError:
            messagebox.showerror("Error", "Credentials file not found!")

    def connect_to_db(self):
        server = self.server_entry.get()
        database = self.database_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()

        try:
            conn_str = (
                f"Driver={{ODBC Driver 18 for SQL Server}};"
                f"Server=tcp:{server},1433;"  # Fixed port reference
                f"Database={database};"
                f"Uid={username};"
                f"Pwd={password};"
                f"Encrypt=yes;"
                f"TrustServerCertificate=no;"
            )
            conn = pyodbc.connect(conn_str)
            messagebox.showinfo("Connection Success", "Connected to Azure SQL Database successfully!")
            conn.close()
        except Exception as e:
            messagebox.showerror("Connection Error", str(e))

if __name__ == "__main__":
    app = AzureDBApp()
    app.mainloop()
