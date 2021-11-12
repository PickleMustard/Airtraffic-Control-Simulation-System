# Screens.py
# Description:
#   Contains the definitions for classes for the associated widgets in every screen
#   This file will be split into files for each screen in the future

from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.label import Label
from kivy.properties import NumericProperty
from kivy.properties import StringProperty
from kivy.animation import Animation
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout

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
        super(PlaneInfoList, self).__init__(**kwargs)
        Clock.schedule_once(self.finish_init,0)

    # Autopopulate list of plane info
    def finish_init(self, dt):
        self.populate()

    # TODO: Write query for populating list of plane info
    # Populate list of plane info from database
    def populate(self):
        print("Populating")
        self.rv.data = [
            {'dataName': ''.join(sample(ascii_lowercase, 6)),
             'dataValue': str(randint(0, 2000))}
            for x in range(50)]

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
class SimulatedWorker(Widget):
    def __init__(self, **kwargs):
        super(SimulatedWorker, self).__init__(**kwargs)

# Class for the TerminalSimulationWindow root widget
class TerminalSimulationWindow(Screen):

    def animationTestt(self, widget, **kwargs):
        anim = Animation(x=0, y=0)
        anim.start(self.ids.otherExample)
        print (self.ids.otherExample.height)
        print (self.ids.otherExample.width)
        print(str(self.height) + " " + str(self.width))


    def animationTest(self, widget, **kwargs):
        anim = Animation(x=1200, y=980, duration=1)
        anim.start(widget)

# Class for alert creator
class AlertCreator():
    pass

    # Create alert