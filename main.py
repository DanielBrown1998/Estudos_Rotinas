import math

from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import StringProperty, ColorProperty
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.navigationbar import MDNavigationBar, MDNavigationItem
from pathlib import Path

from kivymd.uix.screenmanager import MDScreenManager


class BaseMDNavigationItem(MDNavigationItem):
    icon = StringProperty()
    text = StringProperty()


class Nav(MDNavigationBar):
    pass


# Widget de gerenciamento
class Principal(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.day = app.today()
        if self.day is not None:
            self.ids.screen_manager.current = self.day


class Manager(MDScreenManager):
    pass


# class principal
class MainApp(MDApp):
    # font_file
    KIVY_HOME = Path(__file__).parent

    # Paleta
    color_font_focus = ColorProperty('#234CAD')
    color_shadow = ColorProperty('#31477A')
    background = ColorProperty('#FFFFFF')
    background_two = ColorProperty('#2B3347')
    color_font = ColorProperty('#292C33')

    def on_start(self) -> bool:
        super().on_start()
        """
        todo inicializar o banco de dados
        caso os campos estejam vazios retorne False
        """
        return True

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def today(self) -> str | None:

        """
        todo buscar os dados do banco de dados:
        todo caso esteja vazio retorne None
        """
        from datetime import datetime
        day = datetime.weekday(datetime.today())
        if day == 6:
            return 'domingo'
        elif day == 0:
            return 'segunda'
        elif day == 1:
            return 'terça'
        elif day == 2:
            return 'quarta'
        elif day == 3:
            return 'quinta'
        elif day == 4:
            return 'sexta'
        elif day == 5:
            return 'sabado'

    def on_switch_tabs(
            self,
            bar: MDNavigationBar,
            item: MDNavigationItem,
            item_icon: str,
            item_text: str,
    ):
        self.root.ids.screen_manager.current = item_text

    def build(self):
        self.theme_cls.theme_style = 'Light'
        self.theme_cls.material_style = 'M3'
        self.theme_cls.dynamic_color = True
        self.title = 'Studie'
        Builder.load_file('assets/screens/main.kv')
        return Principal()


if __name__ == '__main__':
    app = MainApp()
    app.run()
