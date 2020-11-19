from pygame import mixer
from tkinter import Tk
from tkinter import Label
from tkinter import Button
from tkinter import filedialog

current_volume = float(0.5)

#Functions
def play_song():
    filename = filedialog.askopenfilename(initialdir="C:/", title="Please choose a song")
    print(filename)

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
Button(master, text="Pause", font=("Ink Free Reaular", 12)).grid(row=3, sticky="E")
Button(master, text="Resume", font=("Ink Free Reaular", 12)).grid(row=3, sticky="W")
Button(master, text="-", font=("Ink Free Reaular", 12), width=5).grid(row=5, sticky="W")
Button(master, text="+", font=("Ink Free Reaular", 12), width=5).grid(row=5, sticky="E")


#, """command=volume_up"""
#, """command=volume_down"""
#command=pause_song
#, """command=resume_song"""
master.mainloop()