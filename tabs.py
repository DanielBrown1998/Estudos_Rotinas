from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import StringProperty
from kivymd.uix.card import MDCard
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.scrollview import MDScrollView
from kivy.core.window import Window
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.stacklayout import MDStackLayout

Builder.load_file(r'./assets/screens/tabs.kv')


class Check(MDCheckbox):

    def on_checkbox_active(self, checkbox: object, value: object) -> None:
        if value:
            print('The checkbox', checkbox, 'is active', 'and', checkbox.state, 'state')
        else:
            print('The checkbox', checkbox, 'is inactive', 'and', checkbox.state, 'state')


class Content(MDRelativeLayout):
    pass


class Disciplina(MDCard):
    hora = StringProperty()
    text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.width = Window.size[0] - dp("40")

    def change_me(self, my_id):
        self.ids.texto.text = 'adicionado'


class Day(MDStackLayout):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print('day')
        # todo buscar os dados no banco de dados referente à tabela do dia


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
