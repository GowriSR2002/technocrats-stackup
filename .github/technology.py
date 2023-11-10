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
                'question': "1. Who co-founded Microsoft and is one of the wealthiest people in the world?",
                'options': ["Steve Jobs", "Bill Gates", "Mark Zuckerberg", "Jeff Bezos"],
                'correct_option': 1,
            },
            {
                'question': "2. Which company developed the iPhone, iPad, and Macintosh computer?",
                'options': ["Microsoft", "Apple", "Google", "Amazon"],
                'correct_option': 1,
            },
            {
                'question': "3. What does the acronym 'WWW' stand for in the context of the internet?",
                'options': ["World Wide Web", "World Wrestling World", "Wireless Web Work", "World Widget Web"],
                'correct_option': 0,
            },
            {
                'question': "4. Which social media platform is known for its character limit in posts and tweets?",
                'options': ["Facebook", "Instagram", "Twitter", "LinkedIn"],
                'correct_option': 2,
            },
            {
                'question': "5. What does the abbreviation 'PDF' stand for in the context of document formats?",
                'options': ["Portable Document Format", "Pretty Digital File", "Print Document File", "Personal Data File"],
                'correct_option': 0,
            },
            {
                'question': "6. Who is the co-founder of SpaceX and Tesla, Inc.?",
                'options': ["Jeff Bezos", "Richard Branson", "Elon Musk", "Mark Zuckerberg"],
                'correct_option': 2,
            },
            {
                'question': "7. Which programming language is often used for web development and is known for its versatility?",
                'options': ["Java", "C++", "Python", "JavaScript"],
                'correct_option': 3,
            },
            {
                'question': "8. The first commercial email system was developed by which company in the early 1970s?",
                'options': ["Microsoft", "Google", "Apple", "Ray Tomlinson"],
                'correct_option': 3,
            },
            {
                'question': "9. What does the abbreviation 'AI' stand for in the context of technology?",
                'options': ["Authentic Intelligence", "Advanced Interface", "Artificial Intelligence", "Automated Internet"],
                'correct_option': 2,
            },
            {
                'question': "10. Who is often called the 'father of the computer' and developed the first mechanical computer, known as the Analytical Engine?",
                'options': ["Steve Jobs", "Charles Babbage", "Alan Turing", "Tim Berners-Lee"],
                'correct_option': 1,
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
