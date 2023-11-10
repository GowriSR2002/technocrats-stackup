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
                'question': "1. 'Here's looking at you, kid' is a famous line from which classic movie?",
                'options': ["Gone with the Wind", "Casablanca", "The Godfather", "Citizen Kane"],
                'correct_option': 1
            },
            {
                'question': "2. Which movie features the quote, 'May the Force be with you'?",
                'options': ["Star Wars", "E.T. the Extra-Terrestrial", "Jurassic Park", "Indiana Jones and the Last Crusade"],
                'correct_option': 0
            },
            {
                'question': "3. 'You can't handle the truth!' is a memorable quote from which legal drama film?",
                'options': ["A Few Good Men", "12 Angry Men", "To Kill a Mockingbird", "My Cousin Vinny"],
                'correct_option': 0
            },
            {
                'question': "4. In which film does the character James Bond famously say, 'Shaken, not stirred'?",
                'options': ["Goldfinger", "Dr. No", "Casino Royale", "The Spy Who Loved Me"],
                'correct_option': 0
            },
            {
                'question': "5. 'Life is like a box of chocolates; you never know what you're gonna get' is a line from which movie?",
                'options': ["Forrest Gump", "The Shawshank Redemption", "Pulp Fiction", "Braveheart"],
                'correct_option': 0
            },
            {
                'question': "6. Which animated film features the quote, 'To infinity and beyond!'?",
                'options': ["Finding Nemo", "Toy Story", "The Incredibles", "Frozen"],
                'correct_option': 1
            },
            {
                'question': "7. 'There's no place like home' is a famous line from which classic movie?",
                'options': ["The Wizard of Oz", "Gone with the Wind", "It's a Wonderful Life", "The Sound of Music"],
                'correct_option': 0
            },
            {
                'question': "8. In 'The Godfather,' what famous line does Don Vito Corleone utter when making someone an offer they can't refuse?",
                'options': [
                    "I'll make you an offer you can't refuse.",
                    "I'm gonna make him an offer he can't refuse.",
                    "You won't be able to refuse my offer.",
                    "An offer you won't refuse, I will make."
                ],
                'correct_option': 1
            },
            {
                'question': "9. 'Why so serious?' is a line delivered by which character in 'The Dark Knight'?",
                'options': ["Batman", "The Joker", "Two-Face", "Alfred"],
                'correct_option': 1
            },
            {
                'question': "10. In the film 'A Few Good Men,' who yells, 'You can't handle the truth' during a courtroom scene?",
                'options': ["Colonel Jessep", "Lieutenant Kaffee", "Colonel Markinson", "Captain Ross"],
                'correct_option': 0
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
