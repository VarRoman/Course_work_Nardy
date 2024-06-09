from kivy.app import App
from kivy.uix.scatterlayout import ScatterLayout
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

        gm = GamePlace()

        self.layout.add_widget(gm)


        # self.layout.resizable = False

        return self.layout


class PlayerPlace(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Checker(Widget):
    def __init__(self, color, position, counter, x, y, **kwargs):
        super().__init__(**kwargs)
        self.x = x
        self.y = y
        self.counter = counter
        self.color = color
        self.position = position
        self.number = 0
        self.label = Label(text=f'{self.number}', font_size='32')
        # self.label.pos = (self.width / 2 - 200, self.y - 20)  # Set position here
        # self.add_widget(self.label)

        with self.canvas:
            Color(*self.color)
            Ellipse(size=[100, 100], pos=(self.x - (self.height / 2), self.y))




class GamePart(AnchorLayout):
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
                # self.add_widget(Checker('black', None, self.x + self.width / 2, 14))
            else:
                Line(points=(
                    self.pos[0] + 5, self.pos[1] + 5, self.width + self.pos[0] - 10, self.pos[1] + 5, self.pos[0] +
                    (self.width / 2), self.height - 50), close=True, size=self.size)
        if self.place:
            ch = Checker('black', self.position, self.counter,
                         self.x + self.width / 2, self.height * 1.5 + 55)

            self.add_widget(ch.label)
            self.add_widget(ch)
        else:
            ch = Checker('black', self.position, self.counter,
                                    self.x + self.width / 2, 14)

            self.add_widget(ch.label)
            self.add_widget(ch)




    def __init__(self, place, position, color, counter, **kwargs):
        super().__init__(**kwargs)
        self.place = place  # змінна для визначення місця canvas

        self.position = position  # який номер цієї позиції відносно дошки
        self.color = color  # який колір фішок, що знаходяться на цьому полі
        self.counter = counter  # кількість фішок на цьому полі

class GamePlace(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.rows = 2
        self.cols = 12

        self.place_on_game = []

        for i in range(12):
            self.place_on_game.append(GamePart(1, i, None, 0))
            self.add_widget(self.place_on_game[i])

        for i in range(12, 24):
            self.place_on_game.append(GamePart(0, i, None, 0))
            self.add_widget(self.place_on_game[i])


if __name__ == '__main__':
    MyApp().run()
