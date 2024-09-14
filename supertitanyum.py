import tkinter as tk
from tkinter import ttk
import pyautogui
import time
import threading
import keyboard

class Application:
    def __init__(self, root):
        self.root = root
        self.root.title("SuperSO")
        self.root.geometry("400x200")
        self.root.config(bg="#282828")

        self.style = ttk.Style()
        self.style.configure("TButton", font=("Helvetica", 12), padding=10)
        self.style.configure("TScale", font=("Helvetica", 10), padding=10)

        self.header_label = tk.Label(root, text="Lightning Depo Şifresi Kırıcı", font=("Helvetica", 16, "bold"), bg="#282828", fg="#ffffff")
        self.header_label.pack(pady=15)

        self.start_button = ttk.Button(root, text="Start", command=self.start_process)
        self.start_button.pack(side=tk.LEFT, padx=20)

        self.stop_button = ttk.Button(root, text="Stop", command=self.stop_process, state=tk.DISABLED)
        self.stop_button.pack(side=tk.RIGHT, padx=20)

        self.speed_scale = tk.Scale(root, from_=1, to=10, orient=tk.HORIZONTAL, label="Mouse Speed", length=300)
        self.speed_scale.set(10)
        self.speed_scale.pack(pady=15)

        self.process_running = False

    def start_process(self):
        self.process_running = True
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.speed_scale.config(state=tk.DISABLED)
        self.thread = threading.Thread(target=self.run_process)
        self.thread.start()

    def stop_process(self):
        self.process_running = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.speed_scale.config(state=tk.NORMAL)

    def run_process(self):
        speed = self.speed_scale.get()
        pyautogui.PAUSE = 1 / speed

        # F12 TO STOP
        keyboard.add_hotkey('f12', self.stop_process)


        chest_position = (885, 550)
        positions = {
            '0': [(958, 645)],
            '1': [(914, 509)],
            '2': [(958, 509)],
            '3': [(1006, 509)],
            '4': [(914, 556)],
            '5': [(958, 556)],
            '6': [(1006, 556)],
            '7': [(914, 600)],
            '8': [(958, 600)],
            '9': [(1006, 600)]
        }


        tick_position = (1000, 645)


        pyautogui.moveTo(chest_position[0], chest_position[1], duration=0.5)
        time.sleep(0.5)
        pyautogui.click(clicks=1)


        for i in range(285, 10000):
            if not self.process_running:
                break

            password = str(i).zfill(4) 
            print(f"Trying password: {password}")


            for digit in password:
                digit_positions = positions[digit]
                for pos in digit_positions:
                    pyautogui.moveTo(pos[0], pos[1], duration=0.1)  
                    pyautogui.click(clicks=1)
                    time.sleep(0.05)

  
            pyautogui.moveTo(tick_position[0], tick_position[1], duration=0.1)  
            pyautogui.click(clicks=1)
            time.sleep(0.05)


            pyautogui.moveTo(chest_position[0], chest_position[1], duration=0.5)
            time.sleep(0.5)
            pyautogui.click(clicks=1)

        self.stop_process()

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    root.mainloop()
