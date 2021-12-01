#This code only have comments on the Login page as that is what I have wrote
#Other comments about the code can be found on someone elses branch
#When trying to login use "Admin1" for username and "Test1234" for the password
#My verson only 3 buttons work on the main menu Schedule, Plane Info, and Logout
#again, other comment about how they work can be found on a different branch (check Noah's branch)
#he should also have implement more buttons
from logging import NullHandler
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
    filler = ObjectProperty(None)
    separator = ObjectProperty(None)

    #use to move the plane in order
    plane1On = True
    plane2On = False
    plane3On = False
    plane4On = False
    
    #use to pop up plane info when arrive
    infoOn = True
    infoOn2 = True
    newLabel = Label
    newFiller = Widget
    newSeparator = Label

    #use to update status text
    statusText1 = "Good"
    statusText2 = "Good"
    statusText3 = "Good"
    statusText4 = "Good"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        #update screen every .1 seconds
        Clock.schedule_interval(self.update, .25)
        
    #the method for the animation
    def update(self, dt):

        #disable label until plane is in sight
        if(self.infoOn2):
            self.infoOn2 = False
            self.newLabel = self.label4
            self.newSeparator = self.separator
            self.planeInfo.remove_widget(self.label4)
            self.planeInfo.remove_widget(self.separator)

        #calculating height and width range
        h1 = self.height - dp(20)
        w1 = self.width * 2/3 - dp(20)

        #get current plan posistion
        x1, y1 = self.plane1.pos
 
        x2, y2 = self.plane2.pos
        
        x3, y3 = self.plane3.pos
   
        x4, y4 = self.plane4.pos
        
        #displaying plane infor
        self.label1.text = "ID               : 000001\nPosition     : " + str(int(x1)) + ", " + str(int(y1)) + " \nAirline        : American Airlines\nStatus        : " + self.statusText1 
        self.label2.text = "ID               : 000002\nPosition     : " + str(int(x2)) + ", " + str(int(y2)) + " \nAirline        : Delta Airlines\nStatus        : " + self.statusText2
        self.label3.text = "ID               : 000003\nPosition     : " + str(int(x3)) + ", " + str(int(y3)) + " \nAirline        : United Airlines\nStatus        : " + self.statusText3
        self.label4.text = "ID               : 000004\nPosition     : " + str(int(x4)) + ", " + str(int(y4)) + " \nAirline        : American Airlines\nStatus        : " + self.statusText4

        #pause movement until the radar screen is shown
        if(startMoving):
            #updating plan position
            #this is for demonstation purposes
            #if we had access to actual plane movement this is where it will go
            #changing status depending on condition
            if(self.plane1On):
                self.statusText1 = "Good, Departing"
                self.plane1.pos = (x1 + dp(5), y1 + dp(5))

            if(self.plane2On):
                self.statusText2 = "Good, Departing"
                self.plane2.pos = (x2 - dp(5), y2 + dp(3))
            
            if(self.plane3On):
                self.statusText3 = "Good, Departing"
                self.plane3.pos = (x3, y3 + dp(5))

            if(self.plane4On):
                if(x4 < dp(400)):
                    self.statusText4 = "Good, Landing"
                    self.plane4.pos = (x4 + dp(5), y4)
                
            if(x4 >= 400):
                    self.statusText4 = "Good, Landed"
                    self.label4.text = "ID               : 000004\nPosition     : " + str(int(x4)) + ", " + str(int(y4)) + " \nAirline        : American Airlines\nStatus        : " + self.statusText4
                    

            #only add widget once
            if(x4 + dp(20) > 0 and self.infoOn):
                    self.infoOn = False
                    self.newFiller = self.filler
                    self.planeInfo.remove_widget(self.filler)
                    self.planeInfo.add_widget(self.newLabel)
                    self.planeInfo.add_widget(self.newSeparator)
                    self.planeInfo.add_widget(self.newFiller)

            #removing plane if it is out of bound of  radar
            if(x1 > w1 or x1 < 0 or y1 > h1 or y1 < 0):
                self.plane1On = False
                self.planeInfo.remove_widget(self.label1)
                self.remove_widget(self.plane1)
                self.plane2On = True

            if(x2 > w1 or x2 < 0 or y2 > h1 or y2 < 0):
                self.plane2On = False
                self.planeInfo.remove_widget(self.label2)
                self.remove_widget(self.plane2)
                self.plane3On = True
                self.plane4On = True

            if(x3 > w1 or x3 < 0 or y3 > h1 or y3 < 0):
                self.plane3On = False
                self.planeInfo.remove_widget(self.label3)
                self.remove_widget(self.plane3)

            if(x4 > w1 or y4 > h1 or y4 < 0):
                self.plane4On = False
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
            self.manager.current = "menuScreen"
            self.textSubmit = ""
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
    def populate(self):
            {'datetime': datetimes[x],
             'code': codes[x],
             'note': notes[x]}
            for x in range(3)]

