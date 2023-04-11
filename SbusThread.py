#!/usr/bin/env python3
from threading import Thread
import  time
import rpi_gpio_sbus as sbus

class SbusThread(object):
    def __init__(self, SBUS_PIN=13):

        self.reader = sbus.SbusReader(SBUS_PIN)
        self.reader.begin_listen()
        self.is_connected = False
       
        # FPS = 1/X
        # X = desired FPS
        self.FPS = 1/30
        self.FPS_MS = int(self.FPS * 1000)
        
        # Start frame retrieval thread
        self.thread = Thread(target=self.update, args=())
        self.thread.daemon = True
        self.thread.start()
        
    def update(self):
        while True:
            if not self.reader.is_connected():
                continue
            try:
                self.is_connected = self.reader.is_connected()
                self.packet_age = self.reader.get_latest_packet_age()
                #returns list of length 16, so -1 from channel num to get index
                self.channel_data = self.reader.translate_latest_packet()
                time.sleep(self.FPS)

            except:
                #cleanup cleanly after error
                self.reader.end_listen()
                raise
    
    def get_SBUS(self):
        if hasattr(self,"channel_data"):
            return self.channel_data
        return None