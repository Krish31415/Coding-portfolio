from Game import Game
from Question import Question
import customtkinter as ctk  # Credit: https://customtkinter.tomschimansky.com/tutorial/grid-system

from MainMenu import MainMenu

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")
ctk.set_widget_scaling(1.8)

def main():
    # create CTk window like a normal tkinter window
    app = ctk.CTk()
    app.geometry("600x600")
    app.title("At A Glance")
    app.after(0, lambda: app.state("zoomed"))

    game = Game([], app)

    menu = MainMenu(app, game)
    menu.displayMenu()

    app.mainloop()


if __name__ == '__main__':
    main()
