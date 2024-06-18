from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.graphics import Color, Rectangle, Ellipse, Line
from kivy.core.window import Window
from kivy.config import Config
from kivy.uix.gridlayout import GridLayout
from random import randint
from screeninfo import get_monitors

Builder.load_file('nardy.kv')

Config.set('graphics', 'resizable', '0')

total_score_white = 0
total_score_black = 0


class MyApp(App):  # Клас, що реалізує головний лейаут за допомогую метода build
    def build(self):
        Window.fullscreen = 'auto'
        self.layout = MainLayout()

        return self.layout


class MainLayout(BoxLayout):  # Головний лейаут, до якого додається контрольний пункт та ігрове поле
    def giving_the_dices(self, obj, value):  # Для отримання випадкових чисел з кубиків
        if value != 'down':
            self.gm.message_label = self.pl.children[0].children[0].children[0].children[2]
            self.gm.first_label_dice = self.pl.children[0].children[0].children[0].children[3]
            self.gm.second_label_dice = self.pl.children[0].children[0].children[0].children[5]
            self.gm.turning_dices = True

    def turning_down_the_checker(self, obj, value):  # Метод щоб переобрати вже обрану фішку
        if value != 'down':
            self.gm.chosen = None

    def skip_the_turn(self, obj, value):  # Метод для пропуску ходу, коли немає можливості ходити
        if value != 'down':
            if self.gm.player_turn == (.89, .93, .96, 1):
                self.gm.player_turn = (.19, .16, .14, 1)
            else:
                self.gm.player_turn = (.89, .93, .96, 1)
            self.gm.table_new = []
            self.gm.turning_dices = False

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.line_widget = Widget()
        self.orientation = 'vertical'
        self.size_hint = (1, 1)
        self.pl = PlayerPlace()
        self.gm = GamePlace()
        # self.rolling_button = self.pl.children[0].children[0].children[3]
        self.rolling_button = self.pl.children[0].children[0].children[3]
        self.rolling_button.fbind('state', self.giving_the_dices)

        self.rolling_button.state = 'down'

        self.giving_up_the_checker_button = self.pl.children[0].children[0].children[0].children[0]
        self.giving_up_the_checker_button.fbind('state', self.turning_down_the_checker)

        self.giving_up_the_turn_button = self.pl.children[0].children[0].children[0].children[1]
        self.giving_up_the_turn_button.fbind('state', self.skip_the_turn)

        self.gm.white_player_final_label = self.pl.children[0].children[0].children[4].children[2]
        self.gm.black_player_final_label = self.pl.children[0].children[0].children[4].children[0]

        self.pl.children[0].children[0].children[1].children[2].text = str(total_score_white)
        self.pl.children[0].children[0].children[1].children[0].text = str(total_score_black)

        self.gm.white_player_final_record_label = self.pl.children[0].children[0].children[1].children[2]
        self.gm.black_player_final_record_label = self.pl.children[0].children[0].children[1].children[0]

        # self.gm.total_value_white = total_score_white
        # self.gm.total_value_black = total_score_black


        self.add_widget(self.pl)
        self.add_widget(self.gm)
        self.rolling_button.state = 'normal'

        self.monitor = []

        for m in get_monitors():
            self.monitor.append(m.width)
            self.monitor.append(m.height)

        with self.canvas:
            Color(.19, .16, .14, 1)  # Колір лінії (червоний)
            Line(points=[self.monitor[0] / 2 - 2, 0, self.monitor[0] / 2 - 2, self.monitor[1] * .71], width=3)


class PlayerPlace(BoxLayout):  # Верхня частина (контрольний пункт)
    def restart_the_game(self):  # метод для перезапуску гри
        Window.clear()
        App.get_running_app().stop()
        MyApp().run()

    def get_random_points(self):
        return str(randint(1, 6))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.total_score_white = str(total_score_white)
        self.total_score_black = str(total_score_black)


class Checker(Widget):  # Віджет фішки
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


class GamePart(AnchorLayout):  # Частини Gameplace, в яких буде розміщено Checkers, а також трикутники для візуалу
    def on_size(self, *args):  # метод, який не дає трикутник розпадатися
        self.canvas.clear()
        with self.canvas:
            Color(.99, .83, .66, 1)
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


