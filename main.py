from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.navigationbar import MDNavigationBar, MDNavigationItem
from pathlib import Path
from kivymd.icon_definitions import md_icons


class BaseMDNavigationItem(MDNavigationItem):
    icon = StringProperty()
    text = StringProperty()


class Nav(MDNavigationBar):
    pass


# Widget de gerenciamento
class Principal(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


# class principal
class MainApp(MDApp):

    KIVY_HOME = Path(__file__).parent

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # print(*[key for key in md_icons.keys()])

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
        self.theme_cls.backgroundColor = 'white'
        self.theme_cls.device_orientation = 'vertical'
        self.theme_cls.primaryContainerColor = 'gray'
        self.theme_cls.secondaryContainerColor = 'black'
        self.theme_cls.material_style = 'M3'
        self.title = 'Studie'
        Builder.load_file('assets/screens/main.kv')
        return Principal()


if __name__ == '__main__':
    MainApp().run()
