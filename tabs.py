from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import StringProperty
from kivymd.uix.button import MDButton
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.scrollview import MDScrollView
from kivy.core.window import Window
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.stacklayout import MDStackLayout

Builder.load_file(r'./assets/screens/tabs.kv')


class MyButton(MDButton):
    tarefa = StringProperty(None)
    hora = StringProperty(None)
    day = StringProperty(None)

    def update(self, tarefa: str, hora: str, day: str) -> None:
        self.tarefa = tarefa
        self.hora = hora
        self.day = day
        print(self.tarefa, self.day, self.hora)


class PopUpCard(MDCard):
    day = StringProperty()


class PopUpScreen(MDScreen):
    day = StringProperty()


class Texto(MDLabel):

    def on_touch_down(self, touch):
        super().on_touch_down(touch)
        if touch.is_double_tap and touch.pos[0] < Window.size[0]*.85:
            self.parent.change()


class Check(MDCheckbox):

    def on_checkbox_active(self, checkbox: object, value: object) -> None:
        if value:
            print('The checkbox', checkbox, 'is active', 'and', checkbox.state, 'state')
        else:
            print('The checkbox', checkbox, 'is inactive', 'and', checkbox.state, 'state')


class Content(MDRelativeLayout):

    def change(self):
        self.parent.change()


class Disciplina(MDCard):
    hora = StringProperty()
    text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.width = Window.size[0] - dp("40")

    def change(self):
        self.parent.change()


class Day(MDStackLayout):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print('day')

        # todo buscar os dados no banco de dados referente à tabela do dia

    def change(self):
        self.parent.change()


class Scroll(MDScrollView):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(
            Day(
                width=Window.size[0]
            )
        )

    def change(self):
        self.parent.change()


class Tabs(MDScreen):

    def change(self):
        self.parent.screen_previous = self.name
        self.parent.current = 'popup'
