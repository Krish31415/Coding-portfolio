import customtkinter as ctk
import os
from Question import Question
from random import shuffle
import pandas as pd


class MainMenu:
    def __init__(self, app: ctk.CTk, game):
        self.app = app
        self.game = game

    def displayMenu(self):
        # Main frame
        self.frame = ctk.CTkFrame(master=self.app, corner_radius=20)
        self.frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.frame.place(relx=0.5, rely=0.5, anchor="center")  # Centers frame

        # Title
        title = ctk.CTkLabel(self.frame, text="At A Glance", font=("Arial", 50, "bold"), fg_color="transparent")
        title.grid(row=0, column=0, padx=20, pady=12, sticky="nsew")

        # AI Photos
        aiPhotos = ctk.CTkButton(self.frame, text="AI Photos", command=self.playAIPhotos)
        aiPhotos.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")

        # Stats Tricks
        statsTricks = ctk.CTkButton(self.frame, text="Misleading Statistics", command=self.playMisleadingStats, )
        statsTricks.grid(row=2, column=0, padx=20, pady=10, sticky="nsew")

        # Logical Fallacies
        logicalFallacies = ctk.CTkButton(self.frame, text="Logical Fallacies", command=self.playLogicalFallacies)
        logicalFallacies.grid(row=3, column=0, padx=20, pady=(10, 20), sticky="nsew")

    def playGame(self, questionList: list):
        self.frame.destroy()
        self.game.currentQuestion = 0
        shuffle(questionList)
        self.game.questions = questionList
        self.game.displayQuestion(self)

    def playAIPhotos(self):
        images = ["./images/AI/" + image for image in os.listdir("./images/AI")]
        images += ["./images/Real/" + image for image in os.listdir("./images/Real")]
        splitIndex = len(os.listdir("./images/AI"))

        # Generates question for each image in images
        questionList = [Question("Is the image AI generated or Real?",
                                 ["AI", "Real"],
                                 i // splitIndex,  # Correct answer
                                 images=[images[i]])
                        for i in range(len(images))]

        self.playGame(questionList)

    def playMisleadingStats(self):
        images = ["./images/MisleadingStats/" + image for image in os.listdir("./images/MisleadingStats")]
        questionList = []
        questionDF = pd.read_csv("MisleadingStats.csv")

        for i in range(len(questionDF)):
            elem = questionDF.iloc[i]
            answerChoices = [elem["Option 0"], elem["Option 1"]]
            question = Question(elem["Prompt"], answerChoices, elem["Correct Answer"], images=[images[i]])
            questionList.append(question)

        self.playGame(questionList)

    def playLogicalFallacies(self):
        questionList = []
        questionDF = pd.read_csv("LogicalFallacies.csv")

        for i in range(len(questionDF)):
            elem = questionDF.iloc[i]
            answerChoices = [elem["Option 0"], elem["Option 1"], elem["Option 2"], elem["Option 3"]]
            question = Question(elem["Prompt"], answerChoices, elem["Correct Answer"])
            questionList.append(question)

        self.playGame(questionList)


def main():
    pass


if __name__ == '__main__':
    main()
