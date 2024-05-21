from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.lang import Builder

Window.size = (360, 640)

class GerenciadorTelas(ScreenManager):
    pass

class PrimeiraTela(Screen):
    pass
   

class SegundaTela(Screen):
    pass

class TerceiraTela(Screen):
    pass

class MyApp(App):
    def build(self):
        Builder.load_file('MyApp.kv')
        return GerenciadorTelas()

MyApp().run()
