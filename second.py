from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.textinput import TextInput

class BoxApp(App):
    def build(self):
        al = AnchorLayout()
        bl = BoxLayout(orientation='vertical', padding=10, size_hint=(None, None), size=(400, 400))

        bl.add_widget(TextInput())
        bl.add_widget(TextInput())
        bl.add_widget(Button(text="Click me!"))

        al.add_widget(bl)
        return al


if __name__ == '__main__':
    BoxApp().run()