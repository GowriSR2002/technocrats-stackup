import tkinter as tk
from PIL import ImageTk
from tkinter import messagebox

class QuizLeaderboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Leaderboard")
        self.root.geometry('990x600+50+50')
        bgImage=ImageTk.PhotoImage(file='.github/bg1.png')
        self.root.bgLabel=tk.Label(root,image=bgImage)
        self.root.configure(bg="#FFD1DC")  # Set background color to light pink

        # Quiz variables
        self.current_player = tk.StringVar()
        self.current_score = tk.StringVar()
        self.current_player.set("Player 1")
        self.current_score.set(0)

        # Leaderboard data
        self.leaderboard_data = {"Player 1": 0, "Player 2": 0, "Player 3": 0, "Player 4": 0}

        # UI elements
        self.quiz_frame = tk.Frame(self.root, padx=20, pady=20, bg="#FFD1DC")  # Set frame background color
        self.quiz_frame.pack()

        self.leaderboard_frame = tk.Frame(self.root, padx=20, pady=20, bg="#FFD1DC")  # Set frame background color
        self.leaderboard_frame.pack()

        self.create_quiz_interface()
        self.create_leaderboard()

    def create_quiz_interface(self):
        quiz_label = tk.Label(self.quiz_frame, text="Quiz Interface", font=("Helvetica", 16), bg="#FFD1DC")
        quiz_label.grid(row=0, column=0, columnspan=2, pady=10)

        player_label = tk.Label(self.quiz_frame, text="Current Player:", bg="#FFD1DC")
        player_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")

        player_entry = tk.Entry(self.quiz_frame, textvariable=self.current_player, state="readonly")
        player_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        score_label = tk.Label(self.quiz_frame, text="Current Score:", bg="#FFD1DC")
        score_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")

        score_entry = tk.Entry(self.quiz_frame, textvariable=self.current_score, state="readonly")
        score_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        add_button = tk.Button(self.quiz_frame, text="Add Score", command=self.add_score)
        add_button.grid(row=3, column=0, columnspan=2, pady=10)

        view_button = tk.Button(self.quiz_frame, text="View Scores", command=self.view_scores)
        view_button.grid(row=4, column=0, columnspan=2, pady=10)

    def create_leaderboard(self):
        leaderboard_label = tk.Label(self.leaderboard_frame, text="Leaderboard", font=("Helvetica", 16), bg="#FFD1DC")
        leaderboard_label.grid(row=0, column=0, columnspan=2, pady=10)

        for index, (player, score) in enumerate(self.leaderboard_data.items(), start=1):
            player_label = tk.Label(self.leaderboard_frame, text=player, bg="#FFD1DC")
            player_label.grid(row=index, column=0, padx=10, pady=5, sticky="w")

            score_label = tk.Label(self.leaderboard_frame, text=score, bg="#FFD1DC")
            score_label.grid(row=index, column=1, padx=10, pady=5, sticky="e")

    def add_score(self):
        try:
            new_score = int(self.current_score.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid score.")
            return

        current_player = self.current_player.get()

        if current_player in self.leaderboard_data:
            self.leaderboard_data[current_player] += new_score
            # Sort the leaderboard based on scores
            sorted_leaderboard = sorted(self.leaderboard_data.items(), key=lambda x: x[1], reverse=True)
            self.leaderboard_data = dict(sorted_leaderboard)

            # Update the leaderboard UI
            for index, (player, score) in enumerate(sorted_leaderboard, start=1):
                self.leaderboard_frame.grid_forget()
                self.create_leaderboard()

            # Reset current player and score
            self.current_player.set("Player 1")
            self.current_score.set(0)
        else:
            messagebox.showerror("Error", "Invalid player. Please select a player from the leaderboard.")

    def view_scores(self):
        current_player = self.current_player.get()
        if current_player in self.leaderboard_data:
            score = self.leaderboard_data[current_player]
            messagebox.showinfo("Player Scores", f"{current_player}'s Score: {score}")
        else:
            messagebox.showerror("Error", "Invalid player. Please select a player from the leaderboard.")

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizLeaderboard(root)
    root.mainloop()
