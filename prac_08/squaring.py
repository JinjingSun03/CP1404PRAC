from kivy.properties import StringProperty

class SquareNumberApp(App):
    output_text = StringProperty("0.0")

    def build(self):
        Window.size = (200, 150)
        self.title = "Miles to Kilometres Converter"
        self.root = Builder.load_file('squaring.kv')
        return self.root

    def handle_input(self, text):
        try:
            miles = float(text)
        except ValueError:
            miles = 0.0
        self.calculate_and_update_output(miles)

    def handle_increment(self, value):
        try:
            miles = float(self.root.ids.miles_input.text)
        except ValueError:
            miles = 0.0
        miles += value
        self.calculate_and_update_output(miles)

    def calculate_and_update_output(self, miles):
        conversion_factor = 1.60934
        kilometers = miles * conversion_factor
        self.output_text = f"{kilometers:.2f}"




"""
BoxLayout:
    orientation: 'horizontal'
    TextInput:
        id: input_number
        text: '7'
        font_size: 48
        multiline: False

    Button:
        text: 'Square'
        on_press: app.handle_calculate(input_number.text)

    Label:
        id: output_label
        font_size: 48
        color: (1, 0, 1, 1)
BoxLayout:
    orientation: 'vertical'

    BoxLayout:
        orientation: 'horizontal'

        Label:
            text: 'Enter a number and press "Square"'

    Label:
        text: 'Bottom Label'
"""