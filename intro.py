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
            pass
        else:
            pass


class Select(MDBoxLayout):
    texto = StringProperty()


class Config(MDSwiperItem):
    pass


class MySwiper(MDSwiperItem):
    image = StringProperty()


class Body(MDSwiper):
    pass


class Info(MDScreen):
    pass
