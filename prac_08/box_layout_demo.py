from kivy.app import App
from kivy.lang import Builder

class BoxLayoutDemo(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        print("Greet")
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def handle_clear(self):
        print("Clear")
        self.root.ids.input_name.text = ''
        self.root.ids.output_label.text = 'Enter your name'

BoxLayoutDemo().run()


"""
# box_layout.kv
BoxLayout:
    orientation: 'vertical'

    Button:
        text: 'Clear'
        on_press: app.handle_clear()

    TextInput:
        id: input_name
        text: ''

    Button:
        text: 'Greet'
        on_press: app.handle_greet()

    Label:
        text: 'Enter your name'
        color: 1, 1, 0, 1
        id: output_label
"""