"""from tkinter import *

game_width = 500
game_height = 500
snake_item = 10

tk = Tk()
tk.title("игра Змейка на Python")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=game_width, height=game_height, bd=0, highlightthickness=0)
canvas.pack()
tk.update()
tk.mainloop()"""

from tkinter import *

retry = Tk()
retry.title('Label Enable')
btn_end = Button(retry, text='close', command=exit)


def tog():
    if retry.cget('bg') == 'yellow':
        retry.configure(bg='gray')
    else:
        retry.configure(bg='yellow')


btn_tog = Button(retry, text='swith', command=tog)
btn_end.pack(padx=150, pady=20)
btn_tog.pack(padx=150, pady=20)
retry.mainloop()
