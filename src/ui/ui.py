import tkinter as tk
from ui.register_view import RegisterUI
from ui.login_view import LoginUI
from views import MainPageView

class MainApp:
  def __init__(self, root):
    self.root = root
    self.current_frame = None
    self.current_user = None


  def change_frame(self, frame):
    if self.current_frame:
      self.current_frame.destroy()
    self.current_frame = frame
    self.current_frame.pack(fill="both", expand=True)


  def show_main_menu(self):
    menu_frame = tk.Frame(self.root)

    tk.Label(menu_frame, text="Tervetuloa! Valitse toiminto:").pack(pady=10)
    tk.Button(menu_frame, text="Rekisteröidy", command=lambda: self.show_register_window()).pack(pady=5)
    tk.Button(menu_frame, text="Kirjaudu", command=lambda: self.show_login_window()).pack(pady=5)

    self.change_frame(menu_frame)

  def show_register_window(self):
    register_view = RegisterUI(self.root, self)
    self.change_frame(register_view)

  def show_login_window(self):
    login_view = LoginUI(self.root, self)
    self.change_frame(login_view)

  def show_main_page(self, user):
    self.current_user = user
    main_page = MainPageView(self.root, user, self.log_out)
    self.change_frame(main_page)

  def log_out(self):
    self.current_user = None
    self.show_main_menu()