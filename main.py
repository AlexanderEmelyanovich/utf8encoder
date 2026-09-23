import base64
import binascii

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window


class EncoderApp(App):
    def build(self):
        Window.size = (400, 700)

        root = BoxLayout(
            orientation="vertical",
            padding=15,
            spacing=10
        )

        title = Label(
            text="UTF-8 кодировщик",
            font_size="24sp",
            size_hint_y=None,
            height=50
        )

        self.input_text = TextInput(
            hint_text="Введите сообщение или Base64-код",
            multiline=True,
            font_size="18sp",
            size_hint_y=0.35
        )

        encrypt_button = Button(
            text="Зашифровать / закодировать",
            font_size="17sp",
            size_hint_y=None,
            height=60
        )
        encrypt_button.bind(on_press=self.encode_text)

        decrypt_button = Button(
            text="Дешифровать / декодировать",
            font_size="17sp",
            size_hint_y=None,
            height=60
        )
        decrypt_button.bind(on_press=self.decode_text)

        clear_button = Button(
            text="Очистить",
            font_size="17sp",
            size_hint_y=None,
            height=50
        )
        clear_button.bind(on_press=self.clear_fields)

        result_label = Label(
            text="Результат:",
            font_size="18sp",
            size_hint_y=None,
            height=35,
            halign="left"
        )
        result_label.bind(size=self.update_text_size)

        self.result_text = TextInput(
            text="",
            readonly=True,
            multiline=True,
            font_size="18sp",
            size_hint_y=0.35
        )

        root.add_widget(title)
        root.add_widget(self.input_text)
        root.add_widget(encrypt_button)
        root.add_widget(decrypt_button)
        root.add_widget(clear_button)
        root.add_widget(result_label)
        root.add_widget(self.result_text)

        return root

    def update_text_size(self, label, size):
        label.text_size = (size[0], None)

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
            utf8_bytes = base64.b64decode(
                encoded_text,
                validate=True
            )
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
