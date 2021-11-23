# Screens.py
# Description:
#   Contains the definitions for classes for the associated widgets in every screen
#   This file will be split into files for each screen in the future

# This code only have comments on the Login page as that is what I have wrote
# Other comments about the code can be found on someone elses branch
# When trying to login use "Admin1" for username and "Test1234" for the password
# My verson only 3 buttons work on the main menu Schedule, Plane Info, and Logout
# again, other comment about how they work can be found on a different branch (check Noah's branch)
# he should also have implement more buttons

from kivy.metrics import dp
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.properties import NumericProperty, ObjectProperty
from kivy.properties import StringProperty
from kivy.animation import Animation
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.config import Config
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
import time
import threading
from kivy.uix import *
from datetime import datetime, timedelta
import math
import MasterLogAccess
# TODO: Remove these two imports once PlaneInfoList.populate is implemented
from random import sample, randint
from string import ascii_lowercase


# Set window size
Window.size = (1280, 720)
Window.minimum_width, Window.minimum_height = Window.size

# 888888 888888 8b    d8 88""Yb 88        db    888888 888888 .dP"Y8 
#   88   88__   88b  d88 88__dP 88       dPYb     88   88__   `Ybo." 
#   88   88""   88YbdP88 88"""  88  .o  dP__Yb    88   88""   o.`Y8b 
#   88   888888 88 YY 88 88     88ood8 dP""""Yb   88   888888 8bodP' 

class TitleLabel(Label):
    pass

class TopBarLayout(GridLayout):
    title_text = StringProperty()
    def __init__(self, **kwargs):
        super(TopBarLayout, self).__init__(**kwargs)

# this variable is so that animation does not start until a certain screen in
startMoving = False

# Class for WindowManager controller - needed to change screens
class WindowManager(ScreenManager):
    login = ObjectProperty(None)
    mainMenu = ObjectProperty(None)
    radar = ObjectProperty(None)

#this is the code for the radar page
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

# 88      dP"Yb   dP""b8 88 88b 88 
# 88     dP   Yb dP   `" 88 88Yb88 
# 88  .o Yb   dP Yb  "88 88 88 Y88 
# 88ood8  YbodP   YboodP 88 88  Y8 

# Class for LoginWindow root widget
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

# 8b    d8    db    88 88b 88     8b    d8 888888 88b 88 88   88 
# 88b  d88   dPYb   88 88Yb88     88b  d88 88__   88Yb88 88   88 
# 88YbdP88  dP__Yb  88 88 Y88     88YbdP88 88""   88 Y88 Y8   8P 
# 88 YY 88 dP""""Yb 88 88  Y8     88 YY 88 888888 88  Y8 `YbodP' 

# Class for MainMenuWindow root widget
class MainMenuWindow(Screen):
    def changeToRadar(self):
        global startMoving
        startMoving = True
        self.manager.current = "radarScreen"
        self.manager.transition = SlideTransition(direction='right', duration=.25)

# 88""Yb 88        db    88b 88 888888     88 88b 88 888888  dP"Yb      Yb        dP 88 88b 88 8888b.   dP"Yb  Yb        dP 
# 88__dP 88       dPYb   88Yb88 88__       88 88Yb88 88__   dP   Yb      Yb  db  dP  88 88Yb88  8I  Yb dP   Yb  Yb  db  dP  
# 88"""  88  .o  dP__Yb  88 Y88 88""       88 88 Y88 88""   Yb   dP       YbdPYbdP   88 88 Y88  8I  dY Yb   dP   YbdPYbdP   
# 88     88ood8 dP""""Yb 88  Y8 888888     88 88  Y8 88      YbodP         YP  YP    88 88  Y8 8888Y"   YbodP     YP  YP    

# Class for PlaneInfoWindow root widget
class PlaneInfoWindow(Screen):
    def search(self):
        # Getting the text values from text inputs
        searchKey = self.ids.PlaneInfoTextInput.text

        # make a new dataset based on search terms
        newData = []
        for x in getattr(self.ids.PlaneInfoList, 'data'):
            # Ensure that row matches search criteria
            if searchKey == "" or (searchKey.lower() in str(x[0]).lower()):
                newData.append({'dataName': str(x[0]),
                                'dataValue': str(x[1])})
        self.ids.PlaneInfoList.rv.data = newData

# Class for a row in the table of plane information in PlaneInfo Screen
class PlaneInfoRow(RecycleDataViewBehavior,BoxLayout):
    dataName = StringProperty()
    dataValue = StringProperty()
    def __init__(self, **kwargs):
        super(PlaneInfoRow, self).__init__(**kwargs)

