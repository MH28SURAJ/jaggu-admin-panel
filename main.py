from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window
import requests

# APP BACKGROUND COLOR
Window.clearcolor = (0.05, 0.05, 0.08, 1)

# FIREBASE URL
FIREBASE_URL = "https://automation-v6-default-rtdb.asia-southeast1.firebasedatabase.app/keys"

class AdminPanel(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', spacing=15, padding=20, **kwargs)

        # HEADER
        self.header = Label(
            text='DEVELOPER JAGGU ADMIN PANEL',
            font_size=24,
            bold=True,
            color=(0, 1, 1, 1),
            size_hint=(1, 0.2)
        )

        self.add_widget(self.header)

        # KEY INPUT
        self.key_input = TextInput(
            hint_text='ENTER KEY',
            multiline=False,
            background_color=(0.1, 0.1, 0.15, 1),
            foreground_color=(1, 1, 1, 1)
        )

        self.add_widget(self.key_input)

        # EXPIRY INPUT
        self.expiry_input = TextInput(
            hint_text='ENTER EXPIRY',
            multiline=False,
            background_color=(0.1, 0.1, 0.15, 1),
            foreground_color=(1, 1, 1, 1)
        )

        self.add_widget(self.expiry_input)

        # HWID INPUT
        self.hwid_input = TextInput(
            hint_text='ENTER HWID',
            multiline=False,
            background_color=(0.1, 0.1, 0.15, 1),
            foreground_color=(1, 1, 1, 1)
        )

        self.add_widget(self.hwid_input)

        # BUTTON
        self.upload_btn = Button(
            text='UPLOAD TO FIREBASE',
            size_hint=(1, 0.25),
            background_color=(0, 0.8, 1, 1),
            bold=True
        )

        self.upload_btn.bind(on_press=self.upload_key)

        self.add_widget(self.upload_btn)

        # RESULT LABEL
        self.result = Label(
            text='',
            color=(0, 1, 0, 1),
            font_size=18
        )

        self.add_widget(self.result)

    def upload_key(self, instance):

        key_name = self.key_input.text
        expiry = self.expiry_input.text
        hwid = self.hwid_input.text

        data = {
            key_name: {
                "expiry": expiry,
                "hwid": hwid
            }
        }

        try:
            requests.patch(
                f"{FIREBASE_URL}.json",
                json=data
            )

            self.result.text = 'UPLOADED SUCCESSFULLY'

        except Exception as e:
            self.result.text = str(e)

class JagguAdminApp(App):
    def build(self):
        return AdminPanel()

JagguAdminApp().run()