import tkinter as tk
import customtkinter as ctk
from MainMenu import MainMenu
from PIL import Image


class Game:
    def __init__(self, questionList: list, app: ctk.CTk):
        self.questions = questionList
        self.app = app
        self.selection = tk.IntVar(value=-1)
        self.currentQuestion = 0

    def displayQuestion(self, menu: MainMenu):
        self.menu = menu

        # Main frame
        self.frame = ctk.CTkFrame(master=self.app, corner_radius=20)
        self.frame.grid(row=0, column=0, padx=20, pady=20)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")  # Centers frame

        # Display the image
        if len(self.questions[self.currentQuestion].images) > 0:
            # Construct filepath based on whether image is AI or Real
            image = ctk.CTkImage(Image.open(self.questions[self.currentQuestion].images[0]),
                                 Image.open(self.questions[self.currentQuestion].images[0]),
                                 size=(225, 225))
            imageLabel = ctk.CTkLabel(self.frame, image=image, text="", fg_color="transparent")
            imageLabel.grid(row=2, column=0, padx=20, pady=(20, 0), sticky="nsew")

        # Prompt widget
        prompt = ctk.CTkLabel(self.frame, text=self.questions[self.currentQuestion].prompt, wraplength=400)
        prompt.grid(row=3, column=0, padx=20, pady=(15, 5), sticky="ns")

        # Options widgets
        options = [ctk.CTkRadioButton(self.frame, text=choice, value=i, variable=self.selection)
                   for i, choice in enumerate(self.questions[self.currentQuestion].answerChoices)]

        # Position the options
        for i, option in enumerate(options):
            option.grid(row=i + 4, column=0, padx=20, pady=10, sticky="nsew")

        submitButton = ctk.CTkButton(self.frame, text="Submit", command=self.submitAnswer)
        submitButton.grid(row=len(options) + 4, column=0, padx=20, pady=(10, 20), sticky="nsew")

        # Quit to menu
        quitButton = ctk.CTkButton(self.app, text="Quit", command=self.quitToMenu, fg_color="darkred",
                                   font=("Arial", 10, "bold"), width=40)
        quitButton.place(relx=0.01, rely=0.02, anchor="nw")

    def submitAnswer(self):
        result = ("Correct!" if self.selection.get() == self.questions[self.currentQuestion].correctAnswer
                  else "Incorrect!")

        dialog = ctk.CTkInputDialog(title="Results",
                                    text=result+"\n\nClick Ok to continue to the next question!\nClick Cancel to return to the question.",
                                    entry_fg_color="green" if result == "Correct!" else "red",
                                    entry_border_color="green" if result == "Correct!" else "red", )

        # Check if user has selected an answer
        if dialog.get_input() is None or self.selection.get() == -1:
            return

        # Reset everything for next question
        self.currentQuestion += 1
        self.frame.destroy()
        self.selection.set(-1)

        # Return to menu at end of questions
        if self.currentQuestion < len(self.questions):
            self.displayQuestion(self.menu)
        else:
            self.menu.displayMenu()

    def quitToMenu(self):
        self.frame.destroy()
        self.menu.displayMenu()


def main():
    pass


if __name__ == '__main__':
    main()
