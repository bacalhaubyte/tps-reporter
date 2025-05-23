import keyboard
import time
import random

def keep_active():
    try:
        print("TPS Report Compiling... Press Ctrl+C to stop.")
        while True:
            # Press F15 key (invisible key 'scrlk' press that won't disrupt your work)
            keyboard.press_and_release('f15')
            # Random wait between X,Y seconds
            wait_time = random.randint(4, 25)
            print(f"PC Load Letter! Next attempt in {wait_time} seconds.")
            time.sleep(wait_time)
    except KeyboardInterrupt:
        print("Halt & Catch Fire.")

if __name__ == "__main__":
    keep_active()
