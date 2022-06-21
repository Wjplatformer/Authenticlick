from pynput import mouse
'''
def on_move(x, y):
    print('Pointer moved to {0}'.format(
        (x, y)))
'''
def on_click(x, y, button, pressed):
    if pressed == False:
        print('clicked!')

# Collect events until released
while True:
    with mouse.Listener(
            on_click=on_click) as listener:
        listener.join()


# https://pypi.org/project/pynput/