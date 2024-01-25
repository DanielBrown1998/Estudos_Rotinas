from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen

Builder.load_file(r'./assets/screens/intro.kv')


class Body(MDBoxLayout):
    pass


class Info(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print(self.name)
        self.add_widget(
            Body()
        )
