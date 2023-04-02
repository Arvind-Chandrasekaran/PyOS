import keyboard

def key_func(fun,key='Enter'):
    def key_press(z):
        global key
        z()
        keyboard.remove_hotkey(key)
    keyboard.add_hotkey(key,lambda:key_press(fun))