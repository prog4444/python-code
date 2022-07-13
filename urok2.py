"""import calendar
c = calendar.LocaleTextCalendar(0, "Russian_Russia.1251")
print(c.formatmonth(2021, 9))"""

import tkinter

window_main = tkinter.Tk(className='Tkinter - TutorialKart', )
window_main.geometry("400x200")

button_submit = tkinter.Button(window_main, text ="Submit", activebackground='#78d6ff')

button_submit.pack()
window_main.mainloop()
