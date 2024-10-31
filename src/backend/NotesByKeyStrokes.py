import keyboard
class NotesByKeyStrokes:
    def __init__(self) -> None:
        self.keyOn = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        pass
    def playing(self):
        if keyboard.is_pressed("a"):
            self.keyOn[0] = 1
        if keyboard.is_pressed("w"):
            self.keyOn[1] = 1
        if keyboard.is_pressed("s"):
            self.keyOn[2] = 1
        if keyboard.is_pressed("e"):
            self.keyOn[3] = 1
        if keyboard.is_pressed("d"):
            self.keyOn[4] = 1
        if keyboard.is_pressed("f"):
            self.keyOn[5] = 1
        if keyboard.is_pressed("t"):
            self.keyOn[6] = 1
        if keyboard.is_pressed("g"):
            self.keyOn[7] = 1
        if keyboard.is_pressed("y"):
            self.keyOn[8] = 1
        if keyboard.is_pressed("h"):
            self.keyOn[9] = 1
        if keyboard.is_pressed("u"):
            self.keyOn[10] = 1
        if keyboard.is_pressed("j"):
            self.keyOn[11] = 1
        return self.keyOn
