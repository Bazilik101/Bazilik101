import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class grolApp(GridLayout):
    def __init__(self,**kwargs):
        super(grolApp,self).__init__(**kwargs)
        self.top_grid = GridLayout()
        self.cols=2

        self.top_grid.cols=2


        self.name=TextInput(multiline=True)
        self.add_widget(Label(text='русский:'))
        self.top_grid.name=TextInput(multiline=False)
        self.top_grid.add_widget(self.name)
        self.top_grid.add_widget(Label(text='морзе:'))
        self.top_grid.mami = TextInput(multiline=False)
        self.top_grid.add_widget(self.mami)

        self.submit.bind(on_press=self.submit)
        self.add_widget(self.submit)
        self.submin=Button



class App(App):
    def build(self):
        return grolApp()



if __name__ == '__main__':
    App().run()