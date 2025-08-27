import tkinter as tk

root = tk.Tk()
root.title('Calculadora')
root.geometry('350x500')
root.configure(bg = 'black')

for r in range(9):
    root.grid_rowconfigure(r, weight = 1)

for c in range(6):
    root.grid_columnconfigure(c, weight = 1)

display_var = tk.StringVar(value = '0')

display = tk.Entry(
                    root, 
                    font=('Arial', 15), 
                    justify = 'right', 
                    textvariable = display_var, 
                    bd = 0, 
                    relief = 'flat', 
                    state = 'readonly', 
                    readonlybackground = 'white', 
                    fg = 'black', 
                    highlightthickness = 0, 
                    insertwidth = 0
                    )

display.grid(
            row = 0, 
            column = 0, 
            columnspan = 6, 
            sticky = tk.NSEW, 
            padx = 8, 
            pady = 8
            )

filas = [
        ["MC", "MR", "M+", "M-", "MS", "M"],
        ["2nd", "Grad", "Rad", "n!", "(", ")"],
        ["Inv", "sen", "cos", "tan", "ln", "log"],
        ["π", "e", "√", "x²", "x^y", "1/x"],
        ["7", "8", "9", "÷", "AC", "⌫"],
        ["4", "5", "6", "×", "%", "×10ˣ"],
        ["1", "2", "3", "−", "Resp", "Exp"],
        ["0", "00", ",", "+", "=", "±"]
        ]

botones = [b for fila in filas for b in fila]

row_num = 1
col_num = 0

for texto in botones:
    button = tk.Button(
                        root, 
                        text = texto, 
                        font = ("Arial", 15), 
                        bg = "gray30", 
                        fg = "white", 
                        activebackground = "gray35", 
                        activeforeground = "white", 
                        relief = "ridge", 
                        bd = 1, 
                        highlightthickness = 0, 
                        padx = 0, 
                        pady = 0, 
                        takefocus = 0
                        )

    button.grid(
                row = row_num, 
                column = col_num, 
                sticky = tk.NSEW, 
                padx = 6, 
                pady = 6
                )

    col_num += 1
    if col_num > 5:
        col_num = 0
        row_num += 1

root.mainloop()