from tkinter import *

def buttonClick(number):
    global operator
    operator = operator + str(number)
    input_value.set(operator)

def buttonClear():
    global operator
    operator = ""
    input_value.set(operator)

def buttonEqual():
    global operator
    result = str(eval(operator))
    input_value.set(result)

main = Tk()
main.title("Calculator")

operator = ""

input_value = StringVar()

display_text = Entry(main,font=("sans-serif",20,"bold"),bd=30,textvariable=input_value,insertwidth=4,
                     bg="powder blue")
display_text.grid(columnspan=4)

#row 7 8 9 +

btn_7 = Button(main,bd=8,padx=16,
               font=("sans-serif",20,"bold"),fg="black",bg="powder blue",text=7,
               command= lambda : buttonClick(7))
btn_7.grid(row=1,column=0)

btn_8 = Button(main,bd=8,padx=16,font=("sans-serif",20,"bold"),fg="black",
               bg="powder blue",text=8,
               command= lambda : buttonClick(8))
btn_8.grid(row=1,column=1)

btn_9 = Button(main,bd=8,padx=16,font=("sans-serif",20,"bold"),fg="black",
               bg="powder blue",text=9,
               command= lambda : buttonClick(9))
btn_9.grid(row=1,column=2)

btn_add = Button(main,bd=8,padx=16,font=("sans-serif",20,"bold"),fg="black",bg="powder blue",text="+",
                 command= lambda : buttonClick('+'))
btn_add.grid(row=1,column=3)

#row 4 5 6 -

btn_4 = Button(main,bd=8,padx=16,font=("sans-serif",20,"bold"),
               fg="black",bg="powder blue",text=4,
               command= lambda : buttonClick(4))
btn_4.grid(row=2,column=0)

btn_5 = Button(main,bd=8,padx=16,font=("sans-serif",20,"bold"),
               fg="black",bg="powder blue",text=5,command= lambda : buttonClick(5))
btn_5.grid(row=2,column=1)

btn_6 = Button(main,bd=8,padx=16,font=("sans-serif",20,"bold"),fg="black",bg="powder blue",text=6,
               command= lambda : buttonClick(6))
btn_6.grid(row=2,column=2)

btn_sub = Button(main,bd=8,padx=16,font=("sans-serif",20,"bold"),fg="black",bg="powder blue",text="-",
                 command= lambda : buttonClick('-'))
btn_sub.grid(row=2,column=3)

#row 1 2 3 *

btn_1 = Button(main,bd=8,padx=16,font=("sans-serif",20,"bold"),
               fg="black",bg="powder blue",text=1,
               command= lambda : buttonClick(1))
btn_1.grid(row=3,column=0)

btn_2 = Button(main,bd=8,padx=16,font=("sans-serif",20,"bold"),fg="black",bg="powder blue",text=2,
               command= lambda : buttonClick(2))
btn_2.grid(row=3,column=1)

btn_3 = Button(main,bd=8,padx=16,font=("sans-serif",20,"bold"),
               fg="black",bg="powder blue",text=3,command= lambda : buttonClick(3))
btn_3.grid(row=3,column=2)

btn_multi = Button(main,bd=8,padx=16,font=("sans-serif",20,"bold"),fg="black",bg="powder blue",text="*",
                   command= lambda : buttonClick('*'))
btn_multi.grid(row=3,column=3)

#row 0 C = /

btn_0 = Button(main,bd=8,padx=16,
               font=("sans-serif",20,"bold"),fg="black",bg="powder blue",text=0,
               command= lambda : buttonClick(0))
btn_0.grid(row=4,column=0)

btn_Clear = Button(main,bd=8,padx=16,font=("sans-serif",20,"bold"),
               fg="black",bg="powder blue",text="C",command=buttonClear)
btn_Clear.grid(row=4,column=1)

btn_Equal = Button(main,bd=8,padx=16,font=("sans-serif",20,"bold"),fg="black",
               bg="powder blue",text="=",command=buttonEqual)
btn_Equal.grid(row=4,column=2)

btn_divide = Button(main,bd=8,padx=16,font=("sans-serif",20,"bold"),fg="black",bg="powder blue",
                 text="/",command= lambda : buttonClick('/'))
btn_divide.grid(row=4,column=3)

main.mainloop()
