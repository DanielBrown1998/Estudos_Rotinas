from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.swiper import MDSwiper, MDSwiperItem

Builder.load_file(r'./assets/screens/intro.kv')


class Check(MDCheckbox):
    def on_checkbox_active(self, checkbox: object, value: object) -> None:
        if value:
            print('The checkbox', checkbox, 'is active', 'and', checkbox.state, 'state')
        else:
            print('The checkbox', checkbox, 'is inactive', 'and', checkbox.state, 'state')


class Select(MDBoxLayout):
    texto = StringProperty()


class Config(MDSwiperItem):
    ...


class MySwiper(MDSwiperItem):
    image = StringProperty()


class Body(MDSwiper):
    image = StringProperty()


class Info(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print(self.name)
        self.add_widget(
            Body()
        )
