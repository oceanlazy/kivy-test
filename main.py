import subprocess

from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout

from io import StringIO
import sys


class Root(AnchorLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        sys.stdout = StringIO()
        self.ids.output.bind(size=self.ids.output.setter('text_size'))  # todo move to kv

    def python_execute(self, command):
        try:
            eval('print({})'.format(command))
            self.ids.output.text = sys.stdout.getvalue()
        except Exception as e:
            self.ids.output.text = str(e)

    def terminal_execute(self, command):
        try:
            process = subprocess.Popen(command.split(), stdin=subprocess.PIPE, stdout=subprocess.PIPE)
            stdout, stderr = process.communicate()
            self.ids.output.text = 'STDOUT:\n{}\n\nSTDERR:\n{}'.format(stdout, stderr)
        except Exception as e:
            self.ids.output.text = str(e)


class TestKivyAPKApp(App):
    def build(self):
        return Root()


if __name__ == '__main__':
    app = TestKivyAPKApp()
    app.kv_file = 'main.kv'
    app.run()
