from kivy.animation import Animation
from kivy.lang import Builder
from kivy.properties import StringProperty, NumericProperty
from kivy.uix.popup import Popup
from kivymd.uix.behaviors import TouchBehavior, ScaleBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDButton, MDIconButton
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.stacklayout import MDStackLayout
from main import MainApp as App

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
        pass


class Content(MDRelativeLayout):
    name_tab = StringProperty()
    hora = StringProperty()

    def change(self):
        return self.parent.change()


class Disciplina(
    MDCard,
    TouchBehavior,
    ScaleBehavior,
):
    hora = StringProperty()
    text = StringProperty()
    scale_value_x = NumericProperty(1)
    scale_value_y = NumericProperty(1)
    scale_value_z = NumericProperty(1)

    # busca a nome da screen em vigência
    def change(self):
        return self.parent.change()

    def on_long_touch(self, touch, *args):
        """
        Apaga os dados contidos no widget

        :param touch:
        :param args:
        :return:
        """
        anim = (
            Animation(
                scale_value_x=1.01,
                scale_value_y=1.01,
                scale_value_z=1.01,
                d=0.2,
            ) +
            Animation(
                scale_value_x=self.scale_value_x,
                scale_value_y=self.scale_value_y,
                scale_value_z=self.scale_value_z,
                d=0.2,
            )
        )
        anim.start(self)
        App.get_running_app().root.ids[f"{self.change()}"]\
            .ids[f'content_{self.hora[:2]}'].ids.texto.text = ''


class Day(MDStackLayout):
    # busca a nome da screen em vigência
    def change(self):
        return self.parent.change()


class Scroll(MDScrollView):

    # busca a nome da screen em vigência
    def change(self):
        return self.parent.change()


class Tabs(MDScreen):

    # busca a nome da screen em vigência
    def change(self):
        return self.name
