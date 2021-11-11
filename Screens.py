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

class WindowManager(ScreenManager):
    pass

class LoginWindow(Screen):
    def testFunction(self):
        print("TEST FUNCTION")

class MainMenuWindow(Screen):
    pass

# Remove these two imports once PlaneInfoList.populate is implemented
from random import sample, randint
from string import ascii_lowercase

class PlaneInfoWindow(Screen):
    pass

class PlaneInfoRow(RecycleDataViewBehavior,BoxLayout):
    dataName = StringProperty()
    dataValue = StringProperty()
    def __init__(self, **kwargs):
        super(PlaneInfoRow, self).__init__(**kwargs)

class PlaneInfoList(BoxLayout):
    def __init__(self, **kwargs):
        super(PlaneInfoList, self).__init__(**kwargs)
        Clock.schedule_once(self.finish_init,0)

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

class ScheduleWindow(Screen):
    pass

class ArrivalRow(RecycleDataViewBehavior,BoxLayout):
    planeName = StringProperty()
    planeArrivalTime = StringProperty()
    def __init__(self, **kwargs):
        super(ArrivalRow, self).__init__(**kwargs)

class DepartureRow(RecycleDataViewBehavior,BoxLayout):
    planeName = StringProperty()
    planeDepartureTime = StringProperty()
    def __init__(self, **kwargs):
        super(DepartureRow, self).__init__(**kwargs)

#https://github.com/kivy/kivy/issues/6582
class ArrivalList(BoxLayout):
    def __init__(self, **kwargs):
        super(ArrivalList, self).__init__(**kwargs)
        Clock.schedule_once(self.finish_init,0)

    def finish_init(self, dt):
        self.populate()

    # Dillon I need a query here for a plane's info!!!!---------------------------------------
    def populate(self):
        self.rv.data = [
            {'planeName': ''.join(sample(ascii_lowercase, 6)),
             'planeArrivalTime': str(randint(0, 2000))}
            for x in range(50)]

class DepartureList(BoxLayout):
    def __init__(self, **kwargs):
        super(DepartureList, self).__init__(**kwargs)
        Clock.schedule_once(self.finish_init,0)

    def finish_init(self, dt):
        self.populate()

    # Dillon I need a query here for a plane's info!!!!---------------------------------------
    def populate(self):
        self.rv.data = [
            {'planeName': ''.join(sample(ascii_lowercase, 6)),
             'planeDepartureTime': str(randint(0, 2000))}
            for x in range(50)]

class SimulatedWorker(Widget):
    def __init__(self, **kwargs):
        super(SimulatedWorker, self).__init__(**kwargs)

class Test(FloatLayout):
    pass

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
