# -*- coding:UTF-8 -*-
import pyglet

window = pyglet.window.Window(fullscreen=False, resizable=True, style=pyglet.window.Window.WINDOW_STYLE_BORDERLESS)

@window.event
def on_draw():
    window.clear()

if __name__ == '__main__':
    config = window.context.config
    print(config.double_buffer)
    print(config.aux_buffers)
    platform = pyglet.window.get_platform()
    display = platform.get_default_display()
    for screen in display.get_screens():
        print(screen)
    window.maximize()
    print (window.width)
    print (window.height)
    pyglet.app.run()

