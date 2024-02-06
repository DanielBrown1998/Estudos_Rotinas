from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import StringProperty
from kivymd.uix.card import MDCard
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.scrollview import MDScrollView
from kivy.core.window import Window
from kivymd.uix.stacklayout import MDStackLayout

Builder.load_file(r'./assets/screens/tabs.kv')


class Content(MDRelativeLayout):
    pass


class Disciplina(MDCard):
    hora = StringProperty()
    text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.width = Window.size[0] - dp("40")


class Day(MDStackLayout):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print('day')
        # todo buscar os dados no banco de dados referente à tabela do dia

    def on_touch_down(self, touch):
        super().on_touch_down(touch)
        print(self.ids.keys())


class Scroll(MDScrollView):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.add_widget(
            Day(
                width=Window.size[0]
            )
        )


class Tabs(MDScreen):
    pass
