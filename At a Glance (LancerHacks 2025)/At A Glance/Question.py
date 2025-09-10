class Question():
    def __init__(self, prompt: str, answerChoices: list, correctAnswer: int, images=[]):
        """
        str prompt: The question/ text prompt
        list answerChoices: list of strings representing answer choices.
        correctAnswer: int representing index of correct answer in answerChoices
        images: list representing images to be compared or printed
        """

        self.prompt = prompt
        self.answerChoices = answerChoices
        self.correctAnswer = correctAnswer
        self.images = images

    def __str__(self):
        retString = ""
        retString += self.prompt + "\n"

        letter = "A"
        for i in range(len(self.answerChoices)):
            retString += letter + ": " + str(self.answerChoices[i]) + "\n"
            letter = chr(ord(letter) + 1)
        return retString


def main():
    q = Question("What is 2+2?", [3, 4, 5, 6], 1)
    print(q)


if __name__ == '__main__':
    main()
