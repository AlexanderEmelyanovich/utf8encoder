import base64
import binascii

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.metrics import dp


class EncoderApp(App):
    def build(self):
        Window.clearcolor = (0.12, 0.13, 0.16, 1)

        root = BoxLayout(
            orientation="vertical",
            padding=dp(20),
            spacing=dp(12)
        )

        title = Label(
            text="UTF-8 кодировщик",
            font_size="26sp",
            bold=True,
            color=(0.95, 0.95, 0.95, 1),
            size_hint_y=None,
            height=dp(50)
        )

        self.input_text = TextInput(
            hint_text="Введите сообщение или Base64-код",
            multiline=True,
            font_size="18sp",
            size_hint_y=0.38,
            background_color=(0.18, 0.19, 0.22, 1),
            foreground_color=(1, 1, 1, 1),
            cursor_color=(0.3, 0.7, 1, 1),
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
            bold=True,
            background_color=(0.25, 0.60, 0.96, 1),
            color=(1, 1, 1, 1)
        )
        encrypt_button.bind(on_press=self.encode_text)

        decrypt_button = Button(
            text="Декодировать",
            font_size="16sp",
            bold=True,
            background_color=(0.30, 0.70, 0.50, 1),
            color=(1, 1, 1, 1)
        )
        decrypt_button.bind(on_press=self.decode_text)

        clear_button = Button(
            text="Очистить",
            font_size="16sp",
            background_color=(0.75, 0.35, 0.35, 1),
            color=(1, 1, 1, 1),
            size_hint_x=0.4
        )
        clear_button.bind(on_press=self.clear_fields)

        buttons_row.add_widget(encrypt_button)
        buttons_row.add_widget(decrypt_button)

        result_label = Label(
            text="Результат",
            font_size="16sp",
            color=(0.7, 0.7, 0.72, 1),
            size_hint_y=None,
            height=dp(30),
            halign="left"
        )
        result_label.bind(
            size=lambda l, s: l.__setattr__("text_size", (s[0], None))
        )

        result_scroll = ScrollView(size_hint_y=0.38)

        self.result_text = TextInput(
            text="",
            readonly=True,
            multiline=True,
            font_size="18sp",
            background_color=(0.18, 0.19, 0.22, 1),
            foreground_color=(0.95, 0.95, 0.95, 1),
            padding=(dp(12), dp(12)),
            size_hint_y=None,
            height=dp(100)
        )
        self.result_text.bind(
            texture_size=lambda _, ts: self.result_text.__setattr__(
                "height", max(ts[1], dp(100))
            )
        )

        result_scroll.add_widget(self.result_text)

        root.add_widget(title)
        root.add_widget(self.input_text)
        root.add_widget(buttons_row)
        root.add_widget(clear_button)
        root.add_widget(result_label)
        root.add_widget(result_scroll)

        return root

    def encode_text(self, instance):
        message = self.input_text.text

        if not message:
            self.result_text.text = "Введите сообщение."
            return

        try:
            utf8_bytes = message.encode("utf-8")
            encoded_text = base64.b64encode(utf8_bytes).decode("ascii")
            self.result_text.text = encoded_text
        except Exception as error:
            self.result_text.text = f"Ошибка: {error}"

    def decode_text(self, instance):
        encoded_text = self.input_text.text.strip()

        if not encoded_text:
            self.result_text.text = "Введите Base64-код."
            return

        try:
            utf8_bytes = base64.b64decode(encoded_text, validate=True)
            decoded_text = utf8_bytes.decode("utf-8")
            self.result_text.text = decoded_text
        except (binascii.Error, UnicodeDecodeError):
            self.result_text.text = (
                "Ошибка: введённый текст не является "
                "корректным UTF-8 Base64-кодом."
            )
        except Exception as error:
            self.result_text.text = f"Ошибка: {error}"

    def clear_fields(self, instance):
        self.input_text.text = ""
        self.result_text.text = ""


if __name__ == "__main__":
    EncoderApp().run()
