from kivy.lang import Builder
from kivy.metrics import dp, sp
from kivy.properties import StringProperty
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.scrollview import MDScrollView
from kivy.core.window import Window
Builder.load_file(r'./assets/screens/tabs.kv')


class Hour(MDCard):
    hora = StringProperty()
    disciplina = StringProperty()


class Day(MDBoxLayout):
    week = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print('day')
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
        for time in range(8, 20):
            self.add_widget(
                Hour(
                    hora=f"{time}:00",
                    id=f"{time}:00",
                    disciplina=self.id,
                    width=Window.size[0]*.9
                )
            )


class Content(MDBoxLayout):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)
        print('content')
        week = 'segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sabado', 'domingo'
        for day in week:
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


class Tabs(MDScreen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print('tabs')
