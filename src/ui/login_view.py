import tkinter as tk
from tkinter import messagebox
from login import Login
from repositories.user_repository import UserRepository

class LoginUI(tk.Frame):
  def __init__(self, root, app):
      super().__init__(root)
      self.app = app
      self.user_repo = UserRepository()
      self.login = Login(self.user_repo)
      self.create_widgets()

  def create_widgets(self):
    tk.Label(self, text="Käyttäjätunnus").pack()
    self.entry_username = tk.Entry(self)
    self.entry_username.pack()

    tk.Label(self, text="Salasana").pack()
    self.entry_password = tk.Entry(self, show="*")
    self.entry_password.pack()

    login_button = tk.Button(self, text="Kirjaudu", command=self.login_user)
    login_button.pack()

    back_button = tk.Button(self, text="Takaisin", command=self.app.show_main_menu)
    back_button.pack(pady=5)


  def login_user(self):
    username = self.entry_username.get()
    password = self.entry_password.get()

    success, message = self.login.login_user(username, password)

    if success:
      messagebox.showinfo("Kirjautuminen", message)
      self.app.show_main_page(username)
    else:
      messagebox.showerror("Virhe", message)