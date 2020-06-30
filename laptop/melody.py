from kivy.core.audio.audio_pygame import mixer


class melody():
    def __init__(self):
        super().__init__()
        self.player = []


    def store(self, id):
        # self.player = self.player + id
        mixer.init()
        mixer.music.load("sounds/1.mp3")
        mixer.music.play()


