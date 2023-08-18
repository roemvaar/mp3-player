import tkinter as tk
from model import Model
from view import View
from controller import Controller
from pygame import mixer


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('MP3 Player App')
        self.geometry("920x600+290+85")
        self.configure(background='#212121')
        self.resizable(False, False)

        # Create a model
        model = Model()

        # Create a view and place it on the root window
        view = View(self)
        view.grid(row=0, column=0, padx=10, pady=10)

        # Create a controller
        controller = Controller(model, view)

        mixer.init()

        # Set the controller to view
        view.set_controller(controller)


if __name__ == '__main__':
    app = App()
    app.mainloop()
