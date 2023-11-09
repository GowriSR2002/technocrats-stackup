import tkinter as tk
import subprocess
from tkinter import messagebox

class TopicSelectionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Choose a Topic")
        self.root.geometry("800x600")
        
        self.heading_label = tk.Label(root, text="Choose a Topic", font=("Arial", 20), justify="center")
        self.heading_label.grid(row=0, column=0, columnspan=5, pady=20)

        self.topic_buttons = []

        self.topics = [
            {
                'name': "World Capitals",
                'questions': [
                    {
                        'question': "1. What is the capital of France?",
                        'options': ["Paris", "Berlin", "Madrid", "Rome"],
                        'correct_option': 0
                    },
                    {
                        'question': "2.	The capital of Japan is:",
                        'options': ["Tokyo", "Beijing", "Seoul", "Bangkok"],
                        'correct_option': 0
                    },
                    {
                        'question': "3.	What is the capital of Australia?",
                        'options': ["Sydney", "Melbourne", "Canberra", "Brisbane"],
                        'correct_option': 2
                    },
                    {
                        'question': "4.	Which city serves as the capital of Brazil?",
                        'options': ["Rio de Janeiro", "Sao Paulo", "Brasilia", "Salvador"],
                        'correct_option': 2
                    },
                    {
                        'question': "5.	The capital of South Africa is:",
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
                ],  # Add your list of questions here
            },
            {
                'name': "Science and Nature",
                'questions': [
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
        
                ],  # Add questions for this topic
            },
            # Add more topics with their questions
        ]

        for i, topic in enumerate(self.topics):
            row = 1 + i // 3
            col = i % 3

            button = tk.Button(root, text=topic['name'], width=15, height=2, font=("Arial", 12),
                               command=lambda t=topic: self.select_topic(t))
            button.grid(row=row, column=col, pady=10, padx=10, sticky="nsew")
            self.topic_buttons.append(button)

        for i in range(4):
            root.grid_rowconfigure(i, weight=1)
        for i in range(3):
            root.grid_columnconfigure(i, weight=1)


    def select_topic(self, topic):
        print(f"Selected topic: {topic['name']}")  # Add this line
        root.withdraw()
        quiz_app = QuizApp(root, topic)
        root.protocol("WM_DELETE_WINDOW", quiz_app.quit)
        quiz_app.show_question()

class QuizApp:
    def __init__(self, root, topic):
        self.root = root
        self.topic = topic
        self.root.title("Quiz Application")
        self.root.geometry("800x600")
        self.current_question = 0
        self.score = 0

        self.questions = self.topic['questions']

        self.question_label = tk.Label(root, text="")
        self.question_label.grid(row=1, column=0, columnspan=4, pady=20)

        self.var = tk.IntVar()
        self.var.set(-1)

        self.radio_buttons = []

        for i in range(4):
            option_frame = tk.Frame(root)
            option_frame.grid(row=2 + i, column=0, columnspan=4, pady=10, padx=10)

            radio = tk.Radiobutton(option_frame, variable=self.var, value=i)
            radio.pack(side="left")

            text = tk.Label(option_frame, text="", anchor="w")
            text.pack(side="left")

            self.radio_buttons.append((radio, text))

        self.next_button = tk.Button(root, text="Next", command=self.next_question)
        self.next_button.grid(row=6, column=0, columnspan=4, pady=10)

    def show_question(self):
        print("Showing question")  # Add this line
        question = self.questions[self.current_question]
        self.question_label.config(text=question['question'], justify="center")
        
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
        else:
            messagebox.showinfo("Quiz Over", f"Your score is {self.score}/{len(self.questions)}")
            self.quit()

    def show_question(self):
        question = self.questions[self.current_question]
        self.question_label.config(text=question['question'], justify="center")
        
        for i, (radio, text) in enumerate(self.radio_buttons):
            radio.config(variable=self.var, value=i)
            text.config(text=question['options'][i])

    def quit(self):
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = TopicSelectionApp(root)
    root.mainloop()
