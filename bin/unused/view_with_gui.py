#!/usr/bin/env python3

import tkinter as tk
from config import *

unit = 'arch'

class DatabaseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Database Viewer")

        # Database connection parameters
        self.dbname = creds['dbname']
        self.user = creds['user']
        self.password = creds['passwd']
        self.host = creds['host']
        self.port = "5432"

        # Create database connection
        try:
            self.conn = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            self.cur = self.conn.cursor()
        except psycopg2.Error as e:
            print("Error connecting to the database:", e)
            self.root.destroy()
            return

        # GUI elements
        self.label = tk.Label(root, text="Row Content:")
        self.label.pack()

        self.row_text = tk.Text(root, height=10, width=80)
        self.row_text.pack()

        self.load_button = tk.Button(root, text="Load Row", command=self.load_row)
        self.load_button.pack()


    def load_row(self):
        # Query to retrieve a row from the database table
        query = f"SELECT id,name,url FROM units WHERE id = '{unit}' LIMIT 1;"
        try:
            self.cur.execute(query)
            row = self.cur.fetchall()  # Retrieve one row
            id,name,url = row[0]
            row_str = (f'ID: {id}\nName: {name}\nURL: {url}')
            self.row_text.delete(1.0, tk.END)
            self.row_text.insert(tk.END, row_str)
            #if row:
            #    #row_str = "\n".join([f"{col}: {val}" for col, val in zip(self.cur.description, row)])
            #    row_str = "\n".join([f"{col}: {val}" for col, val in row])
            #    self.row_text.delete(1.0, tk.END)  # Clear previous content
            #    self.row_text.insert(tk.END, row_str)
            #else:
            #    self.row_text.delete(1.0, tk.END)
            #    self.row_text.insert(tk.END, "No rows found.")
        except psycopg2.Error as e:
            print("Error executing query:", e)

    def __del__(self):
        # Close database connection when the object is deleted
        self.cur.close()
        self.conn.close()

if __name__ == "__main__":
    root = tk.Tk()
    app = DatabaseApp(root)
    root.mainloop()

