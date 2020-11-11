import pyglet
from pyglet.window import key  #contains all the keyboard key codes
from pyglet.window import mouse #contains all the mouse actions possible

window = pyglet.window.Window()

label = pyglet.text.Label('Hello World',
                          font_name='JetBrains Mono',
                          font_size=36,
                          x = window.width//2, y = window.height//2,
                          anchor_x = 'center', anchor_y='center')
image = pyglet.image.load('Screenshot_20201023_142642.png')

event_logger = pyglet.window.event.WindowEventLogger()
window.push_handlers(event_logger)

@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        print('MLB')

#Keyboard events 
@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.A:
        print('A')

    elif symbol == key.W:
        print('W')

#Draw Call
@window.event
def on_draw():
    window.clear()
    image.blit(0, 0)
    label.draw()


pyglet.app.run()
