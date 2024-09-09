import serial


def read_arduino(queue, left_half: bool = True):
    PORT_BASE = "/dev/ttyACM0" if left_half else "/dev/tty"
    previous_str = "0" * 14
    with serial.Serial(PORT_BASE, 9600, timeout=1) as set:
        set.reset_input_buffer()
        while True:
            if set.in_waiting:
                b = set.readline()
                try:
                    line = b.decode('utf-8').strip()
                except UnicodeDecodeError as e:
                    print(b)
                    continue

                if len(line) != 8:
                    print(line)
                    continue
                for c1, c2 in zip(line[:-1], previous_str):
                    if c1 != c2:
                        previous_str = line
                        break
                else:
                    continue

                if line[-1] == "1":
                    line = ["0" for _ in range(len(line)-1)]
                else:
                    line = line[:-1]

                queue.put({left_half: line})
