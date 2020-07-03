from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from melody import melody
from kivy.core.window import Window
from word_game import word_game
from kivy.properties import StringProperty


obj1 = melody()
word = word_game()


Window.fullscreen = 'auto'

Builder.load_file("main.kv")
Builder.load_file("missing_letters.kv")


class MenuScreen(Screen):
    pass


class MelodyMaker(Screen):
    def store(self, id):
        obj1.store(id)

    def play(self):
        obj1.play()


class Missing_letter(Screen):

    word = StringProperty()
    hint = StringProperty()
    flag = StringProperty(defaultvalue='start')
    status = StringProperty()
    question = StringProperty('Click Start To Proceed')
    answer = ''
    def get(self):
        self.word, self.hint = word.question()
        self.flag = 'Reset'
        self.question = self.word + ' Hint: ' + self.hint
    def submit(self, ans):
        app = main()
        if word.answer(ans):
            self.status = 'Correct!!'
            self.flag = 'Proceed'
        else:
            self.status = 'Sorry, try again'


sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(MelodyMaker(name='Melody Maker'))
sm.add_widget(Missing_letter(name='Missing'))


class main(App):

    def build(self):
        return sm


if __name__ == '__main__':
    main().run()
