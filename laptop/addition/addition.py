import random
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Line
from kivy.uix.button import Button


class add(Screen):
    question1 = 0
    question2 = 0
    question = StringProperty('hello')
    result = StringProperty('')
    status = True

    def get(self):
        self.question1 = random.randint(0, 100)
        self.question2 = random.randint(0, 100)
        self.question = str(self.question1) + ' + ' + str(self.question2)

    def submit(self):
        if self.question1 + self.question2 == int(self.ids.answer.text):
            self.result = 'Correct !!!'
            self.get()
            self.ids.answer.text = ''
        else:
            self.result = 'Please Try Again'

    def openDraw(self):

        parent = Widget()
        if self.status is False:
            self.clear_widgets(parent)
        self.painter = MyPaintWidget()
        clearbtn = Button(text='Clear')
        clearbtn.bind(on_release=self.clear_canvas)
        parent.add_widget(self.painter)
        parent.add_widget(clearbtn)
        self.add_widget(parent)
        self.status = False

    def clear_canvas(self, obj):
        self.painter.canvas.clear()


class MyPaintWidget(Widget):

    def on_touch_down(self, touch):
        with self.canvas:
            Color(1, 1, 0)
            d = 30.
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
            touch.ud['line'] = Line(points=(touch.x, touch.y))

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]
