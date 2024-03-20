from kivy.lang import Builder
from kivy.properties import StringProperty, ColorProperty
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.chip import MDChip
from kivymd.uix.list import MDListItem
from kivymd.uix.screen import MDScreen
from kivymd.uix.swiper import MDSwiper, MDSwiperItem

Builder.load_file(r'./assets/screens/intro.kv')


class Item(MDListItem):
    icon = StringProperty()
    principal_text = StringProperty()
    support_text = StringProperty()


class Dados(MDChip):
    dados_color = ColorProperty()


class Select(MDBoxLayout):
    texto = StringProperty()


class Config(MDSwiperItem):
    pass


class Intro(MDSwiperItem):
    pass


class MySwiper(MDSwiperItem):
    image = StringProperty()


class Body(MDSwiper):
    pass


class Info(MDScreen):
    pass
