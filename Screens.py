from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.label import Label
from kivy.properties import NumericProperty
from kivy.properties import StringProperty

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
            
    # Populate the list at the start - not functioning
#    def __post_init__(self, **kwargs):
#        super().__init__(**kwargs)
#        PlaneInfoList

class ScheduleWindow(Screen):
    pass
#https://github.com/kivy/kivy/issues/6582
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