from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from melody import melody
from kivy.core.window import Window


obj = melody()


Window.fullscreen = 'auto'


Builder.load_file("main.kv")


class MenuScreen(Screen):
    pass


class MelodyMaker(Screen):
    def store(self, id):
        obj.store(id)

    def play(self):
        obj.play()


class Missing_letter(Screen):
    pass


sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(MelodyMaker(name='Melody Maker'))
sm.add_widget(Missing_letter(name='Missing'))


class main(App):

    def build(self):
        return sm


if __name__ == '__main__':
    main().run()
