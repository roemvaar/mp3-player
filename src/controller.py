from pygame import mixer


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
            mixer.music.load("music/Bad_Bunny_WHERE_SHE_GOES.mp3")
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
