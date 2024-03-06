from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.popup import Popup
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDButton, MDIconButton
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.stacklayout import MDStackLayout

import json
Builder.load_file(r'./assets/screens/tabs.kv')


class PopupButton(MDButton):
    tarefa = StringProperty(None)
    hora = StringProperty(None)
    day = StringProperty(None)


class PopUpCard(Popup):
    day = StringProperty()
    hora = StringProperty()

    def __init__(self, hora: str, day: str) -> None:
        super().__init__()
        self.hora = hora
        self.day = day


class ContentPopUp(MDBoxLayout):
    day = StringProperty()
    hora = StringProperty()
    dismiss = Popup.dismiss


class ContentButton(MDIconButton):
    hora = StringProperty()
    day = StringProperty()

    def update_data(self, hora: str):
        self.day = self.parent.change()
        popup = PopUpCard(
            hora=hora,
            day=self.day,
        )
        popup.open()


class Texto(MDLabel):
    ...


class Check(MDCheckbox):

    def on_checkbox_active(self, checkbox: object, value: object) -> None:
        if value:
            print('The checkbox', checkbox, 'is active', 'and', checkbox.state, 'state')
        else:
            print('The checkbox', checkbox, 'is inactive', 'and', checkbox.state, 'state')


class Content(MDRelativeLayout):
    name_tab = StringProperty()
    hora = StringProperty()

    def change(self):
        return self.parent.change()


class Disciplina(MDCard):
    hora = StringProperty()
    text = StringProperty()

    def change(self):
        return self.parent.change()


class Day(MDStackLayout):
    def change(self):
        return self.parent.change()


class Scroll(MDScrollView):

    def change(self):
        return self.parent.change()


class Tabs(MDScreen):

    def change(self):
        return self.name
