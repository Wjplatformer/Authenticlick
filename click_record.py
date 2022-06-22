from time import perf_counter
from pynput import mouse

#VAR
pattern=[]
time_start=0
time_end=0
recording_ongoing=False

def click(x, y, button, pressed):
    global pattern, time_start, time_end, recording_ongoing

    if pressed == True and recording_ongoing == True:
        time_end=perf_counter()
        print(f'clicked completed at {time_end - time_start:0.1f}!')
        pattern.append(f"{time_end - time_start: 0.1f}")
    else:
        print('click started')
        time_start=perf_counter()
        if pattern == []:
            recording_ongoing = True

    if len(pattern) == 10:
        recording_ongoing = False
        print(pattern)
        listener.stop()

with mouse.Listener(on_click=click) as listener:
    listener.join()

# https://pypi.org/project/pynput/