<<<<<<< HEAD
from kivy.app import App
from kivy.lang import Builder

# Contains window classes
=======
# main.py
# Description: 
#   Contains the definition of the application

from kivy.app import App
from kivy.lang import Builder
>>>>>>> a94f89242ea14abd82b71faf5868975c6dfe958f
import Screens

main = Builder.load_file("main.kv")
    
class Air_Traffic_Control_System(App):
    def build(self):
        return main

<<<<<<< HEAD

=======
>>>>>>> a94f89242ea14abd82b71faf5868975c6dfe958f
if __name__ == '__main__':
    Air_Traffic_Control_System().run()