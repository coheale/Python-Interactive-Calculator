import tkinter as tk
import math

calculation_result = ""

def add_to_calculation_result(symbol):
    global calculation_result
    calculation_result += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation_result)

def evaluate_calculation_result():
    global calculation_result
    try:
        calculation_result = str(round(eval(calculation_result), 5))
        # calculation_result = ""
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation_result)

    except:
        clear_field()
        text_result.insert(1.0, "Error")

# Square root function
def square_root():
    global calculation_result
    try:
        calculation_result = round(math.sqrt(eval(calculation_result)), 5)
        calculation_result = str(calculation_result)
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation_result)

    # If invalid square root, report error on screen
    except:
        clear_field()
        text_result.insert(1.0, "Error (neg sqrt)")

def clear_field():
    global calculation_result
    calculation_result = ""
    text_result.delete(1.0, "end")

root = tk.Tk()
root.title('Cody\'s Calculator')
root.geometry('270x325')

text_result = tk.Text(root, height=2, width=16, font=("Times", 24))
text_result.grid(columnspan=5)


"""
BELOW ARE THE BUTTON ASSIGNMENTS FOR THE BUTTONS
ON THE CALCULATOR
"""

button_1 = tk.Button(root, text="1", command=lambda: add_to_calculation_result(1), width=5, font=("Times", 14))
button_1.grid(row=2, column=1)

button_2 = tk.Button(root, text="2", command=lambda: add_to_calculation_result(2), width=5, font=("Times", 14))
button_2.grid(row=2, column=2)

button_3 = tk.Button(root, text="3", command=lambda: add_to_calculation_result(3), width=5, font=("Times", 14))
button_3.grid(row=2, column=3)

button_4 = tk.Button(root, text="4", command=lambda: add_to_calculation_result(4), width=5, font=("Times", 14))
button_4.grid(row=3, column=1)

button_5 = tk.Button(root, text="5", command=lambda: add_to_calculation_result(5), width=5, font=("Times", 14))
button_5.grid(row=3, column=2)

button_6 = tk.Button(root, text="6", command=lambda: add_to_calculation_result(6), width=5, font=("Times", 14))
button_6.grid(row=3, column=3)

button_7 = tk.Button(root, text="7", command=lambda: add_to_calculation_result(7), width=5, font=("Times", 14))
button_7.grid(row=4, column=1)

button_8 = tk.Button(root, text="8", command=lambda: add_to_calculation_result(8), width=5, font=("Times", 14))
button_8.grid(row=4, column=2)

button_9 = tk.Button(root, text="9", command=lambda: add_to_calculation_result(9), width=5, font=("Times", 14))
button_9.grid(row=4, column=3)

button_0 = tk.Button(root, text="0", command=lambda: add_to_calculation_result(0), width=5, font=("Times", 14))
button_0.grid(row=5, column=2)

button_left_parentheses = tk.Button(root, text="(", command=lambda: add_to_calculation_result('('), width=5, font=("Times", 14))
button_left_parentheses.grid(row=5, column=1)

button_right_parentheses = tk.Button(root, text=")", command=lambda: add_to_calculation_result(')'), width=5, font=("Times", 14))
button_right_parentheses.grid(row=5, column=3)

button_plus = tk.Button(root, text="+", command=lambda: add_to_calculation_result('+'), width=5, font=("Times", 14))
button_plus.grid(row=2, column=4)

button_minus = tk.Button(root, text="-", command=lambda: add_to_calculation_result('-'), width=5, font=("Times", 14))
button_minus.grid(row=3, column=4)

button_times = tk.Button(root, text="*", command=lambda: add_to_calculation_result('*'), width=5, font=("Times", 14))
button_times.grid(row=4, column=4)

button_divide = tk.Button(root, text="/", command=lambda: add_to_calculation_result('/'), width=5, font=("Times", 14))
button_divide.grid(row=5, column=4)

button_clear = tk.Button(root, text="C", command=clear_field, width=11, font=("Times", 14))
button_clear.grid(row=6, column=1, columnspan=2)

button_equals = tk.Button(root, text="=", command=evaluate_calculation_result, width=11, font=("Times", 14))
button_equals.grid(row=6, column=3, columnspan=2)

button_dot = tk.Button(root, text=".", command=lambda: add_to_calculation_result('.'), width=5, font=("Times", 14))
button_dot.grid(row=7, column=1)

#Square root button
button_square_root = tk.Button(root, text="sqrt", command=square_root, width=5, font=("Times", 14))
button_square_root.grid(row=7, column=2)

#Exit button
button_exit = tk.Button(root, text="EXIT", command=root.destroy, width=5, font=("Times", 14))
button_exit.grid(row=7, column=3)

root.mainloop()