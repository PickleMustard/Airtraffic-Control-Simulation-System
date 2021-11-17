#This code only have comments on the Login page as that is what I have wrote
#Other comments about the code can be found on someone elses branch
#When trying to login use "Admin1" for username and "Test1234" for the password
#My verson only 3 buttons work on the main menu Schedule, Plane Info, and Logout
#again, other comment about how they work can be found on a different branch (check Noah's branch)
#he should also have implement more buttons
from kivy.metrics import dp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.label import Label
from kivy.properties import NumericProperty, ObjectProperty
from kivy.properties import StringProperty

#class to change between screens
from kivy.uix.widget import Widget


class WindowManager(ScreenManager):
    login = ObjectProperty(None)
    mainMenu = ObjectProperty(None)

#this hos the code for the radar page
class RadarWindow(Screen):
    planes = [ObjectProperty(None), ObjectProperty(None), ObjectProperty(None), ObjectProperty(None)]

class Plane(Widget):
    pass
#this hold the code for the login page
class LoginWindow(Screen):
    #ObjectPropert retrieve the text input from the .kv file
    userSubmit = ObjectProperty(None)
    passwordSubmit = ObjectProperty(None)
    #textSubmit is use to display successful login or a message saying wrong username and/or password
    textSubmit = StringProperty("")

    # account is a list of tuple that has username as key and password as value
    # Dillon have the list of valid user here
    account = [("Admin1", "Test1234"),
               ("Admin2", "Password")]

    #This function is called when the submit button is hit
    def onSubmit(self):

        valid = False

        #this for loop checks if the username and password are in the account list
        for i, tuple in enumerate(self.account):
            if (tuple[0] == self.userSubmit.text and tuple[1] == self.passwordSubmit.text):
                valid = True;

        #if it is, set textSubmit to success and change to the main menu
        if valid:
            self.textSubmit = "Success"
            self.manager.current = "menuScreen"
        #else display incorrect username or password message
        else:
            self.textSubmit = "Incorrect username or password."


class MainMenuWindow(Screen):
    pass


# Remove these two imports once PlaneInfoList.populate is implemented
from random import sample, randint
from string import ascii_lowercase


class PlaneInfoWindow(Screen):
    pass


class PlaneInfoRow(RecycleDataViewBehavior, BoxLayout):
    dataName = StringProperty()
    dataValue = StringProperty()

    def __init__(self, **kwargs):
        super(PlaneInfoRow, self).__init__(**kwargs)


class PlaneInfoList(BoxLayout):
    def __init__(self, **kwargs):
        super(PlaneInfoList, self).__init__(**kwargs)
        Clock.schedule_once(self.finish_init, 0)

    def finish_init(self, dt):
        self.populate()

    # Dillon I need a query here for a plane's info!!!!---------------------------------------
    def populate(self):
        print("Populating")
        self.rv.data = [
            {'dataName': ''.join(sample(ascii_lowercase, 6)),
             'dataValue': str(randint(0, 2000))}
            for x in range(50)]

    def sort(self):
        self.rv.data = sorted(self.rv.data, key=lambda x: x['name.text'])

    def clear(self):
        self.rv.data = []

    def insert(self, value):
        self.rv.data.insert(0, {
            'name.text': value or 'default value', 'value': 'unknown'})

    def update(self, value):
        if self.rv.data:
            self.rv.data[0]['name.text'] = value or 'default new value'
            self.rv.refresh_from_data()

    def remove(self):
        if self.rv.data:
            self.rv.data.pop(0)

    # Populate the list at the start - not functioning


#    def __post_init__(self, **kwargs):
#        super().__init__(**kwargs)
#        PlaneInfoList

class ScheduleWindow(Screen):
    pass


# https://github.com/kivy/kivy/issues/6582
class ArrivalList(BoxLayout):
    # Dillon I need a query here for a plane's info!!!!---------------------------------------
    def populate(self):
        self.rv.data = [
            {'name.text': ''.join(sample(ascii_lowercase, 6)),
             'value': str(randint(0, 2000))}
            for x in range(50)]


class DepartureList(BoxLayout):
    # Dillon I need a query here for a plane's info!!!!---------------------------------------
    def populate(self):
        self.rv.data = [
            {'name.text': ''.join(sample(ascii_lowercase, 6)),
             'value': str(randint(0, 2000))}
            for x in range(50)]
