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

        self.layout = MainLayout()
        # self.layout.do_layout()

        return self.layout

class MainLayout(BoxLayout):
    def giving_the_dices(self, obj, value):
        if value != 'down':
            self.gm.message_label = self.pl.children[0].children[0].children[0].children[2]
            self.gm.first_label_dice = self.pl.children[0].children[0].children[0].children[3]
            self.gm.second_label_dice = self.pl.children[0].children[0].children[0].children[5]
            self.gm.turning_dices = True

    def turning_down_the_checker(self, obj, value):
        if value != 'down':
            self.gm.chosen = None

    def skip_the_turn(self, obj, value):
        if value != 'down':
            if self.gm.player_turn == (.89, .93, .97, 1):
                self.gm.player_turn = (.19, .16, .14, 1)
            else:
                self.gm.player_turn = (.89, .93, .97, 1)
            self.gm.table_new = []
            self.gm.turning_dices = False

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.size_hint = (1, 1)
        self.pl = PlayerPlace()
        self.gm = GamePlace()
        # self.rolling_button = self.pl.children[0].children[0].children[3]
        self.rolling_button = self.pl.children[0].children[0].children[3]
        self.rolling_button.fbind('state', self.giving_the_dices)

        self.giving_up_the_checker_button = self.pl.children[0].children[0].children[0].children[0]
        self.giving_up_the_checker_button.fbind('state', self.turning_down_the_checker)

        self.giving_up_the_turn_button = self.pl.children[0].children[0].children[0].children[1]
        self.giving_up_the_turn_button.fbind('state', self.skip_the_turn)

        self.add_widget(self.pl)
        self.add_widget(self.gm)




class PlayerPlace(BoxLayout):
    def get_random_points(self):
        return str(randint(1, 6))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Checker(Widget):
    def update_checker_canvas(self, new_color):
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
        if not self.chosen:
            for i in self.place_on_game:
                if i.collide_point(*touch.pos) and i.counter != 0 and i.color == self.player_turn:
                    self.chosen = i
                    break

        else:
            for i in self.place_on_game:
                if i.collide_point(*touch.pos) and (i.color == self.chosen.color or
                                        i.color == (.99, .83, .67, 1)) and i != self.chosen and self.turning_dices:
                    if not self.table_new:
                        self.message_label.text = ""
                        self.table_new.extend([int(self.first_label_dice.text), int(self.second_label_dice.text)])
                        if self.table_new[0] == self.table_new[1]:
                            self.table_new.extend([self.table_new[0], self.table_new[1]])
                        self.counter = len(self.table_new)
                    if (i.position - self.chosen.position in self.table_new or
                            (i.position + 24) - self.chosen.position in self.table_new):
                        i.counter = i.counter + 1
                        i.ch.counter = i.counter
                        i.ch.label.text = f'{i.counter}'

                        self.chosen.counter = self.chosen.counter - 1
                        self.chosen.ch.counter = self.chosen.counter
                        self.chosen.ch.label.text = f'{self.chosen.counter}'

                        if i.color == (.99, .83, .67, 1) and i.counter > 0:
                            i.color = self.chosen.color
                            i.on_size()

                        if self.chosen.color != (.99, .83, .67, 1) and self.chosen.counter == 0:
                            self.chosen.color = (.99, .83, .67, 1)
                            self.chosen.on_size()
                        if (i.position - self.chosen.position) in self.table_new:
                            self.table_new.remove(i.position - self.chosen.position)
                        else:
                            self.table_new.remove(24 + i.position - self.chosen.position)
                        self.counter -= 1
                        if not self.counter:
                            self.message_label.text = "Next player's turn"
                            if self.player_turn == (.89, .93, .97, 1):
                                self.player_turn = (.19, .16, .14, 1)
                            else:
                                self.player_turn = (.89, .93, .97, 1)
                            self.turning_dices = False

                        self.chosen = None
                        break
                if not self.turning_dices:
                    self.message_label.text = "Next player should\n turn the dices!"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.turning_dices = False
        self.player_turn = (.89, .93, .97, 1)
        self.counter = 0
        self.table_new = []
        self.first_label_dice = None
        self.second_label_dice = None
        self.message_label = None
        self.rows = 2
        self.cols = 12

        self.place_on_game = []
        self.chosen = None

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