#  dP""b8 88""Yb  dP"Yb  88   88 88b 88 8888b.       dP""b8 88""Yb 888888 Yb        dP     .dP"Y8 88 8b    d8 
# dP   `" 88__dP dP   Yb 88   88 88Yb88  8I  Yb     dP   `" 88__dP 88__    Yb  db  dP      `Ybo." 88 88b  d88 
# Yb  "88 88"Yb  Yb   dP Y8   8P 88 Y88  8I  dY     Yb      88"Yb  88""     YbdPYbdP       o.`Y8b 88 88YbdP88 
#  YboodP 88  Yb  YbodP  `YbodP' 88  Y8 8888Y"       YboodP 88  Yb 888888    YP  YP        8bodP' 88 88 YY 88 

class EngineeringCheckPopup(Popup):
    pass

class ExtendGatePopup(Popup):
    pass


class GroundCrewSimulationWindow (Screen):
    def engineeringCheck(self):
        h = self.ids.GroundCrewSimFloatLayout.height
        w = self.ids.GroundCrewSimFloatLayout.width

        anim1 = Animation(x=w*.68, y=h*.68, duration=1)
        anim1.start(self.ids.worker1)

        anim2 = Animation(x=w*.54, y=h*.33, duration=1)
        anim2.start(self.ids.worker2)

        anim3 = Animation(x=w*.65, y=h*.9, duration=1)
        anim3.start(self.ids.worker3)

        anim4 = Animation(x=w*.56, y=h*.54, duration=1)
        anim4.start(self.ids.worker4)

        anim5 = Animation(x=w*.73, y=h*.29, duration=1)
        anim5.start(self.ids.worker5)

        threading.Timer(3, self.createEngineeringCheckPopup).start()

    def createEngineeringCheckPopup(self):
        eCheckPopup = EngineeringCheckPopup(pos= (self.center_x - 150, self.center_y-100))
        eCheckPopup.open()

    def extendGate(self):
        h = self.ids.GroundCrewSimFloatLayout.height
        w = self.ids.GroundCrewSimFloatLayout.width

        # Move Workers
        anim1 = Animation(x=w*.02, y=h*.1, duration=1)
        anim1.start(self.ids.worker1)

        anim2 = Animation(x=w*.02, y=h*.15, duration=1)
        anim2.start(self.ids.worker2)

        anim3 = Animation(x=w*.02, y=h*.2, duration=1)
        anim3.start(self.ids.worker3)

        anim4 = Animation(x=w*.02, y=h*.25, duration=1)
        anim4.start(self.ids.worker4)

        anim5 = Animation(x=w*.02, y=h*.30, duration=1)
        anim5.start(self.ids.worker5)


        # Extend gate
        gateAnim = Animation(size_hint=(.03, .27), duration=3)
        gateAnim.start(self.ids.gate)

        threading.Timer(3, self.createExtendGatePopup).start()

    def createExtendGatePopup(self):
        gPopup = ExtendGatePopup(pos= (self.center_x - 150, self.center_y-100))
        gPopup.open()
        
    




#  dP""b8  dP"Yb  8b    d8 8b    d8 88   88 88b 88 88  dP""b8    db    888888 88  dP"Yb  88b 88 .dP"Y8 
# dP   `" dP   Yb 88b  d88 88b  d88 88   88 88Yb88 88 dP   `"   dPYb     88   88 dP   Yb 88Yb88 `Ybo." 
# Yb      Yb   dP 88YbdP88 88YbdP88 Y8   8P 88 Y88 88 Yb       dP__Yb    88   88 Yb   dP 88 Y88 o.`Y8b 
#  YboodP  YbodP  88 YY 88 88 YY 88 `YbodP' 88  Y8 88  YboodP dP""""Yb   88   88  YbodP  88  Y8 8bodP' 


class CommunicationsWindow (Screen):
    pass

class ChannelRow(GridLayout):
    channel_text = StringProperty()
    def __init__(self, **kwargs):
        super(ChannelRow, self).__init__(**kwargs)



# Class for controller for simulated workers
class SimulatedWorkerAnimationController():
    pass

# Class for alert creator
class AlertCreator():
    pass

    # Create alert
