import tkinter as tk
from tkinter import messagebox, ttk


class GoalUI(tk.Frame):
    def __init__(self, root, goal_service, user_id, go_back):
        super().__init__(root)
        self.goal_service = goal_service
        self.user_id = user_id
        self.go_back = go_back

        self.goal_entry = tk.Entry(self)
        self.goal_entry.grid(row=0, column=1)

        back_button = tk.Button(self, text="Takaisin", command=self.go_back)
        back_button.grid(row=4, column=1)

        add_button = tk.Button(
            self, text="Lisää tavoite", command=self.add_goal)
        add_button.grid(row=1, column=1)

        self.goals_list = ttk.Treeview(self, columns=(
            "id", "Goal", "Status", "Created At", "Status Updated At"), show="headings")
        self.goals_list.heading("id", text="id")
        self.goals_list.heading("Goal", text="Tavoite")
        self.goals_list.heading("Status", text="Tila")
        self.goals_list.heading("Created At", text="Luotu")
        self.goals_list.heading("Status Updated At", text="Tila päivitetty")
        self.goals_list.column("id", width=0)
        self.goals_list.grid(row=2, column=1, sticky="nsew")
        self.goals_list.bind("<Double-1>", self.edit_status)

        update_button = tk.Button(
            self, text="Päivitä tila", command=self.update_status)
        update_button.grid(row=3, column=1)

        self.status_combobox = None
        self.current_goal_id = None

        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.goals_list.tag_configure("käynnissä", foreground="black")
        self.goals_list.tag_configure("suoritettu", foreground="green")
        self.goals_list.tag_configure("ei suoritettu", foreground="red")

        self.refresh_goals()

    def add_goal(self):
        goal = self.goal_entry.get()
        success, message = self.goal_service.add_goal(self.user_id, goal)
        messagebox.showinfo("Ilmoitus", message)
        if success:
            self.refresh_goals()

    def edit_status(self, event):
        if self.status_combobox:
            self.status_combobox.destroy()

        selected_item = self.goals_list.selection()
        if not selected_item:
            return

        item = self.goals_list.item(selected_item)
        goal_id = item["values"][0]
        current_status = item["values"][2]

        self.status_combobox = ttk.Combobox(
            self, values=["käynnissä", "suoritettu", "ei suoritettu"])
        self.status_combobox.set(current_status)
        self.status_combobox.grid(row=2, column=1)
        self.current_goal_id = goal_id

    def update_status(self):
        if not self.current_goal_id or not self.status_combobox:
            messagebox.showinfo("Ilmoitus", "Valitse tila muokattavaksi!")
            return

        new_status = self.status_combobox.get()
        goal_id = self.current_goal_id

        success, message = self.goal_service.update_goal_status(
            goal_id, new_status)
        messagebox.showinfo("Ilmoitus", message)

        if success:
            self.refresh_goals()

        self.status_combobox.destroy()
        self.status_combobox = None
        self.current_goal_id = None

    def refresh_goals(self):
        for item in self.goals_list.get_children():
            self.goals_list.delete(item)
        goals = self.goal_service.get_user_goals(self.user_id)
        for goal in goals:
            if goal["status"] == "käynnissä":
                tag = "käynnissä"
            elif goal["status"] == "suoritettu":
                tag = "suoritettu"
            else:
                tag = "ei suoritettu"
            self.goals_list.insert("", "end", values=(
                goal["id"], goal["goal"], goal["status"], goal["created_at"], goal["status_updated_at"]), tags=(tag,))
