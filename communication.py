import serial


def read_arduino(queue, left_half: bool = True):
    PORT_BASE = "/dev/ttyACM0" if left_half else "/dev/tty"
    with serial.Serial(PORT_BASE, 9600, timeout=1) as set:
        set.reset_input_buffer()
        while True:
            if set.in_waiting:
                line = set.readline().decode('utf-8').strip()
                queue.put({left_half: line})
