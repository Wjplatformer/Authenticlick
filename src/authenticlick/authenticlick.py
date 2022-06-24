from time import perf_counter
from pynput import mouse

#VAR
CLauthPWxanpttrn=[]
time_start=0
time_end=0
recording_ongoing=False
auth_len=5
listener=0

def click(x, y, button, pressed):
    global CLauthPWxanpttrn, time_start, time_end, recording_ongoing

    if pressed == True and recording_ongoing == True:
        time_end=perf_counter()
        print(f'recording {time_end - time_start:0.1f}!')
        CLauthPWxanpttrn.append(f"{time_end - time_start: 0.1f}")
    else:
        time_start=perf_counter()
        if CLauthPWxanpttrn == []:
            recording_ongoing = True

    #stop the thread
    if len(CLauthPWxanpttrn) == auth_len:
        recording_ongoing = False
        listener.stop()

def click_record(pw_len):
    global listener, auth_len, CLauthPWxanpttrn
    
    auth_len=pw_len
    listener=mouse.Listener(on_click=click)
    listener.start()
    listener.join()

def get_click():
    return CLauthPWxanpttrn

def authenticate():
    pass

# https://pypi.org/project/pynput/