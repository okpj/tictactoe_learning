from kivy.app import App
from kivy.lang import Builder

from TicTacToeGrid import TicTacToeGrid


Builder.load_file("App.kv")

class TicTacToeApp(App):
    def build(self):
        return TicTacToeGrid()


if __name__ == "__main__":
    TicTacToeApp().run()
