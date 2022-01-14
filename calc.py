
from kivy.app import App
from kivy.uix.label import Label

from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.base import runTouchApp
from plants_and_substances import florarium
lst = florarium.keys()
print(lst)


class MainApp(App):
    def build(self):
        label = Label(text='Hello from Kivy',
                      size_hint=(.5, .5),
                      pos_hint={'center_x': .5, 'center_y': .5})

        return label

    dropdown = DropDown()
    for index in range(len(lst)):
        btn = Button(text='%d' % index,
                     size_hint_y=None, height=44)
        btn.bind(on_release=lambda btn: dropdown.select(btn.text))

        dropdown.add_widget(btn)

    mainbutton = Button(text='Список растений', size_hint=(.2, .1),
                        pos_hint={'center_x': .1, 'center_y': .9})
    mainbutton.bind(on_release=dropdown.open)

    dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))
    runTouchApp(mainbutton)


if __name__ == '__main__':
    app = MainApp()
    app.run()
