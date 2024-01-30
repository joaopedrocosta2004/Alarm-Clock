# Alarm clock project in python
# João Pedro Costa
# 29/01/2024

import time
from plyer import notification
import pygame as pygame

def user_interface():
    print ("Alarm Clock Iniciated")
    user_time = input("What time you want to set the alarm: ").split(":")
    hour = str(user_time[0])
    minute = str(user_time[1])
    second = str(user_time[2])
    alarm_time = hour + ":" + minute + ":" + second
    return alarm_time


def main():
    pygame.init()
    my_sound = pygame.mixer.Sound('80s-alarm-clock-sound.wav')
    alarm_time = user_interface()
    while True:
        current_time = time.strftime("%H:%M:%S")
        if current_time >= alarm_time:
            print("It's time to wake up!")
            my_sound.play()
            notification.notify(
                title = 'Alarm Clock',
                message = 'Its time to wake up',
                app_icon = 'clock.ico',
                timeout = 10,
            )
            break
        else:
            print (current_time)
        time.sleep(1)

main()


