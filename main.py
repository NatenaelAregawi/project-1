import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
import kivy

kivy.require('1.9.1')

class MyRoot(BoxLayout):
    random_label_word = ObjectProperty()
    random_label_number = ObjectProperty()

    def __init__(self, **kwargs):
        super(MyRoot, self).__init__(**kwargs)

    def generate_word(self):
        words = ["Hex", "yonichu", "kality","wehazi","jacksu","natty","eyoba","Ashu"]
        random_word = random.choice(words)
        self.random_label_word.text = random_word

    def generate_number(self):
        random_number = str(random.randint(1, 1000))
        self.random_label_number.text = random_number

class NattyRandom(App):
    def build(self):
        return MyRoot()

if __name__ == '__main__':
    NattyRandom().run()
