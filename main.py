import subprocess

from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout

from io import StringIO
import sys


class Root(AnchorLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        sys.stdout = StringIO()

    def python_execute(self, command):
        eval(command)
        self.ids.output.text = sys.stdout.getvalue()

    def terminal_execute(self, command):
        process = subprocess.Popen(command.split(), stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        stdout, stderr = process.communicate()
        self.ids.output.text = 'STDOUT:\n{}\n\nSTDERR:\n{}'.format(stdout, stderr)


class TestKivyAPKApp(App):
    def build(self):
        return Root()


if __name__ == '__main__':
    app = TestKivyAPKApp()
    app.kv_file = 'main.kv'
    app.run()
