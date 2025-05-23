import pyautogui
import random
import time

def random_mouse_movement():
    # Get screen size
    screen_width, screen_height = pyautogui.size()
    
    print("TPS Report Compiling... Ctrl+C to stop.")
    
    try:
        while True:
            # Generate random coordinates within screen boundaries
            x = random.randint(0, screen_width)
            y = random.randint(0, screen_height)
            
            # Move mouse to the generated position
            pyautogui.moveTo(x, y, duration=0.5)
            
            # Wait for random time between X-Y seconds before next movement
            wait_time = random.uniform(3, 14)
            print(f"PC Load Letter ({x},{y}). Next attempt in {wait_time:.1f} seconds.")
            time.sleep(wait_time)
            
    except KeyboardInterrupt:
        print("Halt & Catch Fire.")

if __name__ == "__main__":
    # Adds small delay before starting to allow user time to hide window
    print("Lumbergh is watching, hide this window!")
    time.sleep(3)
    random_mouse_movement()
