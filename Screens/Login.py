import kivy
from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen

class LoginWidget(Widget):
    textSubmit = StringProperty("")
    #account is a list of tuple that has username as key and password as value
    #Dillon have the list of valid user here
    account = [("Admin1", "Test1234"),
             ("Admin2", "Password")]


    def onSubmit(self, subButton, userName, password):

        valid = False

        for x in self.account:
            for key, value in x:
                if(key == userName.text and value == password.text):
                    self.valid = True;

        if self.valid:
            self.textSubmit = "Success"
            #put transition to main menu page here
        else:
            self.textSubmit = "Incorrect username or password."



class Login(App):
    pass

Login().run()