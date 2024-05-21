import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
import re


class RegistrationScreen(Screen):
    def __init__(self, **kwargs):
        super(RegistrationScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=30, spacing=10)

        # Adding a Head Label with styling
        head_label = Label(text="User Registration App", font_size=26, bold=True, height=40)

        # Adding Labels and TextInputs with placeholders
        self.firstname_input = TextInput(hint_text="Enter your first name", multiline=False, font_size=18)
        self.lastname_input = TextInput(hint_text="Enter your last name", multiline=False, font_size=18)
        self.email_input = TextInput(hint_text="Enter your email", multiline=False, font_size=18)
        self.password_input = TextInput(hint_text="Enter your password", multiline=False, font_size=18, password=True)
        self.confirm_input = TextInput(hint_text="Confirm your password", multiline=False, font_size=18, password=True)

        # Button with styling
        submit_button = Button(text="Register", font_size=18, on_press=self.register,
                               background_color=(0.2, 0.6, 0.8, 1))

        # Adding widgets to the layout
        layout.add_widget(head_label)
        layout.add_widget(self.firstname_input)
        layout.add_widget(self.lastname_input)
        layout.add_widget(self.email_input)
        layout.add_widget(self.password_input)
        layout.add_widget(self.confirm_input)
        layout.add_widget(submit_button)

        # Adding the layout to the screen
        self.add_widget(layout)

    def register(self, instance):
        first_name = self.firstname_input.text
        last_name = self.lastname_input.text
        email = self.email_input.text
        password = self.password_input.text
        confirm_password = self.confirm_input.text

        if first_name.strip() == '' or last_name.strip() == '' or email.strip() == '' or password.strip() == '' or confirm_password.strip() == '':
            message = "Please fill in all fields"
            self.show_popup(message)
            self.highlight_empty_fields()
        elif not self.validate_email(email):
            message = "Invalid email address."
            self.show_popup(message)
            self.highlight_email_field()
        elif password != confirm_password:
            message = "Passwords don't match"
            self.show_popup(message)
        else:
            filename = first_name + '.txt'
            with open(filename, 'w') as file:
                file.write('First Name: {}\n'.format(first_name))
                file.write('Last Name: {}\n'.format(last_name))
                file.write('Email: {}\n'.format(email))
                file.write('Password: {}\n'.format(password))
            message = "Registration Successful!! \nFirst Name: {}\nEmail: {}".format(first_name, email)
            self.show_popup(message)
            self.clear_inputs()

    def validate_email(self, email):
        # Check if email ends with @gmail.com
        pattern = r'^[\w\.-]+@gmail\.com$'
        if re.match(pattern, email):
            return True
        return False

    def show_popup(self, message):
        popup = Popup(title="Registration Status", content=Label(text=message), size_hint=(None, None), size=(400, 200))
        popup.open()

    def highlight_empty_fields(self):
        for input_field in [self.firstname_input, self.lastname_input, self.email_input, self.password_input,
                            self.confirm_input]:
            if input_field.text.strip() == '':
                input_field.background_color = (1, 0, 0, 0.5)  # Red background for empty fields
            else:
                input_field.background_color = (1, 1, 1, 1)  # Reset to white for non-empty fields

    def highlight_email_field(self):
        self.email_input.background_color = (1, 0, 0, 0.5)  # Red background for invalid email
        for input_field in [self.firstname_input, self.lastname_input, self.password_input, self.confirm_input]:
            input_field.background_color = (1, 1, 1, 1)  # Reset to white for other fields

    def clear_inputs(self):
        self.firstname_input.text = ''
        self.lastname_input.text = ''
        self.email_input.text = ''
        self.password_input.text = ''
        self.confirm_input.text = ''
        for input_field in [self.firstname_input, self.lastname_input, self.email_input, self.password_input,
                            self.confirm_input]:
            input_field.background_color = (1, 1, 1, 1)  # Reset to white background


class RegistrationApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(RegistrationScreen(name='registration'))
        return sm


if __name__ == '__main__':
    RegistrationApp().run()