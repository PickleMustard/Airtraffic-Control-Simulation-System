# main.py
# Description:
#	Contains the definition of the application

from kivy.app import App
from kivy.lang import Builder

main = Builder.load_file("main.kv")
    
class Air_Traffic_Control_System(App):
    def build(self):
        return main

if __name__ == '__main__':
    Air_Traffic_Control_System().run()