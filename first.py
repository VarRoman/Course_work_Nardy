from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.codeinput import CodeInput
from pygments.lexers import HtmlLexer
from kivy.uix.floatlayout import FloatLayout

class MyApp(App):
    def build(self):
        # return CodeInput(lexer=HtmlLexer())
        fl = FloatLayout(size=(400, 400))
        fl.add_widget(Button(text='Click Me!',
            font_size=40,
            on_press = self.btn_press,
            background_color=[0, 1, 0, 1],
            background_normal='',
            size_hint=(.5, .5),
            pos=(200, 0)))

        return fl
    def btn_press(self, instance):
        print('Button pressed')
        instance.text = 'I was clicked'

if __name__ == '__main__':
    MyApp().run()
