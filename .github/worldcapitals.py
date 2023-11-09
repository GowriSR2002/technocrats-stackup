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
        background=ImageTk.PhotoImage(file='.github/bg1.png')
        self.root.bgLabel=tk.Label(root,image=background)
        self.current_question = 0
        self.score = 0

        self.questions = [
            {
                'question': "1. What is the capital of France?",
                'options': ["Paris", "Berlin", "Madrid", "Rome"],
                'correct_option': 0
            },
            {
                'question': "2. The capital of Japan is:",
                'options': ["Tokyo", "Beijing", "Seoul", "Bangkok"],
                'correct_option': 0
            },
            {
                'question': "3. What is the capital of Australia?",
                'options': ["Sydney", "Melbourne", "Canberra", "Brisbane"],
                'correct_option': 2
            },
            {
                'question': "4. Which city serves as the capital of Brazil?",
                'options': ["Rio de Janeiro", "Sao Paulo", "Brasilia", "Salvador"],
                'correct_option': 2
            },
            {
                'question': "5. The capital of South Africa is:",
                'options': ["Cape Town", "Pretoria", "Durban", "Johannesburg"],
                'correct_option': 2
            },
            {
                'question': "6. The capital of Egypt is:",
                'options': ["Cairo", "Alexandria", "Giza", "Luxor"],
                'correct_option': 0
            },
            {
                'question': "7. What city serves as the capital of Canada?",
                'options': ["Toronto", "Vancouver", "Ottawa", "Montreal"],
                'correct_option': 2
            },
            {
                'question': "8. The capital of India is:",
                'options': ["Delhi", "Mumbai", "Bangalore", "Kolkata"],
                'correct_option': 0
            },
            {
                'question': "9. What is the capital of Russia?",
                'options': ["St. Petersburg", "Moscow", "Vladivostok", "Kiev"],
                'correct_option': 1
            },
            {
                'question': "10. What is the capital of Argentina?",
                'options': ["Buenos Aires", "Santiago", "Lima", "Montevideo"],
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
        
        self.prev_button = tk.Button(root, text="Previous", font=("Arial", 16), command=self.previous_question ,state=tk.NORMAL)
        self.prev_button.pack(pady=10)

        self.next_button = tk.Button(root, text="Next",font=("Arial", 16), command=self.next_question)
        self.next_button.pack(pady=10)
        
        self.prev_button = tk.Button(root, text="Submit", font=("Arial", 16), command=self.submit_quiz ,state=tk.NORMAL)
        self.prev_button.pack(pady=10)

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
            self.submit_button.pack(pady=10)
            '''
            messagebox.showinfo("Quiz Over", f"Your score is {self.score}/{len(self.questions)}")
            self.next_button["state"] = tk.DISABLED
            self.submit_button["state"] = tk.NORMAL
            self.root.quit()
'''
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
