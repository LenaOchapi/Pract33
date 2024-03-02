import kivy
kivy.require('1.0.7')
from kivy.animation import Animation
from kivy.app import App
from kivy.uix.button import Button


class TestApp(App):
    def animate(self, instance):
        animation = Animation(pos=(100, 100), t='out_bounce')
        animation += Animation(pos=(200, 100), t='out_bounce')
        animation &= Animation(size=(500, 500))
        animation += Animation(size=(100, 50))
        animation.start(instance)

    def build(self):
        #hex в  RGBA
        hex_color = "#57ff81"  # Красный цвет
        red = int(hex_color[1:3], 16) / 255.0
        green = int(hex_color[3:5], 16) / 255.0
        blue = int(hex_color[5:7], 16) / 255.0
        alpha = 1.0 #прозрачность

        button = Button(size_hint=(None, None), text='чпоньк',
                        on_press=self.animate,
                        background_color=(red, green, blue, alpha))  # Устанавливаем красный цвет фона кнопки
        return button


if __name__ == '__main__':
    TestApp().run()

