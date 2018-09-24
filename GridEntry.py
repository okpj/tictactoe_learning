from kivy.properties import ListProperty
from kivy.uix.button import Button


class GridEntry(Button):
    coords = ListProperty([1, 1])