# Class for the list of plane information in PlaneInfo Screen
#   Autopopulates on the first clock
class PlaneInfoList(BoxLayout):
    def __init__(self, **kwargs):
        global Log_access
        global data
        Log_access = MasterLogAccess.MasterLogAccess()
        super(PlaneInfoList, self).__init__(**kwargs)
        Clock.schedule_once(self.finish_init,0)

    # Autopopulate list of plane info
    def finish_init(self, dt):
        self.populate()

    # Populate list of plane info from database
    def populate(self):
        # query_result = Log_access.temporary_Info_List_Search()
        # Temporary data
        query_result = [
            ['Plane ID', '1'],
            ['Gas Usage', str(randint(90, 110)/100) + " gal/s"],
            ['Altitude', str(randint(39950, 40050)) + " mi"],
            ['Expected Altitude', '40000 mi'],
            ['Weight', '91,678 lbs'],
            ['Runway', 'Runway 1'],
            ['Docking Gate', 'Gate 1'],
            ['Expected rate of descent', '2000 ft/min']
        ]
        self.data = query_result
        self.rv.data = [{'dataName': str(x[0]),
        'dataValue': str(x[1])} for x in query_result]


    def makeOverweight(self):
        # Temporary data
        query_result = [
            ['Plane ID', '1'],
            ['Gas Usage', "1 gal/s"],
            ['Altitude',  "0 mi"],
            ['Expected Altitude', '0 mi'],
            ['Weight', "95,678 lbs"],
            ['Runway', 'Runway 1'],
            ['Docking Gate', 'Gate 1'],
            ['Expected rate of descent', '2000 ft/min']
        ]
        self.data = query_result
        self.rv.data = [{'dataName': str(x[0]),
        'dataValue': str(x[1])} for x in query_result]

# .dP"Y8  dP""b8 88  88 888888 8888b.  88   88 88     888888 
# `Ybo." dP   `" 88  88 88__    8I  Yb 88   88 88     88__   
# o.`Y8b Yb      888888 88""    8I  dY Y8   8P 88  .o 88""   
# 8bodP'  YboodP 88  88 888888 8888Y"  `YbodP' 88ood8 888888 


# Class for ScheduleWindow root widget
class ScheduleWindow(Screen):
    pass

# Class for a row of ArrivalList, the list of arriving planes
class ArrivalRow(RecycleDataViewBehavior,BoxLayout):
    planeName = StringProperty()
    planeArrivalTime = StringProperty()
    def __init__(self, **kwargs):
        super(ArrivalRow, self).__init__(**kwargs)

# Class for a row of DepartureList, the list of departing planes
class DepartureRow(RecycleDataViewBehavior,BoxLayout):
    planeName = StringProperty()
    planeDepartureTime = StringProperty()
    def __init__(self, **kwargs):
        super(DepartureRow, self).__init__(**kwargs)

#https://github.com/kivy/kivy/issues/6582
# Class for the list or arriving planes
class ArrivalList(BoxLayout):
    def __init__(self, **kwargs):
        super(ArrivalList, self).__init__(**kwargs)
        Clock.schedule_once(self.finish_init,0)

    # Autopopulate list of arrivals
    def finish_init(self, dt):
        self.populate()

    # TODO:  Write query for populating list of arrivals
    # Populate list of arrivals
    def populate(self):
        arrivalPlaneNames = ['Plane A', 'Plane B', 'Plane C']
        dateTimeNow = datetime.now()
        dateTimeA = dateTimeNow.strftime('%a, %b %d, %y  -  %m-%d-%y  -  %H:%M')
        dateTimeNow = datetime.now() + timedelta(hours=3, minutes = 27)
        dateTimeB = dateTimeNow.strftime('%a, %b %d, %y  -  %m-%d-%y  -  %H:%M')
        dateTimeNow = datetime.now() + timedelta(hours=2, minutes = 12)
        dateTimeC = dateTimeNow.strftime('%a, %b %d, %y  -  %m-%d-%y  -  %H:%M')
        arrivalPlaneDatetimes = [dateTimeA, dateTimeB, dateTimeC]

        self.rv.data = [
            {'planeName': arrivalPlaneNames[x],
             'planeArrivalTime': arrivalPlaneDatetimes[x]}
            for x in range(3)]

