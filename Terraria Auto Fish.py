import cv2
import numpy as np
import pyautogui
import keyboard
import time
from PIL import ImageGrab

# --- Settings ---
BOX_TOP_LEFT = None
BOX_BOTTOM_RIGHT = None
RUNNING = False
SENSITIVITY = 12.0  # Adjust if it triggers too early (increase) or misses bites (decrease)

def capture_box(x1, y1, x2, y2):
    """Captures the defined region as a grayscale image."""
    screenshot = ImageGrab.grab(bbox=(x1, y1, x2, y2))
    frame = np.array(screenshot)
    return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

def set_top_left():
    global BOX_TOP_LEFT
    BOX_TOP_LEFT = pyautogui.position()
    print(f"[+] Top-Left set to: {BOX_TOP_LEFT}")

def set_bottom_right():
    global BOX_BOTTOM_RIGHT
    BOX_BOTTOM_RIGHT = pyautogui.position()
    print(f"[+] Bottom-Right set to: {BOX_BOTTOM_RIGHT}")

def fish_loop():
    global RUNNING
    if not BOX_TOP_LEFT or not BOX_BOTTOM_RIGHT:
        print("[!] Error: Set Box Area (F6 & F7) before starting!")
        return

    x1, y1 = BOX_TOP_LEFT
    x2, y2 = BOX_BOTTOM_RIGHT

    # Ensure coordinates are properly ordered
    x1, x2 = min(x1, x2), max(x1, x2)
    y1, y2 = min(y1, y2), max(y1, y2)

    center_x = (x1 + x2) // 2
    center_y = (y1 + y2) // 2

    print("[*] Starting fishing bot... Press 'F9' to STOP.")
    RUNNING = True

    while RUNNING:
        if keyboard.is_pressed('f9'):
            print("[-] Stopped.")
            RUNNING = False
            break

        # 1. Cast the line
        print("[*] Casting...")
        pyautogui.click(center_x, center_y)

        # 2. Wait for the bobber to land and settle
        time.sleep(2.0)

        # 3. Take baseline frame
        baseline = capture_box(x1, y1, x2, y2)
        baseline = cv2.GaussianBlur(baseline, (21, 21), 0)

        bite_detected = False
        start_wait = time.time()

        print("[*] Waiting for bite inside the box...")
        while not bite_detected and RUNNING:
            if keyboard.is_pressed('f9'):
                RUNNING = False
                break

            # Timeout after 25 seconds if no bite occurs
            if time.time() - start_wait > 25:
                print("[!] Timeout. Recasting...")
                break

            # Capture current state
            current = capture_box(x1, y1, x2, y2)
            current = cv2.GaussianBlur(current, (21, 21), 0)

            # Compare difference
            diff = cv2.absdiff(baseline, current)
            score = np.mean(diff)

            # Check if movement exceeds threshold (Bobber splash/dip)
            if score > SENSITIVITY:
                print(f"[+] Bite detected! Movement score: {score:.2f}")
                # 4. Reel in
                pyautogui.click(center_x, center_y)
                bite_detected = True
                time.sleep(1.0) # Wait before next cast
                break

            time.sleep(0.05)

print("========================================")
print("       Terraria Auto Fishing Bot        ")
print("========================================")
print("1. Hover mouse over TOP-LEFT of bobber area -> Press F6")
print("2. Hover mouse over BOTTOM-RIGHT of bobber area -> Press F7")
print("3. Press F8 to START")
print("4. Press F9 to PAUSE / STOP")
print("5. Hold ESC to completely QUIT")
print("========================================")

keyboard.add_hotkey('f6', set_top_left)
keyboard.add_hotkey('f7', set_bottom_right)
keyboard.add_hotkey('f8', fish_loop)

keyboard.wait('esc')