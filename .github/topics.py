from tkinter import *
from PIL import ImageTk
import subprocess

def worldcapitals_page():
    root.destroy()
    import worldcapitals

def scienceandnature_page():
    root.destroy()
    import scienceandnature

def famousliterature_page():
    root.destroy()
    import famousliterature

class TopicSelectionApp:
    
    def __init__(self, root):
        self.root = root
        self.root.title("Choose a Topic")
        self.root.geometry('990x600+50+50')
        background=ImageTk.PhotoImage(file='.github/bgg1.png')
        self.root.bgLabel=Label(root,image=background)        
        self.heading_label = Label(root, text="Choose a Topic !", font=("Arial", 24),justify="center")
        self.heading_label.grid(row=0, column=0, columnspan=5, pady=20)

        self.topic_buttons = []

        topics = [
            "World Capitals",
            "Science and Nature",
            "Famous Literature",
            "Movie Quotes",
            "History",
            "Geography",
            "Music",
            "Technology",
            "Random Quiz"
        ]

        for i, topic in enumerate(topics):
            if i < 9:
                row = 1 + i // 3
                col = i % 3
            
            button = Button(root, text=topic, width=15, height=2, font=("Arial", 16) ,bg='white',fg='darkblue',activebackground='lightblue',activeforeground='darkblue',cursor='hand2')
            button.grid(row=row, column=col, pady=10, padx=10, sticky="nsew")
            self.topic_buttons.append(button)
        
        # Create a command to open a script when the button is clicked
            if i == 0:
                command = worldcapitals_page
                #command = lambda script_name="full/path/to/worldcapitals.py": self.run_script(script_name)
            elif i == 1:
                command = scienceandnature_page
            elif i == 2:
                command = famousliterature_page
         # Configure rows and columns to expand
        for i in range(4):  
            root.grid_rowconfigure(i, weight=1)
        for i in range(3):
            root.grid_columnconfigure(i, weight=1)

if __name__ == "__main__":
    root = Tk()
    app = TopicSelectionApp(root)
    root.mainloop()
