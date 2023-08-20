class Model:
    def __init__(self):
        self.songs = []
        self.currently_playing = "music/Bad_Bunny_WHERE_SHE_GOES.mp3"

    def add_song(self, song):
        self.songs.append(song)

    def set_currently_playing_song(self, song):
        self.currently_playing = song
    
    def currently_playing_song(self):
        return self.currently_playing
