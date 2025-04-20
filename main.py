import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from mood_detector import detect_emotion
from music_player import play_random_music, stop_music

class EmotionMusicApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Emotion-Based Music Player")
        self.root.geometry("500x600")
        self.root.configure(bg="black")
        
        self.emotion = tk.StringVar(value="Detecting...")

        # Logo / Image
        img = Image.open("assets/background.jpg").resize((500, 250))
        self.bg_image = ImageTk.PhotoImage(img)
        tk.Label(root, image=self.bg_image).pack()

        # Emotion Display
        self.label = tk.Label(root, textvariable=self.emotion, font=("Helvetica", 18), fg="white", bg="black")
        self.label.pack(pady=20)

        # Buttons
        ttk.Button(root, text="Detect Mood", command=self.detect).pack(pady=10)
        ttk.Button(root, text="Play Music", command=self.play).pack(pady=10)
        ttk.Button(root, text="Stop Music", command=stop_music).pack(pady=10)

    def detect(self):
        mood = detect_emotion()
        self.emotion.set(f"Your mood is: {mood}")

    def play(self):
        play_random_music(self.emotion.get().split(":")[-1].strip())

if __name__ == "__main__":
    root = tk.Tk()
    app = EmotionMusicApp(root)
    root.mainloop()