# Class for the list of departing planes
class DepartureList(BoxLayout):
    def __init__(self, **kwargs):
        super(DepartureList, self).__init__(**kwargs)
        Clock.schedule_once(self.finish_init,0)

    # Autopopulate list of departures
    def finish_init(self, dt):
        self.populate()

    # TODO: Write query for populating list of departures
    # Populate list of departures
    def populate(self):
        departurePlaneNames = ['Plane A', 'Plane B', 'Plane C']
        dateTimeNow = datetime.now() + timedelta(hours=3, minutes = 27)
        dateTimeA = dateTimeNow.strftime('%a, %b %d, %y  -  %m-%d-%y  -  %H:%M')
        dateTimeNow = datetime.now() + timedelta(hours=5, minutes = 27)
        dateTimeB = dateTimeNow.strftime('%a, %b %d, %y  -  %m-%d-%y  -  %H:%M')
        dateTimeNow = datetime.now() + timedelta(hours=7, minutes = 12)
        dateTimeC = dateTimeNow.strftime('%a, %b %d, %y  -  %m-%d-%y  -  %H:%M')
        departurePlaneDateteimes = [dateTimeA, dateTimeB, dateTimeC]

        self.rv.data = [
            {'planeName': departurePlaneNames[x],
             'planeDepartureTime': departurePlaneDateteimes[x]}
            for x in range(3)]

# 888888 888888 88""Yb 8b    d8 88 88b 88    db    88         .dP"Y8 88 8b    d8 
#   88   88__   88__dP 88b  d88 88 88Yb88   dPYb   88         `Ybo." 88 88b  d88 
#   88   88""   88"Yb  88YbdP88 88 88 Y88  dP__Yb  88  .o     o.`Y8b 88 88YbdP88 
#   88   888888 88  Yb 88 YY 88 88 88  Y8 dP""""Yb 88ood8     8bodP' 88 88 YY 88 

# Class representing a worker in the simulation of the ground crew simulation
class TerminalSimulatedPlane(Widget):
    def __init__(self, **kwargs):
        super(TerminalSimulatedPlane, self).__init__(**kwargs)

# Class for the TerminalSimulationWindow root widget
class TerminalSimulationWindow(Screen):
    planes = []
    def __init__(self, **kwargs):
        super(TerminalSimulationWindow, self).__init__(**kwargs)
        self.planes = []
        self.initializePlanes()

    # Initialize simulated plane objects
    #   Planes are initialized in an array because adding and referencing them by ids is not possible to do dynamically
    #   Plane number and initial positions are determined by a query (not yet implemented)
    def initializePlanes(self):
        # Figure out the number of planes in the simulation
        # TODO: make a query to determine number of planes
        for x in range(0, 1):
            newPlane = TerminalSimulatedPlane()
            # TODO: Make a query to determine the initial position of each plane
            newPlane.pos = (randint(200,200), randint(200,200))
            self.planes.append(newPlane)
            self.add_widget(self.planes[len(self.planes)-1])

    # Animate the given widget. First rotate to face 
    #   wIndex - String - The index of the widget to animate          
    #   destX - Num - The x position to animate to
    #   destY - Num - The y position to animate to
    #   angleOffset - Num - The offset of the calcuated angle to animate to. 
    #       Default if 0 offset. 
    #       angleOffset should be 45 for GoogleAirplane.png
    def planeAnimate(self, wIndex, destX, destY, angleOffset=0, **kwargs):

        # Check that not already at destination
        if (destX  - self.planes[wIndex].pos[0]) == 0 and (destY - self.planes[wIndex].pos[1]) == 0:
            return

        # Calculate angleOffset
        if (destY - self.planes[wIndex].pos[1]) < 1:
            angleOffset -= 180
        atan = math.atan((destX  - self.planes[wIndex].pos[0]) / (destY - self.planes[wIndex].pos[1]))
        deg = atan * 180 / math.pi
        deg = deg * -1
        addedOffset = deg + angleOffset
        angle = addedOffset

        # Create and start animation
        anim = Animation(animAngle=angle, duration=.2) + Animation(x= destX, y = destY, duration=1)
        anim.start(self.planes[wIndex])

# 8b    d8    db    .dP"Y8 888888 888888 88""Yb     88      dP"Yb   dP""b8 
# 88b  d88   dPYb   `Ybo."   88   88__   88__dP     88     dP   Yb dP   `" 
# 88YbdP88  dP__Yb  o.`Y8b   88   88""   88"Yb      88  .o Yb   dP Yb  "88 
# 88 YY 88 dP""""Yb 8bodP'   88   888888 88  Yb     88ood8  YbodP   YboodP 

class MasterLogWindow(Screen):
    pass

# Class for a row of DepartureList, the list of departing planes
class MasterLogRow(RecycleDataViewBehavior,BoxLayout):
    datetime = StringProperty()
    note = StringProperty()
    def __init__(self, **kwargs):
        super(MasterLogRow, self).__init__(**kwargs)

