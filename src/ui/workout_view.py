import tkinter as tk
from tkinter import messagebox
import datetime


class WorkoutUI(tk.Frame):
    """
    Käyttöliittymä harjoituspäiväkirjalle.

    Args:
        tk.Frame: Tkinterin kehysluokka.
    """
    def __init__(self, root, workout_service, user_id, go_back):
        """
        Alustaa WorkoutUI-luokan.

        Args:
            root (Tk): Ikkuna kehykselle.
            workout_service: Harjoituspäiväkirjan käsittelyyn.
            user_id (int): Tunniste käyttäjälle.
            go_back: Palauttaa päävalikkoon.
        """
        super().__init__(root)
        self.workout_service = workout_service
        self.user_id = user_id
        self.go_back = go_back
        self.create_widgets()

    def create_widgets(self):
        """
        Luo widgetit.
        """
        tk.Label(self, text="Harjoituspäiväkirja").pack(pady=10)

        self.workouts_list = tk.Listbox(self, height=10, width=50)
        self.workouts_list.pack(pady=10)

        self.refresh_list()

        tk.Label(self, text="Lisää uusi harjoitus").pack()

        tk.Label(self, text="Päivämäärä:").pack()
        self.date_entry = tk.Entry(self)
        self.date_entry.pack()
        today = datetime.date.today().strftime("%Y-%m-%d")
        self.date_entry.insert(0, today)

        tk.Label(self, text="Harjoitus:").pack()
        self.activity_entry = tk.Entry(self)
        self.activity_entry.pack()

        tk.Label(self, text="Kesto:").pack()
        self.duration_entry = tk.Entry(self)
        self.duration_entry.pack()

        add_button = tk.Button(
            self, text="Lisää harjoitus", command=self.add_workout)
        add_button.pack()

        back_button = tk.Button(self, text="Takaisin", command=self.go_back)
        back_button.pack(pady=10)

    def add_workout(self):
        """
        Lisää harjoituksen käyttäjän päiväkirjaan.
        """
        date = self.date_entry.get()
        activity = self.activity_entry.get()
        duration = self.duration_entry.get()
        success, message = self.workout_service.add_workout(
            self.user_id, date, activity, duration)

        if success:

            messagebox.showinfo("Onnistui", message)
            self.clear_inputs()
            self.refresh_list()
        else:
            messagebox.showerror("Virhe", message)

    def refresh_list(self):
        """
        Päivittää listan käyttäjän harjoituksista.
        """
        self.workouts_list.delete(0, tk.END)
        workouts = self.workout_service.get_workouts(self.user_id)
        for workout in workouts:
            self.workouts_list.insert(
                tk.END, f"{workout['date']} - {workout['activity']} - {workout['duration']} min"
            )
        self.workouts_list.update_idletasks()

    def clear_inputs(self):
        """
        Tyhjentää syötekentät.
        """
        self.activity_entry.delete(0, tk.END)
        self.duration_entry.delete(0, tk.END)
