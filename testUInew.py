from tkinter import *
root = Tk()
root.option_add("*Font", "consolas 25")#*ฟร้อนทั้งหมดให้standardเป็นconsolasขนาด25
root.configure(bg='MediumPurple1')#สีbackgroundทั้งหมด
root.title('Project music player by PPKG')
first_line = Label(root, text="Project Music Player", bg="IndianRed1", width = 35)
second_line = Label(root, text="Name of this song: %s", bg='turquoise1', width = 35)

#Buttonทำปุ่ม
button_addfile = Button(root, text='Add file', font=("Ink Free Reaular", 12), width = 10, bg='khaki1')
button_play = Button(root, text='▶', width = 8, bg='plum1')
button_pause = Button(root, text='⏸', width = 8, bg='plum1')
button_next = Button(root, text='⏭️', width = 8, bg='plum1')
button_previous = Button(root, text='⏮️', width = 8, bg='plum1')
button_random = Button(root, text='⚅ Randomsong', width = 16, bg='aquamarine')
button_repeat = Button(root, text='🔁 Repeat', width = 16, bg='aquamarine') 
button_addsound = Button(root, text='🔊', width = 6, height=1, bg='cornflowerblue') #เพิ่มเสียง
button_subsound = Button(root, text='🔉', width = 6, height=1, bg='cornflowerblue') #ลดเสียง

#แสดงผล
first_line.grid(row=0, column=0, columnspan=4)
second_line.grid(row=1, column=0, columnspan=4)
button_addfile.grid(row=2, column=1, columnspan=2, pady=10)
txt_addfile = Label(root, text='<< choose a song', font=("Ink Free Reaular", 12), bg='MediumPurple1')
txt_addfile.grid(row=2, column=2, columnspan=3)

button_previous.grid(row=3, column=0, pady = 10)
button_play.grid(row=3, column=1, pady = 10)
button_pause.grid(row=3, column=2, pady = 10)
button_next.grid(row=3, column=3, pady = 10)
button_random.grid(row=4, column=0, columnspan=2, pady = 20)
button_repeat.grid(row=4, column=2, columnspan=3, pady = 20)
row5 = Frame(root)
row5.grid(row=5, column=0, columnspan=4)
Label(row5, text='Volume🎵', bg='MediumPurple1').pack()
button_subsound.grid(row=6, column=1, pady=5)
button_addsound.grid(row=6, column=2, pady=5)

root.mainloop()