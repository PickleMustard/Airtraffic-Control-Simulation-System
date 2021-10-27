from kivy.uix.screenmanager import ScreenManager, Screen

class WindowManager(ScreenManager):
    pass

class LoginWindow(Screen):
    def testFunction(self):
        print("TEST FUNCTION")

class MainMenuWindow(Screen):
    pass