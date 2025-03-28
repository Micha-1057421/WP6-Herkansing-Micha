import keyboard
import threading
import time

class InputHandler:
    def __init__(self, left_flipper, right_flipper):
        self.left_flipper = left_flipper
        self.right_flipper = right_flipper
        self.running = False

    def start_listening(self):
        self.running = True
        thread = threading.Thread(target=self._listen, daemon=True)
        thread.start()

    def _listen(self):
        print("Input handler actief: druk op 'A' (links) of 'L' (rechts)")
        while self.running:
            if keyboard.is_pressed('a'):
                self.left_flipper.activate()
            else:
                self.left_flipper.deactivate()

            if keyboard.is_pressed('l'):
                self.right_flipper.activate()
            else:
                self.right_flipper.deactivate()

            time.sleep(0.05)  # debounce