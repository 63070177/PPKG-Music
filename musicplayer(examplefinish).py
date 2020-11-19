from pygame import mixer
from tkinter import Tk
from tkinter import Label
from tkinter import Button
from tkinter import filedialog

current_volume = float(0.5)

#Functions
def play_song():
    filename = filedialog.askopenfilename(initialdir="C:/", title="Please choose a song")
    current_song = filename
    song_title = filename.split("/")
    song_title = song_title[-1]
    try:
        mixer.init()
        mixer.music.load(current_song)
        mixer.music.set_volume(current_volume)
        mixer.music.play()
        song_title_label.config(fg="green", text="Now Playing : " + str(song_title))
        volume_label.config(fg="green", text="Volume : " + str(current_volume))
    except Exception as e:
        print(e)
        song_title_label.config(fg="red", text="Error Can't play")
        mixer.music.pause()

def volume_down():
    try:
        global current_volume
        if current_volume <= float(0):
            volume_label.config(fg="red", text="Volume : Muted")
            return
        current_volume = current_volume - float(0.1)
        current_volume = round(current_volume, 1)
        mixer.music.set_volume(current_volume)
        volume_label.config(fg="green", text="Volume : " + str(current_volume))
    except Exception as e:
        print(e)
        song_title_label.config(fg="red", text="Track hasn't been chosen")

def volume_up():
    try:
        global current_volume
        if current_volume >= float(1):
            volume_label.config(fg="red", text="Volume : Max")
            return
        current_volume = current_volume + float(0.1)
        current_volume = round(current_volume, 1)
        mixer.music.set_volume(current_volume)
        volume_label.config(fg="green", text="Volume : " + str(current_volume))
    except Exception as e:
        print(e)
        song_title_label.config(fg="red", text="Track hasn't been chosen")

def pause_song():
    try:
        mixer.music.pause()
    except Exception as e:
        print(e)
        song_title_label.config(fg="red", text="Track hasn't been chosen")

def resume_song():
    try:
        mixer.music.unpause()
    except Exception as e:
        print(e)
        song_title_label.config(fg="red", text="Track hasn't been chosen")


#main screen
master = Tk()
master.title("Music Player")
master.geometry('900x600')
#Labels
Label(master, text="Music Player", font=("Ink Free Reaular", 18), fg="red").grid(sticky="N", row=0, padx=350)
Label(master, text="Choose a music track", font=("Ink Free Reaular", 16), fg="green").grid(sticky="N", row=1)
Label(master, text="Volume", font=("Ink Free Reaular", 12), fg="red").grid(sticky="N", row=4)
song_title_label = Label(master, font=("Ink Free Reaular", 12))
song_title_label.grid(sticky="N", row=3)
volume_label = Label(master, font=("Ink Free Reaular", 12))
volume_label.grid(sticky="N", row=5)

#Button
Button(master, text="Choose Song", font=("Ink Free Reaular", 12), command=play_song).grid(row=2, sticky="N")
Button(master, text="Pause", font=("Ink Free Reaular", 12), command=pause_song).grid(row=3, sticky="E")
Button(master, text="Resume", font=("Ink Free Reaular", 12), command=resume_song).grid(row=3, sticky="W")
Button(master, text="-", font=("Ink Free Reaular", 12), width=5, command=volume_down).grid(row=5, sticky="W")
Button(master, text="+", font=("Ink Free Reaular", 12), width=5, command=volume_up).grid(row=5, sticky="E")






master.mainloop()
