import os
import random
import pickle
import tkinter as tk
from tkinter import filedialog
from tkinter import PhotoImage
from pygame import mixer

class Player(tk.Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		self.pack()
		mixer.init()

		if os.path.exists('songs.pickle'):
			with open('songs.pickle', 'rb') as f:
				self.playlist = pickle.load(f)
		else:
			self.playlist=[]

		self.current = 0
		self.paused = True
		self.played = False

		self.create_frames()
		self.track_widgets()
		self.control_widgets()
		self.tracklist_widgets()

		self.master.bind('<Left>', self.prev_song)
		self.master.bind('<space>', self.play_pause_song)
		self.master.bind('<Right>', self.next_song)

	def create_frames(self):
		self.config(bg='mediumorchid1')
		self.track = tk.LabelFrame(self, text='Song Track', 
					font=("helvetica",15,"bold"),
					bg="Yellow",fg="midnight blue",bd=5,relief=tk.GROOVE)
		self.track.config(width=250,height=300)
		self.track.grid(row=0, column=0, padx=10, pady=5)

		self.tracklist = tk.LabelFrame(self, text=f'PlayList - {str(len(self.playlist))}',
							font=("helvetica",15,"bold"),
							bg="midnight blue",fg="white")
		self.tracklist.config(width=190,height=400)
		self.tracklist.grid(row=0, column=1, rowspan=3, pady=5)

		self.controls = tk.LabelFrame(self,
							font=("helvetica",15,"bold"),
							bg="royalblue1",fg="white",bd=2,relief=tk.GROOVE)
		self.controls.config(width=410,height=80)
		self.controls.grid(row=2, column=0, pady=5, padx=10)

	def track_widgets(self):
		self.canvas = tk.Label(self.track, image=img)
		self.canvas.configure(width=300, height=240)
		self.canvas.grid(row=0,column=0)

		self.songtrack = tk.Label(self.track, font=("helvetica",16,"bold"),
						bg="midnight blue",fg="white")
		self.songtrack['text'] = 'PPKG-Music'
		self.songtrack.config(width=30, height=1)
		self.songtrack.grid(row=1,column=0,padx=10)

	def control_widgets(self):
		self.random = tk.Button(self.controls, image=random, bg='white')
		self.random['command'] = self.random_song
		self.random.grid(row=0, column=0, padx=7)

		self.prev = tk.Button(self.controls, image=prev, bg='white')
		self.prev['command'] = self.prev_song
		self.prev.grid(row=0, column=1)

		self.pause = tk.Button(self.controls, image=pause, bg='white')
		self.pause['command'] = self.pause_song
		self.pause.grid(row=0, column=2)

		self.next = tk.Button(self.controls, image=next_, bg='white')
		self.next['command'] = self.next_song
		self.next.grid(row=0, column=3)
		
		self.repeat = tk.Button(self.controls, image=repeat, bg='white')
		self.repeat['command'] = self.repeat_songs
		self.repeat.grid(row=0, column=4, padx=7)
		
		self.slider = tk.Scale(self.controls, from_ = 0, to = 10, orient = tk.HORIZONTAL, bg='white', fg='blue4')
		self.slider['variable'] = tk.DoubleVar(self)
		self.slider.set(5)
		mixer.music.set_volume(0.1)
		self.slider['command'] = self.change_volume
		self.slider.grid(row=0, column=6, padx=5)


	def tracklist_widgets(self):
		self.scrollbar = tk.Scrollbar(self.tracklist, orient=tk.VERTICAL)
		self.scrollbar.grid(row=0,column=1, rowspan=4, sticky='ns')

		self.list = tk.Listbox(self.tracklist, selectmode=tk.SINGLE,
					 yscrollcommand=self.scrollbar.set, selectbackground='royalblue1')
		self.enumerate_songs()
		self.list.config(height=15)
		self.list.bind('<Double-1>', self.play_song) 

		self.scrollbar.config(command=self.list.yview)
		self.list.grid(row=0, column=0, rowspan=4)

		self.loadSongs = tk.Button(self.tracklist, bg="yellow", fg='midnight blue', font='consolas 10')
		self.loadSongs['text'] = 'Add🎵'
		self.loadSongs['command'] = self.retrieve_songs
		self.loadSongs.grid(row=5, column=0, pady=2)

	def retrieve_songs(self):
		self.songlist = []
		directory = filedialog.askdirectory()
		for root_, _, files in os.walk(directory):
				for file in files:
					if os.path.splitext(file)[1] == '.mp3':
						path = (root_ + '/' + file).replace('\\','/')
						self.songlist.append(path)

		with open('songs.pickle', 'wb') as f:
			pickle.dump(self.songlist, f)
		self.playlist = self.songlist
		self.tracklist['text'] = f'PlayList - {str(len(self.playlist))}'
		self.list.delete(0, tk.END)
		self.enumerate_songs()

	def enumerate_songs(self):
		for index, song in enumerate(self.playlist):
			self.list.insert(index, os.path.basename(song))

	def play_pause_song(self, event):
		if self.paused:
			self.play_song()
		else:
			self.pause_song()

	def play_song(self, event=None):
		if event is not None:
			self.current = self.list.curselection()[0]
			for i in range(len(self.playlist)):
				self.list.itemconfigure(i, bg="white")

		print(self.playlist[self.current])
		mixer.music.load(self.playlist[self.current])
		self.songtrack['anchor'] = 'w' 
		self.songtrack['text'] = os.path.basename(self.playlist[self.current])

		self.pause['image'] = play
		self.paused = False
		self.played = True
		self.list.activate(self.current)
		self.list.itemconfigure(self.current, bg='royalblue1')

		mixer.music.play()

	def pause_song(self):
		if not self.paused:
			self.paused = True
			mixer.music.pause()
			self.pause['image'] = pause
		else:
			if self.played == False:
				self.play_song()
			self.paused = False
			mixer.music.unpause()
			self.pause['image'] = play

	def prev_song(self, event=None):
		self.master.focus_set()
		if self.current > 0:
			self.current -= 1
		else:
			self.current = 0
		self.list.itemconfigure(self.current + 1, bg='white')
		self.play_song()

	def next_song(self, event=None):
		self.master.focus_set()
		if self.current < len(self.playlist) - 1:
			self.current += 1
		else:
			self.current = 0
		self.list.itemconfigure(self.current - 1, bg='white')
		self.play_song()

	def change_volume(self, event=None):
		self.v = self.volume.get()
		mixer.music.set_volume(self.v / 10)

	def repeat_songs(self, event=None): #this function is called when clicking on REPEAT button.
		mixer.music.play(-1)

	def random_song(self, event=None):
		import random
		random_num = random.randrange(0, len(self.playlist))
		random_file = self.playlist[random_num]
		mixer.music.load(random_file)
		self.songtrack['text'] = os.path.basename(self.playlist[random_num])
		mixer.music.play()

#แก้ไข UI

if __name__ == '__main__':
	root = tk.Tk()
	root.geometry('770x440')
	root.title('Music Player')
	root.configure(bg='mediumorchid1')

	img = PhotoImage(file='icons/music.gif')
	next_ = PhotoImage(file = 'icons/next.png')
	prev = PhotoImage(file='icons/prev.png')
	play = PhotoImage(file='icons/play.png')
	pause = PhotoImage(file='icons/pause.png')
	repeat = PhotoImage(file='icons/repeat.png')
	random = PhotoImage(file='icons/dice.png')

	app = Player(master=root)
	app.mainloop()
