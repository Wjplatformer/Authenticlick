from time import perf_counter
from pynput import mouse
import sys

#VAR
pattern=[]
time_start=0
time_end=0

def click(x, y, button, pressed):
    global pattern, time_start, time_end

    if len(pattern) == 12:
        print(pattern)
        sys.exit()

    if pressed == False:
        print('click started')
        time_start=perf_counter()
        if pattern == []:
            pattern.append('test')
    else:
        if pattern != []:
            time_end=perf_counter()
            print(f'clicked completed at {time_end - time_start:0.1f}!')
            pattern.append(f"{time_end - time_start: 0.1f}")
        

# Collect events until released
while True:
    with mouse.Listener(
            on_click=click) as listener:
        listener.join()


# https://pypi.org/project/pynput/