from kivy.lang import Builder
from kivy.metrics import dp, sp
from kivy.properties import StringProperty
from kivymd.uix.button import MDButton, MDFabButton
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.scrollview import MDScrollView
from kivy.core.window import Window
from kivymd.uix.stacklayout import MDStackLayout
from kivymd.uix.textfield import MDTextField, MDTextFieldHintText, MDTextFieldTrailingIcon, MDTextFieldMaxLengthText

Builder.load_file(r'./assets/screens/tabs.kv')


class MyButton(MDFabButton):
    pass


class Disciplina(MDTextField):
    hora = StringProperty()


class Day(MDStackLayout):
    week = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print('day')

        for time in range(8, 20):
            self.add_widget(
                Disciplina(
                    MDTextFieldHintText(
                        text=f"{time}:00",
                        id=f"{time}:00_disciplina",
                    ),
                    MDTextFieldMaxLengthText(
                        max_text_length=20,
                    ),
                    text=self.week,
                    # disciplina=self.id,
                    # width=Window.size[0]*.4
                )
            )
            my_button = MyButton(
                id=f"{time}:00_button",
            )
            self.add_widget(
                my_button
            )


class Content(MDBoxLayout):
    week = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print('content')
        week = 'segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sabado', 'domingo'
        for day in week:
            self.add_widget(
                MDLabel(
                    text=self.week,
                    valign='center',
                    halign='center',
                    bold=True,
                    font_size=sp(32),
                    padding=dp(10),
                    size_hint_y=None,
                    height=dp(50),

                )
            )
            self.add_widget(
                Day(
                    week=day,
                    id=day,
                    width=Window.size[0]
                )
            )

class Scroll(MDScrollView):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_scroll_start(self, touch, check_children=True):
        if super().on_scroll_start(touch):
            pass
        return True

    def on_scroll_move(self, touch):
        if super().on_scroll_move(touch):
            pass
        return True

    def on_scroll_stop(self, touch, check_children=True):
        if super().on_scroll_stop(touch):
            pass
        return True


class Tabs(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print('tabs')
