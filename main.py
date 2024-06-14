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
from random import randint

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
    def get_random_points(self):
        return str(randint(1, 6))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Checker(Widget):
    def update_checker_canvas(self, new_color):
        if new_color != self.color:
            self.color = new_color
            self.canvas.clear()
            with self.canvas:
                Color(*self.color)
                Ellipse(size=[100, 100], pos=(self.x - (self.height / 2), self.y))

    def __init__(self, color, position, counter, x, y, **kwargs):
        super().__init__(**kwargs)
        self.x = x
        self.y = y
        self.counter = counter
        self.color = color
        self.position = position
        self.label = Label(text=f'{self.counter}', font_size='32')

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
        if self.place and self.place != -1:
            self.ch = Checker(self.color, self.position, self.counter,
                         self.x + self.width / 2, self.height * 1.5 + 55)
            self.add_widget(self.ch.label)
            self.add_widget(self.ch)
        else:
            self.ch = Checker(self.color, self.position, self.counter,
                                    self.x + self.width / 2, 14)

            self.add_widget(self.ch.label)
            self.add_widget(self.ch)

    def __init__(self, place, position, color, counter, **kwargs):
        super().__init__(**kwargs)
        self.place = place  # змінна для визначення місця canvas

        self.position = position  # який номер цієї позиції відносно дошки
        self.color = color  # який колір фішок, що знаходяться на цьому полі
        self.counter = counter  # кількість фішок на цьому полі
        # self.bind(on_touch_down=self.on_touch_down)

class GamePlace(GridLayout):
    def on_touch_down(self, touch):
        print(self.choosen)
        if not self.choosen:
            for i in self.place_on_game:
                if i.collide_point(*touch.pos) and i.counter != 0:
                    print(i.position)
                    self.choosen = i
                    print(self.choosen)
                    break

        else:
            for i in self.place_on_game:
                if i.collide_point(*touch.pos) and (i.color == self.choosen.color or
                                                    i.color == (.99, .83, .67, 1)) and i != self.choosen:
                    i.counter = i.counter + 1
                    i.ch.counter = i.counter
                    i.ch.label.text = f'{i.counter}'

                    self.choosen.counter = self.choosen.counter - 1
                    self.choosen.ch.counter = self.choosen.counter
                    self.choosen.ch.label.text = f'{self.choosen.counter}'

                    if self.choosen.color == (.99, .83, .67, 1) and self.choosen.counter > 0:
                        self.choosen.remove_widget(self.choosen.ch)
                        self.choosen.color = i.color
                        self.choosen.ch.update_checker_canvas(i.color)
                        self.choosen.add_widget(self.choosen.ch)


                    if i.counter == "0":
                        i.color = (.99, .83, .67, 1)
                        i.ch.update_checker_canvas(i.color)

                    self.choosen.on_size()
                    i.on_size()
                    self.choosen = None
                    print(self.choosen)
                    break

    def move_checker(self, first_position, second_position, sample_object):
        pass

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.rows = 2
        self.cols = 12

        self.place_on_game = []
        self.choosen = None

        for i in range(12):
            self.place_on_game.append(GamePart(1, 11 - i, (.99, .83, .67, 1), 0))
            self.add_widget(self.place_on_game[i])

        self.place_on_game.reverse()

        for i in range(12, 24):
            self.place_on_game.append(GamePart(0, i, (.99, .83, .67, 1), 0))
            self.add_widget(self.place_on_game[i])

        self.place_on_game[0].counter = 15
        self.place_on_game[0].color = (.19, .16, .14, 1)
        self.place_on_game[12].counter = 15
        self.place_on_game[12].color = (.89, .93, .97, 1)



if __name__ == '__main__':
    MyApp().run()
