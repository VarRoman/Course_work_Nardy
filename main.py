from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.graphics import Color, Rectangle, Ellipse
from kivy.core.window import Window
from kivy.config import Config
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

Builder.load_file('main.kv')

Config.set('graphics', 'resizable', '0')

class MyApp(App):
    def build(self):
        Window.size = (1000, 700)
        Window.left = 250
        Window.resizable = False


        self.layout = BoxLayout(orientation='vertical')
        self.layout.size_hint = (1, 1)
        self.layout.add_widget(PlayerPlace())
        self.layout.add_widget(GamePlace())
        # self.layout.resizable = False

        return self.layout


class PlayerPlace(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class GamePlace(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

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



if __name__ == '__main__':
    MyApp().run()