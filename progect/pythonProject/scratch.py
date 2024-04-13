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


        self.add_widget(Label(text='русский:'))

        self.name = TextInput(multiline=False)
        self.add_widget(self.name)

        self.add_widget(Label(text='морзе:'))

        self.mami = TextInput(multiline=False)
        self.add_widget(self.mami)

        self.sub_button = Button(text="Принять")
        self.add_widget(self.sub_button)

        self.sub_button.bind(on_press=self.sub)

    def sub(self):
        pass


class myApp(App):
    def build(self):
        return grolApp()



if __name__ == '__main__':
    myApp().run()