import numpy as np
import tkinter as tk  # Built in GUI
from tkinter import messagebox  # pop-up window

def click_button(ev):
    try:
        r, c = map(int, en_row_column.get().split())  # spacebar
        matrix = np.random.randint(1, 101, size=(r, c))
        lbl_result.config(text=matrix)
    except ValueError as err:
        messagebox.showerror('Error!', f"입력 값이 없습니다.\n{err}")


window = tk.Tk()
window.title('numpy gui version v1.5')
window.geometry('300x150')

# create widget
lbl_result = tk.Label(text="random numpy 2d array")
en_row_column = tk.Entry()
btn_click = tk.Button(text="click me!", command=click_button)

lbl_result.pack()
en_row_column.pack(fill='x')
btn_click.pack(fill='x')

en_row_column.bind("<Return>", click_button)

window.mainloop()