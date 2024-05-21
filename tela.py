from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

Window.size = (360, 640)

class GerenciadorTelas(ScreenManager):
    pass

class PrimeiraTela(Screen):
    pass
   

class SegundaTela(Screen):
    pass

class MyApp(App):
    def build(self):
        return GerenciadorTelas()

MyApp().run()
