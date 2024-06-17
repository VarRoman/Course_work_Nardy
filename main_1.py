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

# Builder.load_file('main.kv')

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
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

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


if __name__ == '__main__':
    MyApp().run()
