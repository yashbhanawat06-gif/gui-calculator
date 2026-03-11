import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.geometry("400x450") 

display = tk.Entry(root, 
                   width=20, 
                   borderwidth=5, 
                   font=("Arial", 24), 
                   justify="right",
                   bg="#2d2d2d",
                   fg="white",
                   )

display.grid(row=0, 
             column=0, 
             columnspan=5, 
             padx=10, 
             pady=10)


def click(number):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, str(current) + str(number))

button1 = tk.Button(root,text="1",width=5,height=2,font=("Arial",14), bg="#3a3a3a", fg="white", command=lambda: click(1))
button2 = tk.Button(root,text="2",width=5, height=2,font=("Arial",14), bg="#3a3a3a", fg="white", command=lambda: click(2))
button3 = tk.Button(root,text="3",width=5, height=2,font=("Arial",14), bg="#3a3a3a", fg="white",command=lambda: click(3))
button4 = tk.Button(root,text="4",width=5, height=2,font=("Arial",14), bg="#3a3a3a", fg="white",command=lambda: click(4))
button5 = tk.Button(root,text="5",width=5, height=2,font=("Arial",14), bg="#3a3a3a", fg="white",command=lambda: click(5))
button6 = tk.Button(root,text="6",width=5, height=2,font=("Arial",14), bg="#3a3a3a", fg="white",command=lambda: click(6))
button7 = tk.Button(root,text="7",width=5, height=2,font=("Arial",14), bg="#3a3a3a", fg="white",command=lambda: click(7))
button8 = tk.Button(root,text="8",width=5, height=2,font=("Arial",14), bg="#3a3a3a", fg="white",command=lambda: click(8))
button9 = tk.Button(root,text="9",width=5, height=2,font=("Arial",14), bg="#3a3a3a", fg="white",command=lambda: click(9))
button0 = tk.Button(root,text="0",width=5, height=2,font=("Arial",14), bg="#3a3a3a", fg="white",command=lambda: click(0))
button_add = tk.Button(root,text="+",width=5, height=2,font=("Arial",14), bg="#3a3a3a", fg="white",command=lambda: click("+"))
button_sub = tk.Button(root,text="-",width=5, height=2,font=("Arial",14), bg="#3a3a3a", fg="white",command=lambda: click("-"))
button_mul = tk.Button(root,text="*",width=5, height=2,font=("Arial",14), bg="#3a3a3a", fg="white",command=lambda: click("*"))
button_div = tk.Button(root,text="/",width=5, height=2,font=("Arial",14), bg="#3a3a3a", fg="white",command=lambda: click("/"))
button_dot = tk.Button(root,text=".",width=5,height=2,font=("Arial",14), bg="#3a3a3a", fg="white", command=lambda: click("."))
button_percent = tk.Button(root, text="%",width=5,height=2,font=("Arial",14), bg="#3a3a3a", fg="white", command=lambda: click("%")) 


button1.grid(row=5, column=0, padx=5,pady=5) 
button2.grid(row=5, column=1, padx=5,pady=5)
button3.grid(row=5, column=2, padx=5,pady=5)
button4.grid(row=4, column=0, padx=5,pady=5)
button5.grid(row=4, column=1, padx=5,pady=5)
button6.grid(row=4, column=2, padx=5,pady=5)
button7.grid(row=3, column=0, padx=5,pady=5)
button8.grid(row=3, column=1, padx=5,pady=5)
button9.grid(row=3, column=2, padx=5,pady=5)
button0.grid(row=6, column=1, padx=5,pady=5)
button_add.grid(row=6, column=4, padx=5,pady=5)
button_div.grid(row=3, column=4, padx=5,pady=5)
button_mul.grid(row=4, column=4, padx=5,pady=5)
button_sub.grid(row=5, column=4, padx=5,pady=5)
button_dot.grid(row=7,column=0,padx=5,pady=5)
button_percent.grid(row=7,column=1,padx=5,pady=5)



def calculate():
    result = eval(display.get())
    display.delete(0, tk.END)
    display.insert(0, result)

def backspace():
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current[:-1])

button_back = tk.Button(root,text="⌫",width=5,height=2,font=("Arial",14),bg="#3a3a3a", fg="white", command=backspace)

button_equal = tk.Button(root, text="=", width=5, height=2, font=("Arial",14),bg="#3a3a3a", fg="white", command=calculate)
def clear():
    display.delete(0, tk.END)
button_clear = tk.Button(root, text="C", width=5, height=2, font=("Arial",14),bg="#3a3a3a", fg="white", command=clear)
button_back.grid(row=7, column=2, padx=5, pady=5)

button_equal.grid(row=6, column=2)
button_clear.grid(row=6, column=0)

def square():
    result = float(display.get()) ** 2
    display.delete(0, tk.END)
    display.insert(0, result)

button_square = tk.Button(root,text="x²",width=5,height=2,font=("Arial",14), bg="#3a3a3a", fg="white", command=square)
button_square.grid(row=7, column=4)
root.mainloop()
