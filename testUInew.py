from tkinter import *
master = Tk()
master.option_add("*Font", "consolas 20")#*ฟร้อนทั้งหมดให้standardเป็นconsolasขนาด20
master.configure(bg='MediumPurple1')#สีbackgroundทั้งหมด
master.title('Project music player by PPKG')
first_line = Label(master, text="Project Music Player by PPKG", font=('consolas', 12), fg='yellow', bg="IndianRed1", width = 35)
second_line = Label(master, text="Name of this song: %s", fg='IndianRed2', bg='turquoise1', width = 35)

#Buttonทำปุ่ม
button_addfile = Button(master, text='Add file', font=("consolas", 12), width = 10, bg='khaki1')
button_play = Button(master, text='▶', width = 8, bg='plum1')
button_pause = Button(master, text='⏸', width = 8, bg='plum1')
button_next = Button(master, text='⏭️', width = 8, bg='plum1')
button_previous = Button(master, text='⏮️', width = 8, bg='plum1')
button_random = Button(master, text='⚅ Randomsong', width = 16, bg='aquamarine')
button_repeat = Button(master, text='🔁 Repeat', width = 16, bg='aquamarine') 
button_addsound = Button(master, text='🔊', width = 6, height=1, bg='cornflowerblue') #เพิ่มเสียง
button_subsound = Button(master, text='🔉', width = 6, height=1, bg='cornflowerblue') #ลดเสียง
#แสดงผล
first_line.grid(row=0, column=0, columnspan=4)
second_line.grid(row=1, column=0, columnspan=4)
button_addfile.grid(row=2, column=1, columnspan=2, pady=10)
txt_addfile = Label(master, text='<< choose a song', font=("Ink Free Reaular", 12), bg='MediumPurple1')
txt_addfile.grid(row=2, column=2, columnspan=3)

button_previous.grid(row=3, column=0, pady = 10)
button_play.grid(row=3, column=1, pady = 10)
button_pause.grid(row=3, column=2, pady = 10)
button_next.grid(row=3, column=3, pady = 10)
button_random.grid(row=4, column=0, columnspan=2, pady = 20)
button_repeat.grid(row=4, column=2, columnspan=3, pady = 20)
row5 = Frame(master)
row5.grid(row=5, column=0, columnspan=4)
Label(row5, text='Volume🎵', bg='MediumPurple1').pack()
button_subsound.grid(row=6, column=1, pady=5)
button_addsound.grid(row=6, column=2, pady=5)

master.mainloop()
