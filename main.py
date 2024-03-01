# import math
from connection import create_database, drop_database

from kivy.lang import Builder
# from kivy.metrics import dp
from kivy.properties import StringProperty, ColorProperty, ListProperty
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.navigationbar import MDNavigationBar, MDNavigationItem
from pathlib import Path

from kivymd.uix.screenmanager import MDScreenManager

# todo criar uma arquivo json ou cache do kivy
#  para guardar algumas informações como:
#  database já criado;
#  primeiro acesso;
#  guardar checkpoints


class BaseMDNavigationItem(MDNavigationItem):
    icon = StringProperty()
    text = StringProperty()


class Nav(MDNavigationBar):
    pass


# Widget de gerenciamento
class Principal(MDBoxLayout):
    day = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if app.first_access:
            self.ids.screen_manager.current = app.title
        else:
            self.day = app.today()
            if self.day is not None:
                self.ids.screen_manager.current = self.day


class Manager(MDScreenManager):
    screen_previous = StringProperty()


# class principal
class MainApp(MDApp):
    # font_file
    KIVY_HOME = Path(__file__).parent
    days = ListProperty(['segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sabado', 'domingo'])

    first_access = True  # todo esse elemento é provisório

    # Paleta
    color_font_focus = ColorProperty('#234CAD')
    color_shadow = ColorProperty('#31477A')
    background = ColorProperty('#FFFFFF')
    background_two = ColorProperty('#2B3347')
    color_font = ColorProperty('#292C33')

    def __init__(self, first_access=True, **kwargs):
        super().__init__(**kwargs)
        if first_access:
            print('criando database')
            create_database()

    def on_pause(self):
        super().on_pause()
        return True

    def on_resume(self):
        super().on_resume()
        return True

    def on_stop(self):
        super().on_stop()
        # todo this is temporary
        print(f'excluindo database')
        drop_database()
        return True

    def build_config(self, config):
        super().build_config(config)
        return True

    def today(self) -> str | None:
        from datetime import datetime
        day = datetime.weekday(datetime.today())
        return self.days[day]

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
