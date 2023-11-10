import tkinter as tk
from tkinter import messagebox
#from ttkthemes import ThemedStyle  # Import ThemedStyle from ttkthemes
from PIL import ImageTk
import pymysql

def leaderboard_page():
    root.destroy()
    import leader2

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Application")
        self.root.geometry("800x600")
        background=ImageTk.PhotoImage(file='.github/bgg1.png')
        self.root.bgLabel=tk.Label(root,image=background)
        self.current_question = 0
        self.score = 0

        self.questions = [
            {
                'question': "1. What is the chemical symbol for gold?",
                'options': ["Au", "Ag", "Fe", "Hg"],
                'correct_option': 0
            },
            {
                'question': "2. Which gas makes up the majority of Earth's atmosphere?",
                'options': ["Oxygen", "Nitrogen", "Carbon dioxide", "Hydrogen"],
                'correct_option': 1
            },
            {
                'question': "3. What is the smallest planet in our solar system?",
                'options': ["Mars", "Earth", "Venus", "Mercury"],
                'correct_option': 3
            },
            {
                'question': "4. What is the process by which plants make their own food using sunlight?",
                'options': ["Respiration", "Photosynthesis", "Digestion", "Fermentation"],
                'correct_option': 1
            },
            {
                'question': "5. Which gas do plants absorb from the atmosphere during photosynthesis?",
                'options': ["Carbon dioxide", "Oxygen", "Nitrogen", "Hydrogen"],
                'correct_option': 0
            },
            {
                'question': "6. What is the chemical symbol for water?",
                'options': ["Wo", "Wt", "H2O", "H2SO4"],
                'correct_option': 2
            },
            {
                'question': "7. Which planet is known as the 'Red Planet' due to its reddish appearance?",
                'options': ["Mars", "Jupiter", "Venus", "Saturn"],
                'correct_option': 0
            },
            {
                'question': "8. The study of earthquakes is known as:",
                'options': ["Meteorology", "Volcanology", "Seismology", "Paleontology"],
                'correct_option': 2
            },
            {
                'question': "9. What is the closest star to Earth?",
                'options': ["Alpha Centauri", "Proxima Centauri", "Betelgeuse", "Sirius"],
                'correct_option': 1
            },
            {
                'question': "10. What is the chemical symbol for oxygen?",
                'options': ["O2", "Ox", "O", "Oz"],
                'correct_option': 0
            }
        ]
        self.question_label = tk.Label(root, text="",font=("Arial", 16))
        self.question_label.pack(pady=50)

        self.var = tk.IntVar()
        self.var.set(-1)

        self.radio_buttons = []  # Store the radiobuttons

        for i in range(4):
            
            option_frame = tk.Frame(root)
            option_frame.pack(anchor="w",padx=50)  # Align the frame to the left

            radio = tk.Radiobutton(option_frame, variable=self.var, value=i)
            radio.pack(side="left")  # Align the radio button to the left

            text = tk.Label(option_frame, text="", anchor="w")
            text.pack(side="left")  # Align the text to the left

            self.radio_buttons.append((radio, text))
        
        self.prev_button = tk.Button(root, text="Previous", font=("Arial", 16) ,fg='white',bg='lightblue',activebackground='darkblue',activeforeground='white',cursor='hand2', command=self.previous_question ,state=tk.DISABLED)
        self.prev_button.pack(side=tk.LEFT,pady=10,padx=100)

        self.next_button = tk.Button(root, text="Next", font=("Arial", 16) ,fg='white',bg='lightblue',activebackground='darkblue',activeforeground='white',cursor='hand2', command=self.next_question)
        self.next_button.pack(side=tk.LEFT,pady=10,padx=100)
        
        self.submit_button = tk.Button(root, text="Submit", font=("Arial", 16) ,fg='white',bg='lightblue',activebackground='darkblue',activeforeground='white',cursor='hand2', command=self.submit_quiz ,state=tk.DISABLED)
        self.submit_button.pack(side=tk.LEFT,pady=10,padx=70)
        

    def submit_quiz(self):
        messagebox.showinfo("Quiz Over", f"Your final score is {self.score}/{len(self.questions)}")
        command=leaderboard_page
        self.root.quit()

    def next_question(self):
        if self.var.get() == -1:
            messagebox.showinfo("Message", "Please select an option.")
            return

        if self.questions[self.current_question]['correct_option'] == self.var.get():
            self.score += 1

        self.current_question += 1
        self.var.set(-1)

        if self.current_question < len(self.questions):
            self.show_question()
            # Enable "Previous" button when moving to the next question
            self.prev_button["state"] = tk.NORMAL
        else:
            self.next_button.pack_forget()
            self.submit_button["state"] = tk.NORMAL
            self.submit_button.pack(pady=10)
        
    def previous_question(self):
        if self.current_question > 0:
            self.current_question -= 1
            self.show_question()
            self.prev_button["state"] = tk.NORMAL
            
        else:
            self.prev_button["state"] = tk.DISABLED  # Disable the "Previous" button

    def show_question(self):
        question = self.questions[self.current_question]
        self.question_label.config(text=question['question'], justify="center")
        
        for i, (radio, text) in enumerate(self.radio_buttons):
            radio.config(variable=self.var, value=i)
            text.config(text=question['options'][i], font=("Arial", 16), anchor="w")


if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    app.show_question()
    root.mainloop()


