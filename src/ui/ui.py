import tkinter as tk
from ui.register_view import RegisterUI
from ui.login_view import LoginUI
from ui.main_view import MainPageView
from ui.workout_view import WorkoutUI
from ui.game_stats_view import GameStatsUI
from ui.goal_view import GoalUI
from services.workout_service import WorkoutService
from repositories.workout_repository import WorkoutRepository
from services.game_stats_service import GameStatsService
from repositories.game_stats_repository import GameStatsRepository
from services.goal_service import GoalService
from repositories.goal_repository import GoalRepository


class MainApp:
    def __init__(self, root):
        self.root = root
        self.current_frame = None
        self.current_user = None
        self.show_main_menu()

    def change_frame(self, frame):
        if self.current_frame:
            self.current_frame.destroy()
        self.current_frame = frame
        self.current_frame.pack(fill="both", expand=True)

    def show_main_menu(self):
        menu_frame = tk.Frame(self.root)

        tk.Label(menu_frame, text="Tervetuloa! Valitse toiminto:").pack(pady=10)
        tk.Button(menu_frame, text="Rekisteröidy",
                  command=lambda: self.show_register_window()).pack(pady=5)
        tk.Button(menu_frame, text="Kirjaudu",
                  command=lambda: self.show_login_window()).pack(pady=5)

        self.change_frame(menu_frame)

    def show_register_window(self):
        register_view = RegisterUI(self.root, self)
        self.change_frame(register_view)

    def show_login_window(self):
        login_view = LoginUI(self.root, self)
        self.change_frame(login_view)

    def show_main_page(self, user):
        self.current_user = user
        main_page = MainPageView(
            self.root, user, self.log_out, self.show_workout_window, self.show_game_stats_window, self.show_goal_window)
        self.change_frame(main_page)

    def show_workout_window(self):
        workout_service = WorkoutService(WorkoutRepository())
        workout_view = WorkoutUI(self.root, workout_service, self.current_user,
                                 lambda: self.show_main_page(self.current_user))
        self.change_frame(workout_view)

    def show_game_stats_window(self):
        game_stats_service = GameStatsService(GameStatsRepository())
        game_stats_view = GameStatsUI(
            self.root, game_stats_service, self.current_user, lambda: self.show_main_page(self.current_user))
        self.change_frame(game_stats_view)

    def show_goal_window(self):
        goal_service = GoalService(GoalRepository())
        goal_view = GoalUI(self.root, goal_service, self.current_user,
                           lambda: self.show_main_page(self.current_user))
        self.change_frame(goal_view)

    def log_out(self):
        self.current_user = None
        self.show_main_menu()
