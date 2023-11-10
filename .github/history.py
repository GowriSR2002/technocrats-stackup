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
                'question': "1. Who was the first President of the United States?",
                'options': ["Thomas Jefferson", "John Adams", "George Washington", "Benjamin Franklin"],
                'correct_option': 2
            },
            {
                'question': "2. Which ancient civilization is known for building the Great Wall of China?",
                'options': ["Mesopotamia", "Greece", "Egypt", "China"],
                'correct_option': 3
            },
            {
                'question': "3. In which year did Christopher Columbus first voyage to the Americas?",
                'options': ["1492", "1620", "1776", "1812"],
                'correct_option': 0
            },
            {
                'question': "4. Who was the first woman to fly solo across the Atlantic Ocean?",
                'options': ["Bessie Coleman", "Amelia Earhart", "Harriet Quimby", "Jacqueline Cochran"],
                'correct_option': 1
            },
            {
                'question': "5. Which event marked the beginning of World War I in 1914?",
                'options': ["The sinking of the Titanic", "The assassination of Archduke Franz Ferdinand", 
                             "The signing of the Treaty of Versailles", "The Battle of the Somme"],
                'correct_option': 1
            },
            {
                'question': "6. The Renaissance, a cultural and intellectual movement, began in which European city?",
                'options': ["Paris", "Venice", "Florence", "Athens"],
                'correct_option': 2
            },
            {
                'question': "7. Who is known for leading the nonviolent civil rights movement in the United States during the 1960s?",
                'options': ["Martin Luther King Jr.", "Malcolm X", "Nelson Mandela", "Mahatma Gandhi"],
                'correct_option': 0
            },
            {
                'question': "8. The Industrial Revolution began in which country during the late 18th century?",
                'options': ["France", "Germany", "United Kingdom", "United States"],
                'correct_option': 2
            },
            {
                'question': "9. Which famous explorer was the first to circumnavigate the Earth?",
                'options': ["Vasco da Gama", "Ferdinand Magellan", "Marco Polo", "Christopher Columbus"],
                'correct_option': 1
            },
            {
                'question': "10. Who was the leader of the Soviet Union during the Cuban Missile Crisis?",
                'options': ["Vladimir Putin", "Joseph Stalin", "Nikita Khrushchev", "Leon Trotsky"],
                'correct_option': 2
            },
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

        self.timer_label = tk.Label(root, text="Timer: 0:00", font=("Arial", 14))
        self.timer_label.pack( padx=10, pady=10)

        self.timer_seconds = 0
        self.timer_running = False
        
        self.prev_button = tk.Button(root, text="Previous", font=("Arial", 16),bg='lightblue',activebackground='darkblue',activeforeground='white',cursor='hand2', command=self.previous_question ,state=tk.DISABLED)
        self.prev_button.pack(side=tk.LEFT,pady=10,padx=100)

        self.next_button = tk.Button(root, text="Next", font=("Arial", 16) ,bg='lightblue',activebackground='darkblue',activeforeground='white',cursor='hand2', command=self.next_question)
        self.next_button.pack(side=tk.LEFT,pady=10,padx=100)
        
        self.submit_button = tk.Button(root, text="Submit", font=("Arial", 16) ,bg='lightblue',activebackground='darkblue',activeforeground='white',cursor='hand2', command=self.submit_quiz ,state=tk.DISABLED)
        self.submit_button.pack(side=tk.LEFT,pady=10,padx=70)


        
    def start_timer(self):
        self.timer_running = True
        self.update_timer()

    def stop_timer(self):
        self.timer_running = False

    def update_timer(self):
        if self.timer_running:
            minutes = self.timer_seconds // 60
            seconds = self.timer_seconds % 60
            timer_text = f"Timer: {minutes}:{seconds:02d}"
            self.timer_label.config(text=timer_text)
            self.timer_seconds += 1
            self.root.after(1000, self.update_timer)

    def submit_quiz(self):
        # Stop the timer when the quiz is submitted
        self.stop_timer()
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
        # Start the timer when the first question is shown
        if not self.timer_running:
            self.start_timer()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    app.show_question()
    root.mainloop()
