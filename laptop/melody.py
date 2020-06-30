from kivy.core.audio.audio_pygame import mixer
import time


class melody():
    def __init__(self):
        super().__init__()
        self.player = []

    def store(self, id):
        self.player.append(id)
        mixer.init()
        mixer.music.load("D:/Github/Model-laptop/laptop/sounds/%d.mp3" % id)
        mixer.music.play()

    def play(self):
        for i in range(len(self.player)):
            mixer.init()
            mixer.music.load("D:/Github/Model-laptop/laptop/sounds/%d.mp3" % self.player[i])
            mixer.music.play()
            time.sleep(0.5)
