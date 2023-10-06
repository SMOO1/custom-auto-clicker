
import keyboard
import time
import threading

program_running = False

key_to_click = input("KEY TO CLICK: ")


def click():
    global program_running

    while True:
        if program_running:
            keyboard.press(key_to_click)
            time.sleep(0.05)
            keyboard.release(key_to_click)
        else:
            time.sleep(0.01)

def toggle_program_state(e):
    global program_running
    program_running = not program_running
    print("Program is now", "on" if program_running else "off")

click_thread = threading.Thread(target=click)
click_thread.daemon = True
click_thread.start()

keyboard.on_press_key("F6", toggle_program_state)

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    pass
