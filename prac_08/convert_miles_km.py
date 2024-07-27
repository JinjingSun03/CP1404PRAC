from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

Builder.load_string("""
BoxLayout:
    orientation: 'vertical'
    spacing: 10
    padding: 10

    TextInput:
        id: input_miles
        hint_text: "Enter miles"
        font_size: 18

    BoxLayout:
        orientation: 'horizontal'
        spacing: 10

        Button:
            text: 'Up'
            on_press: app.handle_increment(1)

        Button:
            text: 'Down'
            on_press: app.handle_increment(-1)

        Button:
            text: 'Convert'
            on_press: app.handle_calculate()

    Label:
        text: app.output_text
        font_size: 24
        color: (1, 1, 0, 1)
""")


class MilesConverterApp(App):
    output_text = StringProperty("0.0")

    def build(self):
        self.title = "Convert Miles to Kilometres"
        return Builder.load_file('convert_m_km_solution.kv')

    def handle_calculate(self):
        value = self.get_validated_miles()
        result = value * self.MILES_TO_KM
        self.output_text = str(result)

    def handle_increment(self, change):
        value = self.get_validated_miles() + change
        self.root.ids.input_miles.text = str(value)
        self.handle_calculate()

    def get_validated_miles(self):
        try:
            value = float(self.root.ids.input_miles.text) if self.root.ids.input_miles.text else 0
            return value
        except ValueError:
            return 0

    MILES_TO_KM = 1.60934


MilesConverterApp().run()
