import base64
import binascii

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.metrics import dp


class EncoderApp(App):
    def build(self):
        root = BoxLayout(
            orientation="vertical",
            padding=dp(20),
            spacing=dp(12)
        )

        title = Label(
            text="UTF-8 кодировщик",
            font_size="26sp",
            size_hint_y=None,
            height=dp(50),
            color=(1, 1, 1, 1)
        )

        self.input_text = TextInput(
            hint_text="Введите сообщение или Base64-код",
            multiline=True,
            font_size="18sp",
            size_hint_y=0.38,
            padding=(dp(12), dp(12))
        )

        buttons_row = BoxLayout(
            orientation="horizontal",
            size_hint_y=None,
            height=dp(55),
            spacing=dp(10)
        )

        encrypt_button = Button(
            text="Кодировать",
            font_size="16sp",
            background_color=(0.25, 0.60, 0.96, 1)
        )
        encrypt_button.bind(on_press=self.encode_text)

        decrypt_button = Button(
            text="Декодировать",
            font_size="16sp",
            background_color=(0.30, 0.70, 0.50, 1)
        )
        decrypt_button.bind(on_press=self.decode_text)

        clear_button = Button(
            text="Очистить",
            font_size="16sp",
            background_color=(0.75, 0.35, 0.35, 1),
            size_hint_x=0.4
        )
        clear_button.bind(on_press=self.clear_fields)

        buttons_row.add_widget(encrypt_button)
        buttons_row.add_widget(decrypt_button)

        result_label = Label(
            text="Результат",
            font_size="16sp",
            size_hint_y=None,
            height=dp(30),
            color=(0.7, 0.7, 0.72, 1),
            halign="left"
        )
        result_label.bind(
            size=lambda l, s: setattr(l, "text_size", (s[0], None))
        )

        self.result_text = TextInput(
            text="",
            readonly=True,
            multiline=True,
            font_size="18sp",
            size_hint_y=0.38,
            padding=(dp(12), dp(12))
        )

        root.add_widget(title)
        root.add_widget(self.input_text)
        root.add_widget(buttons_row)
        root.add_widget(clear_button)
        root.add_widget(result_label)
        root.add_widget(self.result_text)

        return root

    def encode_text(self, instance):
        message = self.input_text.text
        if not message:
            self.result_text.text = "Введите сообщение."
            return
        try:
            utf8_bytes = message.encode("utf-8")
            self.result_text.text = base64.b64encode(utf8_bytes).decode("ascii")
        except Exception as error:
            self.result_text.text = "Ошибка: " + str(error)

    def decode_text(self, instance):
        encoded_text = self.input_text.text.strip()
        if not encoded_text:
            self.result_text.text = "Введите Base64-код."
            return
        try:
            utf8_bytes = base64.b64decode(encoded_text, validate=True)
            self.result_text.text = utf8_bytes.decode("utf-8")
        except (binascii.Error, UnicodeDecodeError):
            self.result_text.text = "Ошибка: некорректный Base64-код."
        except Exception as error:
            self.result_text.text = "Ошибка: " + str(error)

    def clear_fields(self, instance):
        self.input_text.text = ""
        self.result_text.text = ""


if __name__ == "__main__":
    EncoderApp().run()
