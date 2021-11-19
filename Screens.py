# Screens.py
# Description:
#   Contains the definitions for classes for the associated widgets in every screen
#   This file will be split into files for each screen in the future

from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.app import App
from kivy.lang import Builder
#from kivy.uix.image import Image
from kivy.uix.recycleview.views import RecycleDataViewBehavior
#from kivy.uix.label import Label
from kivy.properties import NumericProperty
from kivy.properties import StringProperty
from kivy.animation import Animation
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.uix import *
import math
import MasterLogAccess


# Set window size
Window.size = (1280, 720)
Window.minimum_width, Window.minimum_height = Window.size

# Class for WindowManager controller
class WindowManager(ScreenManager):
    pass

# Class for LoginWindow root widget
class LoginWindow(Screen):
    pass

# Class for MainMenuWindow root widget
class MainMenuWindow(Screen):
    pass

# TODO: Remove these two imports once PlaneInfoList.populate is implemented
from random import sample, randint
from string import ascii_lowercase

# Class for PlaneInfoWindow root widget
class PlaneInfoWindow(Screen):
    pass

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
        Log_access = MasterLogAccess.MasterLogAccess()
        super(PlaneInfoList, self).__init__(**kwargs)
        Clock.schedule_once(self.finish_init,0)

    # Autopopulate list of plane info
    def finish_init(self, dt):
        self.populate()

    # Populate list of plane info from database
    def populate(self):
        query_result = Log_access.temporary_Info_List_Search()
        self.rv.data = [{'dataName': str(x[0]), 'dataValue': x[1]} for x in query_result]

    # Sort the list plane info
    def sort(self):
        self.rv.data = sorted(self.rv.data, key=lambda x: x['name.text'])

    # Clear the list of plane info
    def clear(self):
        self.rv.data = []

    # Update list of plane info
    def update(self, value):
        if self.rv.data:
            self.rv.data[0]['name.text'] = value or 'default new value'
            self.rv.refresh_from_data()

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
        self.rv.data = [
            {'planeName': ''.join(sample(ascii_lowercase, 6)),
             'planeArrivalTime': str(randint(0, 2000))}
            for x in range(50)]

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
        self.rv.data = [
            {'planeName': ''.join(sample(ascii_lowercase, 6)),
             'planeDepartureTime': str(randint(0, 2000))}
            for x in range(50)]

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

    # Animate the given widget
    #   wIndex - String - The index of the widget to animate          
    #   destX - Num - The x position to animate to
    #   destY - Num - The y position to animate to
    #   angleOffset - Num - The offset of the calcuated angle to animate to. 
    #       Default if 0 offset. 
    #       angleOffset should be 45 for GoogleAirplane.png
    def animate(self, wIndex, destX, destY, angleOffset=0, **kwargs):

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
                



# Class for controller for simulated workers
class SimulatedWorkerAnimationController():
    pass

# Class for alert creator
class AlertCreator():
    pass

    # Create alert
