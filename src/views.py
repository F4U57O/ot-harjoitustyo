import tkinter as tk

class MainPageView(tk.Frame):
  def __init__(self, root, user, log_out_callback):
    super().__init__(root)
    self.user = user
    self.log_out_callback = log_out_callback
    self.root = root
    self.create_main_page()

  def create_main_page(self):
    tk.Label(self, text=f"Tervetuloa, {self.user}!").pack(pady=10)

    log_out_button = tk.Button(self, text="Kirjaudu ulos", command=self.log_out_callback)
    log_out_button.pack(pady=20)
