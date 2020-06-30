from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from melody import melody

# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.

Builder.load_file("main.kv")


# Declare both screens
class MenuScreen(Screen):
    pass


class MelodyMaker(Screen):
    def store(self, id):
        obj = melody()
        obj.store(id)


# Create the screen manager
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(MelodyMaker(name='Melody Maker'))


class main(App):

    def build(self):
        return sm


if __name__ == '__main__':
    main().run()
