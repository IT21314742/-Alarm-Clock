# Python Alarm Clock

import time
import datetime
import pygame

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    sound_file = "mp3.mp3"
    is_running = True

    while is_running:
        current_time = datetime.datetime.now()





if __name__ == "__main__": 
    alarm_time = input("Enter the alarm time (HH:MM:SS): ")
    set_alarm(alarm_time)