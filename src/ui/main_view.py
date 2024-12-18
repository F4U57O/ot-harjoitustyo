import tkinter as tk
from tkinter import ttk
from ui.workout_view import WorkoutUI
from repositories.workout_repository import WorkoutRepository
from services.workout_service import WorkoutService


class MainPageView(tk.Frame):
    """
    Käyttöliittymä sovelluksen pääsivulle.

    Args:
        tk.Frame: Tkinterin kehysluokka.
    """
    def __init__(self, root, user, log_out_callback, show_workout, show_game_stats, show_goal):
        """
        Alustaa MainPageView-luokan.

        Args:
            root (Tk): Ikkuna kehykselle.
            user (str): Käyttäjätunnus.
            log_out_callback: Uloskirjautuimnen.
            show_workout: Näyttää harjoituspäiväkirjan.
            show_game_stats: Näyttää pelitilastot.
            show_goal: Näyttää tavoitteet.
        """
        super().__init__(root)
        self.user = user
        self.log_out_callback = log_out_callback
        self.root = root
        self.show_workout = show_workout
        self.show_game_stats = show_game_stats
        self.show_goal = show_goal
        self.workout_repo = WorkoutRepository()
        self.workout_service = WorkoutService(self.workout_repo)
        self.create_main_page()

    def create_main_page(self):
        """
        Luo pääsivun elementit.
        """
        tk.Label(self, text=f"Tervetuloa, {self.user}!").pack(pady=10)
        workout_button = tk.Button(
            self, text="Harjoituspäiväkirja",
            command=self.show_workout)
        workout_button.pack(pady=10)

        stats_button = tk.Button(
            self, text="Pelitilastot", command=self.show_game_stats)
        stats_button.pack(pady=10)

        goal_button = tk.Button(self, text="Tavoitteet",
                                command=self.show_goal)
        goal_button.pack(pady=10)

        log_out_button = tk.Button(
            self, text="Kirjaudu ulos", command=self.log_out_callback)
        log_out_button.pack(pady=20)

    def log_out(self):
        """
        Mahdollistaa uloskirjautumisen.
        """
        self.log_out_callback()
