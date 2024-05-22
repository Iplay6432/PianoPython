#!/usr/bin/env python3

import serial


def main():
    PORT_BASE = "/dev/tty"
    with serial.Serial() as set:
        while True:
            pass


if __name__ == "__main__":
    main()
