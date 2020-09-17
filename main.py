from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class BoxApp(App):
    def build(self):
        b1 = BoxLayout()

        b1.add_widget(Button(text="Кнопка"))

if __name__ == "__main__":
    BoxApp().run()