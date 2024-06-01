from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.graphics import (Color, Ellipse, Rectangle, Line)
from kivy.core.window import Window
from kivy.config import Config
from kivy.uix.button import Button

Builder.load_file('main.kv')


class MyApp(App):
    def build(self):
        Window.clearcolor = (.99, .83, .67, 1)
        Window.size = (1000, 600)
        Window.left = 250

        self.layout = BoxLayout(orientation='vertical')
        self.layout.size_hint = (1, 1)
        self.layout.add_widget(PlayerPlace())
        self.layout.add_widget(GamePlace())
        # self.layout.add_widget(PlayerPlace())

        return self.layout


class PlayerPlace(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.add_widget(Label(text='sfjsjfl'))
        # self.size_hint = [.3, 1]

class PainterWidget(Widget):
    def __init__(self, **kwargs):
        super(PainterWidget, self).__init__(**kwargs)


class GamePlace(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Label(text='sfjsjfl'))
        self.size_hint = [.7, 1]

        with self.canvas:
            x = 135
            y = 0
            for i in range(12):
                Color(0, 123, 441, 1)
                Ellipse(pos=(x, y), size=(80, 80), )
                x += 80

            y = 285
            x = 135
            for i in range(12):
                Color(0, 1, 0, 1)
                Ellipse(pos=(x, y), size=(80, 80), )
                x += 80
            Color(1, 1, 1, 1)








if __name__ == '__main__':
    MyApp().run()
