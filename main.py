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


class EllipseWidget(Widget):
    def __init__(self, color, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Color(*color)
            self.ellipse = Ellipse(size=(60, 60))
        self.bind(pos=self.update_ellipse, size=self.update_ellipse)

    def update_ellipse(self, *args):
        # Оновлення позиції еліпса, щоб він був в центрі віджета
        self.ellipse.pos = (self.x + 40, self.y + 60)  # Послідовно оновлюємо позицію еліпса на основі положення віджета


class GamePlace(BoxLayout):
    triangle_width = NumericProperty(100)  # Ширина трикутників
    triangle_height = NumericProperty(290)  # Висота трикутників

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.bind(size=self.update_triangles)  # Реагуємо на зміну розміру

        top = AnchorLayout(anchor_y='bottom')
        top_up = BoxLayout(orientation='horizontal')
        top.add_widget(top_up)

        # Додавання верхніх еліпсів
        for i in range(12):
            el = EllipseWidget(color=(94 / 255, 80 / 255, 61 / 255, 1))
            top_up.add_widget(el)

        self.add_widget(top)

        center = AnchorLayout(anchor_y='center')
        center.add_widget(Label(text='                               ', size_hint=(1, 1)))
        self.add_widget(center)
        center1 = AnchorLayout(anchor_y='center')
        center1.add_widget(Label(text='                               ', size_hint=(1, 1)))
        self.add_widget(center1)

        # Нижній макет
        bottom = AnchorLayout(anchor_y='bottom')
        bottom_down = BoxLayout(orientation='horizontal')
        bottom.add_widget(bottom_down)

        # Додавання нижніх еліпсів
        for i in range(12):
            el = EllipseWidget(color=(1, 1, .85, 1))
            bottom_down.add_widget(el)

        self.add_widget(bottom)

        # Малюємо початкові трикутники (один раз)
        self.draw_triangles()

    def draw_triangles(self):
        with self.canvas:
            x = 30
            y = 75 + (self.height - self.triangle_height) / 2  # Вертикальне центрування
            z = x + self.triangle_width

            for i in range(12):
                if i % 2 == 0:
                    Color(140/255, 80/255, 36/255, 1)
                else:
                    Color(.8, 1, .85, 1)

                Line(points=(x, 0, y, self.triangle_height, z, 0), close=True)
                x += self.triangle_width
                y += self.triangle_width
                z += self.triangle_width

            x = 30
            y = 75 + (self.height - self.triangle_height) / 2
            z = x + self.triangle_width

            for i in range(12):
                if i % 2 != 0:
                    Color(140/255, 80/255, 36/255, 1)
                else:
                    Color(.8, 1, .85, 1)

                Line(points=(x, self.height, y, self.height - self.triangle_height, z, self.height), close=True)
                x += self.triangle_width
                y += self.triangle_width
                z += self.triangle_width


    def update_triangles(self, *args):
        # Оновлюємо розміри трикутників залежно від розміру вікна
        self.triangle_width = self.width / 12  # 12 трикутників по горизонталі
        self.triangle_height = self.height / 2.5  # Пропорційна висота

        # Очищуємо тільки інструкції малювання ліній
        self.canvas.before.clear()
        self.canvas.after.clear()

        # Малюємо нові трикутники
        self.draw_triangles()



if __name__ == '__main__':
    MyApp().run()