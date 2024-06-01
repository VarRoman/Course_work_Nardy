from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.graphics import Color
from kivy.core.window import Window
from kivy.config import Config
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

Builder.load_file('main.kv')

class MyApp(App):
    def build(self):
        Window.size = (1000, 700)
        Window.left = 250

        self.layout = BoxLayout(orientation='vertical')
        self.layout.size_hint = (1, 1)
        self.layout.add_widget(PlayerPlace())
        self.layout.add_widget(GamePlace())

        return self.layout


class PlayerPlace(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class GamePlace(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)



if __name__ == '__main__':
    MyApp().run()