class GamePlace(GridLayout):  # Ігрове поле, на якому будуть відбуватися переміщення фішок
    def on_touch_down(self, touch):  # Один великий метод для налаштування механіки гри та її правил,
        # який спрацьовує під час натискання
        global total_score_white, total_score_black
        if not self.blocked:
            if not sum([j.counter for j in self.place_on_game if j.color == (.89, .93, .96, 1)]):  # Перевірка чи вже не кінець
                self.message_label.text = "White won!"
                total_score_white += 1
                self.white_player_final_record_label.text = f"{total_score_white}"
                self.blocked = True

            if not sum([j.counter for j in self.place_on_game if j.color == (.19, .16, .14, 1)]):
                self.message_label.text = "Black won!"
                total_score_black += 1
                self.black_player_final_record_label.text = f"{total_score_black}"
                self.blocked = True

            if not self.chosen:  # Перевірка для визначення вибору фішки гравця
                for i in self.place_on_game:
                    if i.collide_point(*touch.pos) and i.counter and i.color == self.player_turn:
                        self.chosen = i
                        break

            else:
                for i in self.place_on_game:  # Перевірка на знаходження необхідного місця до переміщення фішки
                    if (i.collide_point(*touch.pos) and (i.color == self.chosen.color
                        or i.color == (.99, .83, .66, 1)) and i != self.chosen and self.turning_dices):
                        if not self.table_new:  # Перевірка наявності ходів
                            self.message_label.text = ""
                            self.table_new.extend([int(self.first_label_dice.text), int(self.second_label_dice.text)])
                            if self.table_new[0] == self.table_new[1]:
                                self.table_new.extend([self.table_new[0], self.table_new[1]])

                        if (i.position - self.chosen.position in self.table_new or  # Перевірка правильності ходу
                                (i.position + 24) - self.chosen.position in self.table_new):
                            # Перевірка на фінальний етап для данного гравця у грі
                            if ((self.chosen.color == (.89, .93, .96, 1) and self.chosen.position in range(6, 12) and
                                sum([j.counter for j in self.place_on_game[6:12]]) != self.counter_white) and
                                    i.position not in range(6, 12)):
                                self.chosen = None
                                break

                            # Те саме, але вже для гравця чорними
                            elif ((self.chosen.color == (.19, .16, .14, 1) and self.chosen.position in range(18, 24) and
                                    sum([j.counter for j in self.place_on_game[18:]]) != self.counter_black) and
                                    i.position not in range(18, 24)):
                                self.chosen = None
                                break

                            # Перевірка на фінальний етап з підтвердженням для чорних
                            elif ((self.chosen.color == (.19, .16, .14, 1) and self.chosen.position in range(18, 24) and
                                    sum([j.counter for j in self.place_on_game[18:]]) == self.counter_black) and
                                    i.position not in range(18, 24)):

                                self.black_player_final_label.text = f"{int(self.black_player_final_label.text) + 1}"
                                self.counter_black -= 1

                            # Перевірка на фінальний етап з підтвердженням для білих
                            elif ((self.chosen.color == (.89, .93, .96, 1) and self.chosen.position in range(6, 12) and
                                    sum([j.counter for j in self.place_on_game[6:12]]) == self.counter_white) and
                                    i.position not in range(6, 12)):

                                self.white_player_final_label.text = f"{int(self.white_player_final_label.text) + 1}"
                                self.counter_white -= 1

                            # Зміни при звичайному ході
                            else:
                                i.counter = i.counter + 1
                                i.ch.counter = i.counter
                                i.ch.label.text = f'{i.counter}'

                                if i.color == (.99, .83, .66, 1) and i.counter > 0:
                                    i.color = self.chosen.color
                                    i.on_size()

                            # Загальна процедура для проходження фішки та зміни всіх необхідних елементів
                            self.chosen.counter = self.chosen.counter - 1
                            self.chosen.ch.counter = self.chosen.counter
                            self.chosen.ch.label.text = f'{self.chosen.counter}'

                            if self.chosen.counter == 0:
                                self.chosen.color = (.99, .83, .66, 1)
                                self.chosen.on_size()
                            if (i.position - self.chosen.position) in self.table_new:
                                self.table_new.remove(i.position - self.chosen.position)
                            else:
                                self.table_new.remove(24 + i.position - self.chosen.position)
                            if not self.table_new:
                                self.message_label.text = "Next player's turn"
                                if self.player_turn == (.89, .93, .96, 1):
                                    self.player_turn = (.19, .16, .14, 1)
                                else:
                                    self.player_turn = (.89, .93, .96, 1)
                                self.turning_dices = False

                            self.chosen = None
                            break
                    if not self.turning_dices:
                        self.message_label.text = "Next player should\n turn the dices!"

    def __init__(self, **kwargs):  # Налаштування цілої купи параметрів, велика частина з яких будуть задаватися ззовні
        super().__init__(**kwargs)
        self.turning_dices = False
        self.player_turn = (.89, .93, .96, 1)
        self.table_new = []
        self.counter_white = 1
        self.counter_black = 1

        self.first_label_dice = None
        self.second_label_dice = None
        self.message_label = None

        self.white_player_final_label = None
        self.black_player_final_label = None

        self.white_player_final_record_label = None
        self.black_player_final_record_label = None

        self.blocked = False

        self.rows = 2
        self.cols = 12

        self.place_on_game = []
        self.chosen = None

        # Встановлення базових фішок фонового кольору та 0 тексту Label для подальших маніпуляцій з ними
        for i in range(12):
            self.place_on_game.append(GamePart(1, 11 - i, (.99, .83, .66, 1), 0))
            self.add_widget(self.place_on_game[i])

        self.place_on_game.reverse()

        for i in range(12, 24):
            self.place_on_game.append(GamePart(0, i, (.99, .83, .66, 1), 0))
            self.add_widget(self.place_on_game[i])

        self.place_on_game[0].counter = 1
        self.place_on_game[0].color = (.19, .16, .14, 1)
        self.place_on_game[12].counter = 1
        self.place_on_game[12].color = (.89, .93, .96, 1)



if __name__ == '__main__':
    MyApp().run()
