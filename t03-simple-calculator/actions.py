from tkinter import *

main_text = StringVar()
main_text.set('0')

# Actions
def add_1():
    global main_text
    main_text.set(main_text.get() + '1' if main_text.get() != '0' else '1')
def add_2():
    global main_text
    main_text.set(main_text.get() + '2' if main_text.get() != '0' else '2')
def add_3():
    global main_text
    main_text.set(main_text.get() + '3' if main_text.get() != '0' else '3')
def add_4():
    global main_text
    main_text.set(main_text.get() + '4' if main_text.get() != '0' else '4')
def add_5():
    global main_text
    main_text.set(main_text.get() + '5' if main_text.get() != '0' else '5')
def add_6():
    global main_text
    main_text.set(main_text.get() + '6' if main_text.get() != '0' else '6')
def add_7():
    global main_text
    main_text.set(main_text.get() + '7' if main_text.get() != '0' else '7')
def add_8():
    global main_text
    main_text.set(main_text.get() + '8' if main_text.get() != '0' else '8')
def add_9():
    global main_text
    main_text.set(main_text.get() + '9' if main_text.get() != '0' else '9')
def add_0():
    global main_text
    if main_text.get() != '0':
        main_text.set(main_text.get() + '0')
def add_point():
    global main_text
    if '.' not in main_text.get():
        main_text.set(main_text.get() + '.')
def toggle_pn():
    global main_text
    main_text.set('-' + main_text.get() if '-' not in main_text.get() else main_text.get()[1:])

signs = ['+', '-', '*', '/']
def add_plus():
    global main_text
    main_text.set(main_text.get() + '+' if main_text.get()[-1] not in signs \
                   else main_text.get()[:-1] + '+')
def add_minus():
    global main_text
    main_text.set(main_text.get() + '-' if main_text.get()[-1] not in signs \
                   else main_text.get()[:-1] + '-')
def add_multiply():
    global main_text
    main_text.set(main_text.get() + '*' if main_text.get()[-1] not in signs \
                   else main_text.get()[:-1] + '*')
def add_divide():
    global main_text
    main_text.set(main_text.get() + '/' if main_text.get()[-1] not in signs \
                   else main_text.get()[:-1] + '/')
    
def _calculate(left, sign, right):
    if sign == "+":
        return int(left) + int(right)
    if sign == "-":
        return int(left) - int(right)
    if sign == "*":
        return int(left) * int(right)
    if sign == "/":
        return int(left) / int(right)

def calculate():
    global main_text
    equation = main_text.get()
    
    # first, find the location of multiplications and divisions along with all signs
    signs_idx = []
    level1_idx = []
    for i in range(len(equation)):
        if equation[i] in signs :
            signs_idx.append(i)
        if equation[i] == "*" or equation[i] == "/" :
            level1_idx.append(i)

    # handle for no signs
    if len(signs_idx) == 0 :
        return

    # handle in case of only 1 sign
    if len(signs_idx) == 1 :
        sign = equation[signs_idx[0]]
        eq = equation.split(sign)
        main_text.set(str(_calculate(eq[0], sign, eq[1])))
        return

    # # if found, calculate the neighboring values using the corresponding sign
    # if len(level1_idx) > 0 :
    #     for idx in level1_idx:
            