from pygame import mixer
import eyed3
from tkinter.filedialog import askopenfile
import shutil


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def play_music(self):
        """
        Play music
        :return:
        """
        if self.model:
            audiofile = eyed3.load(self.model.currently_playing)
            self.view.show_current_playing_song(audiofile)
            mixer.music.load(self.model.currently_playing)
            mixer.music.play()

    def stop_music(self):
        """
        Stop music
        :return:
        """
        if self.model:
            mixer.music.pause()

    def pause_music(self):
        """
        Temporarily stop playback of all sound channels
        """
        mixer.music.pause()

    def unpause_music(self):
        """
        Temporarily stop playback of all sound channels
        """
        mixer.music.unpause()
    
    def add_song(self):
        """
        Add song from user library
        """
        filename = askopenfile()
        shutil.copy(filename.name, "/home/roemvaar/repos/mp3-player/music/")

    def display_available_songs(self):
        """
        Display available songs from user library
        """
        if self.model:
            print("Show available songs")
            filename = askopenfile()
            self.model.set_currently_playing_song(filename.name)
            print(self.model.currently_playing)
