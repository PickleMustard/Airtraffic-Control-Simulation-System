#This code only have comments on the Login page as that is what I have wrote
#Other comments about the code can be found on someone elses branch
#When trying to login use "Admin1" for username and "Test1234" for the password
#My verson only 3 buttons work on the main menu Schedule, Plane Info, and Logout
#again, other comment about how they work can be found on a different branch (check Noah's branch)
#he should also have implement more buttons
from kivy.metrics import dp
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.properties import NumericProperty, ObjectProperty
from kivy.properties import StringProperty
from kivy.animation import Animation
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.config import Config

#this variable is so that animation does not start until a certain sceen in on
startMoving = False


#this class is to change between screens
class WindowManager(ScreenManager):
    login = ObjectProperty(None)
    mainMenu = ObjectProperty(None)
    radar = ObjectProperty(None)

#this hos the code for the radar page
class RadarWindow(Screen):

    #these are the variable that corresponds with planes
    global startMoving
    plane1 = ObjectProperty(None)
    plane2 = ObjectProperty(None)
    plane3 = ObjectProperty(None)
    plane4 = ObjectProperty(None)
    label1 = ObjectProperty(None)
    label2 = ObjectProperty(None)
    label3 = ObjectProperty(None)
    label4 = ObjectProperty(None)
    planeInfo = ObjectProperty(None)

    

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        #update screen every .1 seconds
        Clock.schedule_interval(self.update, 0.1)
        
    #the method for the animation
    def update(self, dt):
        #get current plan posistion
        x1, y1 = self.plane1.pos
        x2, y2 = self.plane2.pos
        x3, y3 = self.plane3.pos
        x4, y4 = self.plane4.pos
        
        #displaying plane infor
        self.label1.text = "ID               : 000001\nPosition     : " + str(int(x1)) + ", " + str(int(y1)) + " \nAirline        : American Airlines\nStatus        : Good" 
        self.label2.text = "ID               : 000002\nPosition     : " + str(int(x2)) + ", " + str(int(y2)) + " \nAirline        : Delta Airlines\nStatus        : Good"  
        self.label3.text = "ID               : 000003\nPosition     : " + str(int(x3)) + ", " + str(int(y3)) + " \nAirline        : United Airlines\nStatus        : Good"  
        self.label4.text = "ID               : 000004\nPosition     : " + str(int(x4)) + ", " + str(int(y4)) + " \nAirline        : American Airlines\nStatus        : Approaching" 

        #pause movement until the radar screen is shown
        if(startMoving):
            #updating plan position
            #this is for demonstation purposes
            #if we had access to actual plane movement this is where it will go
            self.plane1.pos = (x1 + 5, y1 + 5)
            self.plane2.pos = (x2 - 5, y2 + 2)
            self.plane3.pos = (x3, y3 + 5)
            

            if(x4 < dp(400)):
                self.plane4.pos = (x4 + 5, y4)

            #removing plane if it is out of bound of  radar
            if(x1 > (self.width * 2/3) - dp(20) or x1 < 0 or y1 > self.height or y1 < 0):
                self.planeInfo.remove_widget(self.label1)
                self.remove_widget(self.plane1)
                

            if(x2 > (self.width * 2/3) - dp(20) or x2 < 0 or y2 > self.height or y2 < 0):
                self.planeInfo.remove_widget(self.label2)
                self.remove_widget(self.plane2)

            if(x3 > (self.width * 2/3) - dp(20) or x3 < 0 or y1 > self.height or y3 < 0):
                self.planeInfo.remove_widget(self.label3)
                self.remove_widget(self.plane3)

            if(x4 > (self.width * 2/3) - dp(10) or y4 > self.height or y4 < 0):
                self.planeInfo.remove_widget(self.label4)
                self.remove_widget(self.plane4)

#class for plane
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
                valid = True

        #if it is, set textSubmit to success and change to the main menu
        if valid:
            self.textSubmit = "Success"
            self.manager.current = "menuScreen"
        #else display incorrect username or password message
        else:
            self.textSubmit = "Incorrect username or password."


class MainMenuWindow(Screen):
    def changeToRadar(self):
        global startMoving
        startMoving = True
        self.manager.current = "radarScreen"
        self.manager.transition = SlideTransition(direction='right', duration=.25)


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
