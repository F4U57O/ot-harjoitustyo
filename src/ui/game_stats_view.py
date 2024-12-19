import os
import tkinter as tk
from tkinter import messagebox, ttk
from tkcalendar import DateEntry


class GameStatsUI(tk.Frame):
    """
    Käyttöliittymä pelitilastojen hallintaan.

    Args:
        tk.Frame: Tkinterin kehysluokka.
    """
    def __init__(self, root, game_stats_service, user_id, go_back):
        """
        Alustaa GameStatsUI-luokan

        Args:
            root (Tk): Ikkuna kehykselle.
            game_stats_service: Pelitilastojen käsittelyyn.
            user_id (int): Tunniste käyttäjälle.
            go_back: Palauttaa edellisen näkymän.
        """
        super().__init__(root)
        self.game_stats_service = game_stats_service
        self.user_id = user_id
        self.go_back = go_back
        self.filepath = os.path.join("data", "teams.txt")
        self.teams = self.load_teams(self.filepath)
        self.create_widgets()

    def create_widgets(self):
        """
        Luo widgetit.
        """
        tk.Label(self, text="Pelitilastot").pack(pady=10)

        list_frame = tk.Frame(self)
        list_frame.pack(pady=10)

        self.stats_list = tk.Listbox(list_frame, height=15, width=100)
        self.stats_list.pack(side="left", fill="both", expand=True)

        scrollbar = tk.Scrollbar(
            list_frame, orient="vertical", command=self.stats_list.yview)
        scrollbar.pack(side="right", fill="y")
        self.stats_list.config(yscrollcommand=scrollbar.set)

        delete_button = tk.Button(
            self, text="Poista", command=self.delete_selected_stat)
        delete_button.pack(pady=5)

        self.total = tk.Label(
            self, text="Pelejä yhteensä: 0, Maaleja yhteensä: 0, Syöttöjä yhteensä: 0, Peliaika yhteensä: 0, Arvosanojen keskiarvo: 0")
        self.total.pack(pady=10)
        self.refresh_list()

        tk.Label(self, text="Lisää uusi pelitilasto").pack(pady=5)
        tk.Label(self, text="Vastustaja:").pack(pady=5)
        self.opponent_combobox = ttk.Combobox(
            self, values=self.teams, state="readonly")
        self.opponent_combobox.pack(pady=10)

        tk.Label(self, text="Päivämäärä:").pack()
        self.date_entry = DateEntry(self, date_pattern='dd-MM-yyyy')
        self.date_entry.pack()

        tk.Label(self, text="Maalit").pack()
        self.goals_spinbox = tk.Spinbox(self, from_=0, to=100, width=5)
        self.goals_spinbox.pack()

        tk.Label(self, text="Syötöt:").pack()
        self.assists_spinbox = tk.Spinbox(self, from_=0, to=100, width=5)
        self.assists_spinbox.pack()

        tk.Label(self, text="Peliaika (min):").pack()
        self.play_time_spinbox = tk.Spinbox(
            self, from_=0, to=100, increment=5, width=5)
        self.play_time_spinbox.pack()

        tk.Label(self, text="Arvosana (1-10):").pack()
        self.rating_slider = tk.Scale(
            self, from_=1, to=10, orient=tk.HORIZONTAL)
        self.rating_slider.pack(pady=5)

        tk.Label(self, text="Palaute:").pack()
        self.feedback_entry = tk.Entry(self)
        self.feedback_entry.pack()

        add_button = tk.Button(
            self, text="Lisää pelitilasto", command=self.add_game_stats)
        add_button.pack(pady=5)

        back_button = tk.Button(self, text="Takaisin", command=self.go_back)
        back_button.pack(pady=10)

    def add_game_stats(self):
        """
        Lisää pelitilaston syötteen perusteella.
        """
        opponent = self.opponent_combobox.get()
        date = self.date_entry.get()
        goals = int(self.goals_spinbox.get())
        assists = int(self.assists_spinbox.get())
        play_time = int(self.play_time_spinbox.get())
        rating = self.rating_slider.get()
        feedback = self.feedback_entry.get()

        game_stats = {
            "opponent": opponent,
            "date": date,
            "goals": goals,
            "assists": assists,
            "play_time": play_time,
            "rating": rating,
            "feedback": feedback
        }

        success, message = self.game_stats_service.add_game_stats(
            game_id=None, user_id=self.user_id, game_stats=game_stats
        )

        if success:
            messagebox.showinfo("Onnistui", message)
            self.clear_inputs()
            self.refresh_list()
        else:
            messagebox.showerror("Virhe", message)

    def refresh_list(self):
        """
        Päivittää pelitilastojen listan ja laskee yhteenvetotiedot.
        """
        self.stats_list.delete(0, tk.END)
        stats = self.game_stats_service.get_game_stats(self.user_id)
        self.stat_ids = []
        total_games = 0
        total_goals = 0
        total_assists = 0
        total_play_time = 0
        total_rating = 0
        rating_count = 0

        for stat in stats:
            self.stats_list.insert(
                tk.END, f"{stat.date} - {stat.opponent} - Maalit: {stat.goals}, Syötöt: {stat.assists}, Peliaika: {stat.play_time} min, Arvosana: {stat.rating}, Palaute: {stat.feedback}"
            )
            self.stat_ids.append(stat.id)

            total_games += 1
            total_goals += stat.goals
            total_assists += stat.assists
            total_play_time += stat.play_time
            total_rating += stat.rating
            rating_count += 1

        average_rating = total_rating / rating_count if rating_count > 0 else 0

        self.total.config(
            text=f"Pelejä yhteensö: {total_games}, Maaleja yhteensä: {total_goals}, Syöttöjä yhteensä: {total_assists}, Peliaika yhteensä: {total_play_time} min, Arvosanojen keskiarvo: {average_rating:.2f}"
        )

    def clear_inputs(self):
        """
        Tyhjentää palautekentän pelitilaston lisäämisen jälkeen.
        """
        self.feedback_entry.delete(0, tk.END)

    def load_teams(self, filepath):
        """
        Lataa joukkueet tiedostosta.

        Args:
            filepath (str): Polku tiedostoon, jossa joukkueiden nimet.

        Returns:
            list[str]: Lista joukkueista.
        """
        try:
            with open(filepath, "r") as file:
                return [line.strip() for line in file if line.strip()]
        except FileNotFoundError:
            return []

    def delete_selected_stat(self):
        """
        Poistaa pelitilaston listasta.
        """
        selected_index = self.stats_list.curselection()
        if not selected_index:
            messagebox.showwarning("Varoitus", "Tilastoa ei valittuna")
            return
        selected_id = self.stat_ids[selected_index[0]]
        confirm = messagebox.askyesno(
            "Varmista Poisto", "Haluatko varmasti poistaa tämän tilaston?")
        if confirm:
            self.game_stats_service.delete_game_stat(selected_id)
            self.refresh_list()
