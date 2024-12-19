import tkinter as tk
from tkinter import messagebox
from services.register_service import RegisterService
from repositories.user_repository import UserRepository


class RegisterUI(tk.Frame):
    """
    Käyttöliittymä rekisteröinnille.

    Args:
        tk.Frame: Tkinterin kehysluokka.
    """
    def __init__(self, root, app):
        """
        Alustaa RegisterUI-luokan.

        Args:
            root (Tk): Ikkuna kehykselle.
            app (App): Pääluokka, jota käytetään näkymän vaihtamiseen.
        """
        super().__init__(root)
        self.app = app
        self.user_repo = UserRepository()
        self.register = RegisterService(self.user_repo)
        self.create_widgets()

    def create_widgets(self):
        """
        Luo widgetit.
        """
        tk.Label(self, text="Käyttäjätunnus").pack()
        self.entry_username = tk.Entry(self)
        self.entry_username.pack()

        tk.Label(self, text="Salasana").pack()
        self.entry_password = tk.Entry(self, show="*")
        self.entry_password.pack()

        register_button = tk.Button(
            self, text="Rekisteröidy", command=self.register_user)
        register_button.pack()

        back_button = tk.Button(self, text="Takaisin",
                                command=self.app.show_main_menu)
        back_button.pack(pady=5)

    def register_user(self):
        """
        Käsittelee käyttäjän rekisteröitymisen.
        """
        username = self.entry_username.get()
        password = self.entry_password.get()
        success, message = self.register.register_user(username, password)

        if success:
            messagebox.showinfo("Rekisteröinti", message)
            self.app.show_main_menu()
        else:
            messagebox.showerror("Virhe", message)
