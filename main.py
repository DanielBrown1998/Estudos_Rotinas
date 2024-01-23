from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from pathlib import Path


# configuração inicial
# Window.size = (320, 650)


# Widget de gerenciamento
class Principal(MDScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


# class principal
class MainApp(MDApp):

    KIVY_HOME = Path(__file__).parent

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

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
