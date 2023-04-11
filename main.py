#!/usr/bin/env python3
import time


from SbusThread import SbusThread
sbusThread = SbusThread(13)

while True:
    SBUS = sbusThread.get_SBUS()
    if SBUS is not None:
        print(SBUS)
    time.sleep(.2)