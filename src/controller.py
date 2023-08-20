from pygame import mixer
import eyed3


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
        print("Added succesfuly")
