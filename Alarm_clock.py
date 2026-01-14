import time
import pygame

pygame.mixer.init()

def alarm(total_seconds):
    while total_seconds > 0:
        minutes = total_seconds // 60
        seconds = total_seconds % 60

        print(f"\rTime Left: {minutes:02d}:{seconds:02d}", end="")
        time.sleep(1)
        total_seconds -= 1

    print("\n⏰ TIME UP!")

    pygame.mixer.music.load("alarm.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(1)

minutes = int(input("Enter minutes: "))
seconds = int(input("Enter seconds: "))
alarm(minutes * 60 + seconds)
