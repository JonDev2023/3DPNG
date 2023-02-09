'''
3DPNG
Directed by JonDev2023
Created by JonDev2023
Released by JonDev2023
Programmed by JonDev2023
'''

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager

class ADM(ScreenManager):
    pass

class Modeling(Screen):
    pass

class Runner(App):
    def build(self):
        self.title = '3DPNG'
        return Builder.load_file('index.kv')

if __name__ == '__main__':
    Runner().run()