from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget



class grolApp(GridLayout):
    def __init__(self,**kwargs):
        super(grolApp,self).__init__(**kwargs)
        self.top_grid = GridLayout()
        self.cols=2


        self.sub_button = Button(text="Принять",

                                 font_size=30,
                                 size_hint_y= None,
                                 height=60,
                                 width=90)
        self.add_widget(self.sub_button)

        self.sub_button.bind(on_press=self.sub)


    def sub(self,):
        pass




class myApp(App):
    def build(self):
        return grolApp()



if __name__ == '__main__':
    myApp().run()