class MasterLogList(BoxLayout):
    def __init__(self, **kwargs):
        super(MasterLogList, self).__init__(**kwargs)
        Clock.schedule_once(self.finish_init,0)

    # Autopopulate list of departures
    def finish_init(self, dt):
        self.populate()

    # Populate list of departures
    def populate(self):
        dateTimeNow = datetime.now() - timedelta(hours=3, minutes = 27)
        dateTimeA = dateTimeNow.strftime('%a, %b %d, %y  -  %m-%d-%y  -  %H:%M')
        dateTimeNow = datetime.now() - timedelta(hours=5, minutes = 27)
        dateTimeB = dateTimeNow.strftime('%a, %b %d, %y  -  %m-%d-%y  -  %H:%M')
        dateTimeNow = datetime.now() - timedelta(hours=7, minutes = 12)
        dateTimeC = dateTimeNow.strftime('%a, %b %d, %y  -  %m-%d-%y  -  %H:%M')
        datetimes = [dateTimeA, dateTimeB, dateTimeC]
        notes = ["Plane 1 landed sucessfully", "Ground crew went on lunch", "Weather check successful"]

        self.rv.data = [
            {'datetime': datetimes[x],
             'note': notes[x]}
            for x in range(3)]

# 88 88b 88  dP""b8 88 8888b.  888888 88b 88 888888     88      dP"Yb   dP""b8 
# 88 88Yb88 dP   `" 88  8I  Yb 88__   88Yb88   88       88     dP   Yb dP   `" 
# 88 88 Y88 Yb      88  8I  dY 88""   88 Y88   88       88  .o Yb   dP Yb  "88 
# 88 88  Y8  YboodP 88 8888Y"  888888 88  Y8   88       88ood8  YbodP   YboodP 

class IncidentLogWindow(Screen):
    pass

# Class for a row of DepartureList, the list of departing planes
class IncidentLogRow(RecycleDataViewBehavior,BoxLayout):
    datetime = StringProperty()
    code = StringProperty()
    note = StringProperty()
    def __init__(self, **kwargs):
        super(IncidentLogRow, self).__init__(**kwargs)

class IncidentLogList(BoxLayout):
    def __init__(self, **kwargs):
        super(IncidentLogList, self).__init__(**kwargs)
        Clock.schedule_once(self.finish_init,0)

    # Autopopulate list of departures
    def finish_init(self, dt):
        self.populate()

    # Populate list of departures
    def populate(self):
        dateTimeNow = datetime.now() - timedelta(hours=100, minutes = 27)
        dateTimeA = dateTimeNow.strftime('%a, %b %d, %y  -  %m-%d-%y  -  %H:%M')
        dateTimeNow = datetime.now() - timedelta(hours=250, minutes = 27)
        dateTimeB = dateTimeNow.strftime('%a, %b %d, %y  -  %m-%d-%y  -  %H:%M')
        dateTimeNow = datetime.now() - timedelta(hours=300, minutes = 12)
        dateTimeC = dateTimeNow.strftime('%a, %b %d, %y  -  %m-%d-%y  -  %H:%M')
        datetimes = [dateTimeA, dateTimeB, dateTimeC]
        codes = ['C', 'U', 'E']
        notes = ['Collision between planes 1 and 2 on the runway', 'Unidentified plane found', 'Plane 1 emergency landing on runway 1']

        self.rv.data = [
            {'datetime': datetimes[x],
             'code': codes[x],
             'note': notes[x]}
            for x in range(3)]

#  dP""b8 88""Yb  dP"Yb  88   88 88b 88 8888b.       dP""b8 88""Yb 888888 Yb        dP     .dP"Y8 88 8b    d8 
# dP   `" 88__dP dP   Yb 88   88 88Yb88  8I  Yb     dP   `" 88__dP 88__    Yb  db  dP      `Ybo." 88 88b  d88 
# Yb  "88 88"Yb  Yb   dP Y8   8P 88 Y88  8I  dY     Yb      88"Yb  88""     YbdPYbdP       o.`Y8b 88 88YbdP88 
#  YboodP 88  Yb  YbodP  `YbodP' 88  Y8 8888Y"       YboodP 88  Yb 888888    YP  YP        8bodP' 88 88 YY 88 

class GroundCrewSimulationWindow (Screen):
    pass


#  dP""b8  dP"Yb  8b    d8 8b    d8 88   88 88b 88 88  dP""b8    db    888888 88  dP"Yb  88b 88 .dP"Y8 
# dP   `" dP   Yb 88b  d88 88b  d88 88   88 88Yb88 88 dP   `"   dPYb     88   88 dP   Yb 88Yb88 `Ybo." 
# Yb      Yb   dP 88YbdP88 88YbdP88 Y8   8P 88 Y88 88 Yb       dP__Yb    88   88 Yb   dP 88 Y88 o.`Y8b 
#  YboodP  YbodP  88 YY 88 88 YY 88 `YbodP' 88  Y8 88  YboodP dP""""Yb   88   88  YbodP  88  Y8 8bodP' 


class CommunicationsWindow (Screen):
    pass





# Class for controller for simulated workers
class SimulatedWorkerAnimationController():
    pass

# Class for alert creator
class AlertCreator():
    pass

    # Create alert
