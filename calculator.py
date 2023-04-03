#Name - Gunaditya Patil
#Date - 02/04/2023
#Single Day Project - GUI Calculator using Python

import tkinter as tk        #impoting tkinter which is the GUI of Python

answer = ""                 #creating a variable that will give output


def add_to_answer(symbol):
    global answer                           #to manipulate inside the function
    answer += str(symbol)                   #the end will always be a string
    text_result.delete(1.0, "end")          #1.0 is start and "end" is end
    text_result.insert(1.0, answer)         #to the answer string adds whatever new stuff we input

def evaluate_answer():
    global answer
    try:
         answer = str(eval(answer))         #eval function evaluates whatever is given input as string
                                            #major drawback is safety as eval can evaluate code
                                            #someone can inject a code that can harm your application or files
         text_result.delete(1.0, "end")
         text_result.insert(1.0, answer)
    except:
             clear_field()
             text_result.insert(1.0, "Error")       #will give error in imposible arithematics, for example divided by 0

def clear_field():
    global answer
    answer = ""
    text_result.delete(1.0, "end")         #will clear the input field
             

 
main = tk.Tk()                  #creates a main window of the application
main.geometry("520x335")        #gives dimensions to the gui

text_result = tk.Text(main, height=3, width=30, font=("Calibri", 25))               #creating a text input part of the GUI
text_result.grid(columnspan=5)

btn1 = tk.Button(main, text="1", width=12, font=("Calibri", 15), command=lambda: add_to_answer(1))          #creates a button
btn1.grid(row=2, column=1)                                                                                  #specifies the position of button
btn2 = tk.Button(main, text="2", width=12, font=("Calibri", 15), command=lambda: add_to_answer(2))
btn2.grid(row=2, column=2)
btn3 = tk.Button(main, text="3", width=12, font=("Calibri", 15), command=lambda: add_to_answer(3))
btn3.grid(row=2, column=3)
btnadd = tk.Button(main, text="+", width=12, font=("Calibri", 15), command=lambda: add_to_answer("+"))
btnadd.grid(row=2, column=4)
btn4 = tk.Button(main, text="4", width=12, font=("Calibri", 15), command=lambda: add_to_answer(4))
btn4.grid(row=3, column=1)
btn5 = tk.Button(main, text="5", width=12, font=("Calibri", 15), command=lambda: add_to_answer(5))
btn5.grid(row=3, column=2)
btn6 = tk.Button(main, text="6", width=12, font=("Calibri", 15), command=lambda: add_to_answer(6))
btn6.grid(row=3, column=3)
btnsub = tk.Button(main, text="-", width=12, font=("Calibri", 15), command=lambda: add_to_answer("-"))
btnsub.grid(row=3, column=4)
btn7 = tk.Button(main, text="7", width=12, font=("Calibri", 15), command=lambda: add_to_answer(7))
btn7.grid(row=4, column=1)
btn8 = tk.Button(main, text="8", width=12, font=("Calibri", 15), command=lambda: add_to_answer(8))
btn8.grid(row=4, column=2)
btn9 = tk.Button(main, text="9", width=12, font=("Calibri", 15), command=lambda: add_to_answer(9))
btn9.grid(row=4, column=3)
btnmul = tk.Button(main, text="*", width=12, font=("Calibri", 15), command=lambda: add_to_answer("*"))
btnmul.grid(row=4, column=4)
btnpar1 = tk.Button(main, text="(", width=12, font=("Calibri", 15), command=lambda: add_to_answer("("))
btnpar1.grid(row=5, column=1)
btn0 = tk.Button(main, text="0", width=12, font=("Calibri", 15), command=lambda: add_to_answer(0))
btn0.grid(row=5, column=2)
btnpar2 = tk.Button(main, text=")", width=12, font=("Calibri", 15), command=lambda: add_to_answer(")"))
btnpar2.grid(row=5, column=3)
btndiv = tk.Button(main, text="/", width=12, font=("Calibri", 15), command=lambda: add_to_answer("/"))
btndiv.grid(row=5, column=4)
btnclr = tk.Button(main, text="CE", width=25, font=("Calibri", 15), command=clear_field)
btnclr.grid(row=6, column=1, columnspan=2)
btndot = tk.Button(main, text=".", width=12, font=("Calibri", 15), command=lambda: add_to_answer("."))
btndot.grid(row=6, column=3)
btneql = tk.Button(main, text="=", width=12, font=("Calibri", 15), command=evaluate_answer)
btneql.grid(row=6, column=4)

main.mainloop()         #creates a main loop which runs an infinite loop till the window is closed