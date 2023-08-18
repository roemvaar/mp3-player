from tkinter import ttk

class View(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Create widgets for audio player
        # play button
        self.play_button = ttk.Button(self, text='Play', command=self.play_button_clicked)
        self.play_button.grid(row=1)

        # stop button
        self.stop_button = ttk.Button(self, text='Stop', command=self.stop_button_clicked)
        self.stop_button.grid(row=3, column=1)

        # pause button
        self.pause_button = ttk.Button(self, text='Pause', command=self.pause_button_clicked)
        self.pause_button.grid(row=3, column=2)

        # unpause button
        self.pause_button = ttk.Button(self, text='Unpause', command=self.unpause_button_clicked)
        self.pause_button.grid(row=3, column=3)

        # Controller
        self.controller = None

    def set_controller(self, controller):
        """
        Set the controller
        :param controller:
        :return:
        """
        self.controller = controller

    def play_button_clicked(self):
        """
        Handle play button event
        :return:
        """
        if self.controller:
            self.controller.play_music()
    
    def stop_button_clicked(self):
        """
        Handle stop button event
        :return:
        """
        if self.controller:
            self.controller.stop_music()

    def pause_button_clicked(self):
        """
        Handle pause button event
        :return:
        """
        if self.controller:
            self.controller.pause_music()

    def unpause_button_clicked(self):
        """
        Handle unpause button event
        :return:
        """
        if self.controller:
            self.controller.unpause_music()
