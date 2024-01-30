from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import StringProperty, NumericProperty
from kivymd.uix.behaviors import ScaleBehavior, HoverBehavior, RotateBehavior
from kivymd.uix.button import MDFabButton
from kivymd.uix.screen import MDScreen
from kivymd.uix.scrollview import MDScrollView
from kivy.core.window import Window
from kivymd.uix.stacklayout import MDStackLayout
from kivymd.uix.textfield import MDTextField, MDTextFieldHintText, MDTextFieldMaxLengthText
from kivy.animation import Animation
Builder.load_file(r'./assets/screens/tabs.kv')


class MyButton(
    MDFabButton,
    ScaleBehavior,
    HoverBehavior,
    RotateBehavior
):

    scale_value_x = NumericProperty(.9)
    scale_value_y = NumericProperty(.9)

    def on_enter(self) -> None:
        anim = Animation(
            scale_value_x=1.,
            scale_value_y=1.,
            rotate_value_angle=90,
            duration=.2,
            t='in_out_quad'
        )
        anim.start(self)

    def on_leave(self) -> None:
        anim = Animation(
            scale_value_x=.9,
            scale_value_y=.9,
            rotate_value_angle=0,
            duration=.2,
            t='in_out_quad'
        )
        anim.start(self)


class Disciplina(MDTextField):
    hora = StringProperty()


class Day(MDStackLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print('day')
        # todo buscar os dados no banco de dados referente à tabela do dia

        for time in range(6, 24):
            self.add_widget(
                Disciplina(
                    MDTextFieldHintText(
                        text=f"{time}:00",
                        id=f"{time}:00_disciplina",
                    ),
                    MDTextFieldMaxLengthText(
                        max_text_length=20,
                    ),
                    text='horário vago',
                )
            )
            my_button = MyButton(
                id=f"{time}:00_button",
            )
            self.add_widget(
                my_button
            )


class Scroll(MDScrollView):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.add_widget(
            Day(
                width=Window.size[0]
            )
        )

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
        print(self.name)
