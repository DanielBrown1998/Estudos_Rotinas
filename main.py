import datetime
import json
from json.decoder import JSONDecodeError
from kivy.lang import Builder
from kivy.properties import StringProperty, ColorProperty, ListProperty
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
    KIVY_HOME = Path(__file__).parent
    days = ListProperty(
        ['segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sabado', 'domingo']
    )

    first_access = True
    clean_checks_weekday: int = 0  # segunda
    delete: bool = False


    # Paleta
    color_font_focus = ColorProperty('#234CAD')
    color_shadow = ColorProperty('#31477A')
    background = ColorProperty('#FFFFFF')
    background_two = ColorProperty('#2B3347')
    color_font = ColorProperty('#292C33')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pseud_cache = None  # local onde ficara armazenado o 'cache'
        self.hora: str | None = None  # a hora do elemento
        self.attr: tuple | None = None  # o valor do check e texto
        self.attrs = None  # listas com os checks e textos salvos

        # calculando o dia de
        self.day = datetime.datetime.today().strftime("%d/%m/%Y")
        self.weekday = datetime.datetime.weekday(datetime.datetime.today())
        if self.weekday != 0:
            self.weekday = 7 - self.weekday
            self.clean_checks_day = str(int(self.day[:2]) + self.weekday) + self.day[2:]
            print(self.clean_checks_day)
        try:
            with open(f'data/pseud_cache.json', 'r', encoding='utf-8') as file:
                print('carregando o pseud_cache')
                self.pseud_cache = json.load(file)
                self.first_access = self.pseud_cache['first_access']
                self.clean_checks_day_cache = self.pseud_cache['clean_checks_day']
        except FileNotFoundError:
            print('arquivo nçao encontrado')
            print(self.day)
            print(self.clean_checks_day)
        except JSONDecodeError:
            print('o arquivo está vazio!!!')

    def on_pause(self):
        super().on_pause()
        self.on_stop()
        return True

    def on_resume(self):
        super().on_resume()
        self.on_start()
        return True

    def on_start(self):
        super().on_start()
        self.fps_monitor_start()
        if self.day >= self.clean_checks_day_cache:
            for day in self.days:
                print(f'Carregando os atributos de {day}:')
                try:
                    with open(f'./data/{day}.json', 'r', encoding='utf-8') as file:
                        self.attrs = json.load(file)
                        for item in self.attrs:
                            for key, value in item.items():
                                self.hora = key
                                self.attr = value
                                app.root.ids[f'{day}'].ids[f'content_\
{self.hora[:2]}'].ids.check.active = False
                                app.root.ids[f'{day}'].ids[f'content_\
{self.hora[:2]}'].ids.texto.text = self.attr[1]
                except FileNotFoundError:
                    print(f'checks do dia {day} não encontrado')
                except JSONDecodeError:
                    print('o arquivo está vazio!!!')

        else:
            for day in self.days:
                print(f'Carregando os atributos de {day}:')
                try:
                    with open(f'./data/{day}.json', 'r', encoding='utf-8') as file:
                        self.attrs = json.load(file)
                        for item in self.attrs:
                            for key, value in item.items():
                                self.hora = key
                                self.attr = value
                                app.root.ids[f'{day}'].ids[f'content_\
{self.hora[:2]}'].ids.check.active = self.attr[0]
                                app.root.ids[f'{day}'].ids[f'content_\
{self.hora[:2]}'].ids.texto.text = self.attr[1]
                except FileNotFoundError:
                    print(f'checks do dia {day} não encontrado')
                except JSONDecodeError:
                    print('o arquivo está vazio!!!')
        return True

    def on_stop(self):
        super().on_stop()
        self.attrs = []
        for day in self.days:
            print(f'Salvando os dados de {day}:')
            with open(f'./data/{day}.json', 'w', encoding='utf-8') as file:
                for hour in range(6, 24):
                    if hour < 10:
                        self.attrs.append(
                            {
                                f"0{hour}:00": (
                                    app.root.ids[f'{day}'].ids[f'content_0{hour}'].ids.check.active,
                                    app.root.ids[f'{day}'].ids[f'content_0{hour}'].ids.texto.text
                                )
                            }
                        )
                    else:
                        self.attrs.append(
                            {
                                f'{hour}:00': (
                                    app.root.ids[f'{day}'].ids[f'content_{hour}'].ids.check.active,
                                    app.root.ids[f'{day}'].ids[f'content_{hour}'].ids.texto.text
                                )
                            }
                        )
                json.dump(
                    self.attrs,
                    file,
                    indent=2,
                    ensure_ascii=False
                )
            self.attrs.clear()

        self.pseud_cache = {
            'first_access': self.first_access,
            'clean_checks_day': self.clean_checks_day
        }
        with open('data/pseud_cache.json', 'w', encoding='utf-8') as file:
            print('Salvando o pseud_cache')
            json.dump(
                self.pseud_cache,
                file,
                ensure_ascii=False,
                indent=2
            )

        return True

    def build_config(self, config):
        super().build_config(config)
        return True

    def today(self) -> str | None:
        from datetime import datetime
        day = datetime.weekday(datetime.today())
        return self.days[day]

    def restore_data(self) -> str:
        if self.delete is True:
            for day in self.days:
                print(f'Carregando os atributos de {day}:')
                try:
                    with open(f'./data/{day}.json', 'r', encoding='utf-8') as file:
                        self.attrs = json.load(file)
                        for item in self.attrs:
                            for key, value in item.items():
                                self.hora = key
                                self.attr = value
                                app.root.ids[f'{day}'].ids[f'content_\
{self.hora[:2]}'].ids.check.active = self.attr[0]
                                app.root.ids[f'{day}'].ids[f'content_\
{self.hora[:2]}'].ids.texto.text = self.attr[1]
                except FileNotFoundError:
                    print('não há dados para restaurar')
                    return 'não há dados para restaurar'
                except JSONDecodeError:
                    print('não há dados para restaurar')
                    return 'não há dados para restaurar'
            self.delete = False
            print('dados recuperados')
            return 'dados recuperados'
        print('os dados não foram recuperados')
        return 'os dados não foram excluídos'

    def delete_data(self) -> str:
        if self.delete is False:
            for day in self.days:
                for hora in range(6, 24):
                    if hora < 10:
                        app.root.ids[f'{day}'].ids[f'content_0\
{hora}'].ids.check.active = False
                        app.root.ids[f'{day}'].ids[f'content_0\
{hora}'].ids.texto.text = ''
                    else:
                        app.root.ids[f'{day}'].ids[f'content_\
{hora}'].ids.check.active = False
                        app.root.ids[f'{day}'].ids[f'content_\
{hora}'].ids.texto.text = ''
            self.delete = True
            print('arquivos deletados')
            return 'arquivos deletados'
        print('arquivos já foram deletados')
        return 'arquivos já foram deletados'

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
