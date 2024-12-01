import tkinter as tk
from ui.ui import MainApp


def main():
    window = tk.Tk()
    window.title("fBallers App")
    window.geometry("1200x1000")

    app = MainApp(window)
    app.show_main_menu()

    window.mainloop()


if __name__ == "__main__":
    main()
