import keyboard
class NotesByKeyStrokes:
    def __init__(self) -> None:
        self.keyOn = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        pass
    def playing(self):
        if keyboard.is_pressed("a"):
            self.keyOn[0] = 1
        if keyboard.is_pressed("s"):
            self.keyOn[1] = 1
        if keyboard.is_pressed("d"):
            self.keyOn[2] = 1
        if keyboard.is_pressed("f"):
            self.keyOn[3] = 1
        if keyboard.is_pressed("g"):
            self.keyOn[4] = 1
        if keyboard.is_pressed("h"):
            self.keyOn[5] = 1
        if keyboard.is_pressed("j"):
            self.keyOn[6] = 1
        if keyboard.is_pressed("k"):
            self.keyOn[7] = 1
        if keyboard.is_pressed("l"):
            self.keyOn[8] = 1
        if keyboard.is_pressed(";"):
            self.keyOn[9] = 1
        if keyboard.is_pressed("'"):
            self.keyOn[10] = 1
        if keyboard.is_pressed("/"):
            self.keyOn[11] = 1
        return self.keyOn
