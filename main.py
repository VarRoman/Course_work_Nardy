from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.graphics import Color, Rectangle, Ellipse, Line
from kivy.core.window import Window
from kivy.config import Config
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.properties import NumericProperty

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


class GamePart(BoxLayout):
    def on_size(self, *args):
        self.canvas.clear()
        with self.canvas:
            Color(.99, .83, .67, 1)
            Rectangle(size=self.size, pos=self.pos)
            Color(49 / 255, 41 / 255, 36 / 255, 1)
            if self.place:
                Line(points=(self.pos[0] + 5, self.height + self.pos[1] - 5, self.width + self.pos[0] - 10,
                             self.height + self.pos[1] - 5, self.pos[0] + (self.width / 2), self.pos[1] + 50),
                            close=True, size=self.size)
            else:
                Line(points=(
                    self.pos[0] + 5, self.pos[1] + 5, self.width + self.pos[0] - 10, self.pos[1] + 5, self.pos[0] +
                    (self.width / 2), self.height - 50), close=True, size=self.size)

    def __init__(self, place, **kwargs):
        super().__init__(**kwargs)
        self.place = place

        self.add_widget(Button())


class GamePlace(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 12
        self.rows = 2

        upper_line = []
        lower_line = []

        for i in range(12):
            upper_line.append(GamePart(1))
            self.add_widget(upper_line[i])

        for i in range(12):
            lower_line.append(GamePart(0))
            self.add_widget(lower_line[i])

        # for child in self.children:
        #     print(f"Розмір дочірнього віджета: {child.size}")
        #     print(f"Позиція дочірнього віджета: {child.pos}")


if __name__ == '__main__':
    MyApp().run()
