import os
import random
import pygame

pygame.mixer.init()

def play_random_music(emotion):
    folder_path = f"music/{emotion}"
    if not os.path.exists(folder_path):
        print("No music folder for this emotion.")
        return

    songs = [f for f in os.listdir(folder_path) if f.endswith(".mp3")]
    if songs:
        song_path = os.path.join(folder_path, random.choice(songs))
        pygame.mixer.music.load(song_path)
        pygame.mixer.music.play()
    else:
        print("No songs found.")

def pause_music():
    pygame.mixer.music.pause()

def unpause_music():
    pygame.mixer.music.unpause()

def stop_music():
    pygame.mixer.music.stop()

