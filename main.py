from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.clock import Clock
from plyer import flash
class FlashlightApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # Label for instructions
        instructions_label = Label(text="Enter your data and click 'Transmit Data' \n for data transmission ", font_size=40)
        self.layout.add_widget(instructions_label)

        # Create a TextInput widget for user input
        self.input_text = TextInput(hint_text="Enter your data", multiline=False, font_size=40)
        self.layout.add_widget(self.input_text)

        # Create a button for transmitting data
        self.transmit_button = Button(text="Transmit Data", font_size=40, on_press=self.transmit_data)
        self.layout.add_widget(self.transmit_button)

        return self.layout

    def transmit_data(self, instance):
        # Get data input from the user
        user_input = self.input_text.text.strip()

        if user_input:
            # Convert the input text to binary
            binary_data = self.convert_to_binary(user_input)

            # Transmit the binary data using the flashlight
            self.flashlight_transmission(binary_data)

    def convert_to_binary(self, data):
        # Convert text data to binary
        binary_data = ''.join(format(ord(char), '08b') for char in data)
        return binary_data

    def flashlight_transmission(self, data):
        # Toggle the flashlight based on binary data
        try:
            if flash.toggle() in flash:
                print(True)
            for bit in data:
                flash.toggle() if int(bit) else flash.turn_off()
                Clock.sleep(0.5)  # Adjust the timing as needed
        except Exception as e:
            print("Error toggling flashlight:", e)

if __name__ == '__main__':
    FlashlightApp().run()
