from tkinter import *
from tkinter import messagebox
from openpyxl import *
import time
import random

root = Tk()

frame = Frame(root)
frame.pack()


# ============ Setting ============

root.resizable(width = FALSE, height = FALSE)
root.geometry("600x550")
root.title("Point of Sale System")
colour = "Light Gray"


# ============ Frames ============

# Heading
top_frame = Frame(root, bg = colour, width = 600, height = 50)
top_frame.pack(side=TOP)

# Footer
footer_frame = Frame(root, bg = colour, width = 600, height = 50)
footer_frame.pack(side = BOTTOM)

# Drinks
left_frame = Frame(root, bg = colour, width = 300, height = 500)
left_frame.pack(side = LEFT)

# Result
right_frame = Frame(root, bg = colour, width = 300, height = 500)
right_frame.pack(side = RIGHT)

# ============ Quantity Calculation ============

drink = {"Drip Coffee": [0, 0], "Cappucino": [0, 0], "Latte": [0, 0], 
         "Flat White": [0, 0], "Hot Chocolate": [0, 0], "Hot Tea": [0, 0]}

def DripCoffee_p1():
	
	global drink
	global del_val
	if del_val.get() == 0 :
		drink["Drip Coffee"][1] += 1
	elif del_val.get() == 1 and drink["Drip Coffee"][1] > 0:
		drink["Drip Coffee"][1] -= 1

	entry_no_dC.delete(0, END)
	entry_no_dC.insert(0, str(drink["Drip Coffee"][1]))
	

def Cappucino_p1():
	
	global drink
	global del_val
	if del_val.get() == 0 :
		drink["Cappucino"][1] += 1

	elif del_val.get() == 1 and drink["Cappucino"][1] > 0:
		drink["Cappucino"][1] -= 1


	entry_no_Cap.delete(0, END)
	entry_no_Cap.insert(0, str(drink["Cappucino"][1]))
	
	
def Latte_p1():
	
	global drink
	global del_val
	if del_val.get() == 0 :
		drink["Latte"][1] += 1

	elif del_val.get() == 1 and drink["Latte"][1] > 0:
		drink["Latte"][1] -= 1


	entry_no_Latt.delete(0, END)
	entry_no_Latt.insert(0, str(drink["Latte"][1]))
	
def FlatWhite_p1():
	
	global drink
	global del_val
	if del_val.get() == 0 :
		drink["Flat White"][1] += 1

	elif del_val.get() == 1 and drink["Flat White"][1] > 0:
		drink["Flat White"][1] -= 1


	entry_no_FW.delete(0, END)
	entry_no_FW.insert(0, str(drink["Flat White"][1]))
	
def HotCoco_p1():

	global drink
	global del_val
	if del_val.get() == 0 :
		drink["Hot Chocolate"][1] += 1

	elif del_val.get() == 1 and drink["Hot Chocolate"][1] > 0:
		drink["Hot Chocolate"][1] -= 1


	entry_no_hC.delete(0, END)
	entry_no_hC.insert(0, str(drink["Hot Chocolate"][1]))
	
def HotTea_p1():

	global drink
	global del_val
	if del_val.get() == 0 :
		drink["Hot Tea"][1] += 1

	elif del_val.get() == 1 and drink["Hot Tea"][1] > 0:
		drink["Hot Tea"][1] -= 1

		
	entry_no_hT.delete(0, END)
	entry_no_hT.insert(0, str(drink["Hot Tea"][1]))


# ============ Total Calculation ============

total_cost = 0
pst = 0
gst = 0

drink = {"Drip Coffee": [2.15, 0], "Cappucino": [3.65, 0], 
         "Latte": [3.65, 0], "Flat White": [3.75, 0], 
         "Hot Chocolate": [2.75, 0], "Hot Tea": [2.25, 0]}

def total_cal():
	global total_cost
	global pst
	global gst
	global drink
	total_cost = (drink["Drip Coffee"][0] * drink["Drip Coffee"][1] + 
                  drink["Cappucino"][0] * drink["Cappucino"][1] +
                  drink["Latte"][0] * drink["Latte"][1] + 
                  drink["Flat White"][0] * drink["Flat White"][1] +
                  drink["Hot Chocolate"][0] * drink["Hot Chocolate"][1] 
                  + drink["Hot Tea"][0] * drink["Hot Tea"][1])

	pst = round(total_cost * 0.07, 2)
	
	gst = round(total_cost * 0.05, 2)
		
	total_cost = round(total_cost + pst + gst, 2)
	
	entry_PST.delete(0, END)
	entry_PST.insert(0, float(pst))

	entry_GST.delete(0, END)
	entry_GST.insert(0, float(gst))	
	
	entry_total.delete(0, END)
	entry_total.insert(0, float(total_cost))
	

# ============ Receipt field ============

receipt_field = Text(left_frame, width=30, height=15)
receipt_field.place(x = 20, y = 175)

def print_receipt():
	
	global drink
	global total_cost
	global pst
	global gst
	global tax
	
	
	receipt_field.delete("1.0", END)
	receipt_field.insert(END, "Beka's Coffee Shop " +" \n")
	receipt_field.insert(END, "=======================\n")
	
	
	
	for drinks, values in drink.items():
		if values[1] > 0:
			receipt_field.insert(END, str(values[1]) + " - " +drinks + " @ $" + str(values[0]) +"\n")
				
	total_cal()
	
	if total_cost == 0:
		receipt_field.insert(END, "No purchase made.\n")
	
	receipt_field.insert(END, "\n")
	receipt_field.insert(END, "Tax: " + str(float(round(pst+gst, 2))) + "\n")
	receipt_field.insert(END, "Total: " + str(total_cost) + "\n")
	receipt_field.insert(END, "=======================\n")
	receipt_field.insert(END, "Thank you for visiting! \n")
	receipt_field.insert(END, time.asctime() +"\n")
	
# ============ Reset ============

def reset_screen():
	entry_no_dC.delete(0, END)
	entry_no_Cap.delete(0, END)
	entry_no_Latt.delete(0, END)
	entry_no_FW.delete(0, END)
	entry_no_hC.delete(0, END)
	entry_no_hT.delete(0, END)
	entry_PST.delete(0, END)
	entry_GST.delete(0, END)
	entry_total.delete(0, END)
	receipt_field.delete("1.0", END)
	
	global total_cost
	global pst
	global gst
	global drink
	
	total_cost = 0
	pst = 0
	gst = 0
	drink = {"Drip Coffee": [2.15, 0], "Cappucino": [3.65, 0], 
         "Latte": [3.65, 0], "Flat White": [3.75, 0], 
         "Hot Chocolate": [2.75, 0], "Hot Tea": [2.25, 0]}
	
	
	

# ============ Drinks buttons ============

btn1 = Button(left_frame, text = "Drip Coffee", command = DripCoffee_p1)
btn1.place(x = 20, y = 15)

btn2 = Button(left_frame, text = "Cappucino", command = Cappucino_p1)
btn2.place(x = 20, y = 65)

btn3 = Button(left_frame, text = "Latte", command = Latte_p1)
btn3.place(x = 20, y = 115)

btn4 = Button(left_frame, text = "Flat White", command = FlatWhite_p1)
btn4.place(x = 110, y = 15)

btn5 = Button(left_frame, text = "Hot Chocolate", command = HotCoco_p1)
btn5.place(x = 110, y = 65)

btn6 = Button(left_frame, text = "Hot Tea", command = HotTea_p1)
btn6.place(x = 110, y = 115)


# ============ Output Right Frame ============

# Drip Coffee
label_dC = Label(right_frame, text="Drip Coffee: ")
label_dC.place(x=10, y=10)

entry_no_dC_var = StringVar()
entry_no_dC = Entry(right_frame, textvariable=entry_no_dC_var, width=5)
entry_no_dC.place(x=160, y=10)


# Cappucino
label_Cap = Label(right_frame, text="Cappucino: ")
label_Cap.place(x=10, y=35)

entry_no_Cap_var = StringVar()
entry_no_Cap = Entry(right_frame, textvariable=entry_no_Cap_var, width=5)
entry_no_Cap.place(x=160, y=35)


# Latte
label_Latt = Label(right_frame, text="Latte: ")
label_Latt.place(x=10, y=60)

entry_no_Latt_var = StringVar()
entry_no_Latt = Entry(right_frame, textvariable=entry_no_Latt_var, width=5)
entry_no_Latt.place(x=160, y=60)


# Flat White
label_FW = Label(right_frame, text="Flat White: ")
label_FW.place(x=10, y=85)

entry_no_FW_var = StringVar()
entry_no_FW = Entry(right_frame, textvariable=entry_no_FW_var, width=5)
entry_no_FW.place(x=160, y=85)


# Hot Chocolate
label_hC = Label(right_frame, text="Hot Chocolate: ")
label_hC.place(x=10, y=110)

entry_no_hC_var = StringVar()
entry_no_hC = Entry(right_frame, textvariable=entry_no_hC_var, width=5)
entry_no_hC.place(x=160, y=110)


# Hot Tea
label_hT = Label(right_frame, text="Hot Tea: ")
label_hT.place(x=10, y=135)

entry_no_hT_var = StringVar()
entry_no_hT = Entry(right_frame, textvariable=entry_no_hT_var, width=5)
entry_no_hT.place(x=160, y=135)


# PST 7%

label_PST = Label(right_frame, text="PST: ")
label_PST.place(x=10, y=180)

entry_PST = Entry(right_frame, textvariable="", width=5)
entry_PST.place(x=160, y=180)

# GST 5%

label_GST  = Label(right_frame, text="GST: ")
label_GST.place(x=10, y=205)

entry_GST = Entry(right_frame, textvariable="", width=5)
entry_GST.place(x=160, y=205)

# Cost
label_total = Label(right_frame, text="Total: ")
label_total.place(x=10, y=230)

entry_total = Entry(right_frame, textvariable="", width=5)
entry_total.place(x=160, y=230)

# ============ Footer buttons ============

quit_btn = Button(footer_frame, text = "Quit", command = frame.quit)
quit_btn.place(relx=.95, rely=.5, anchor="center")

total_btn = Button(footer_frame, text = "Total", command = total_cal)
total_btn.place(relx=.85, rely=.5, anchor="center")

payment_btn = Button(footer_frame, text = "Payment", command = print_receipt)
payment_btn.place(relx=.70, rely=.5, anchor="center")

reset_btn = Button(footer_frame, text = "Reset", command = reset_screen)
reset_btn.place(relx=.30, rely=.5, anchor="center")

del_val = IntVar()
del_cb = Checkbutton(footer_frame, text = "Check to delete", variable=del_val, onvalue=1, offvalue=0)
del_cb.place(relx=.5, rely=.5, anchor="center")

# ============ Title ============

title_label = Label(top_frame, text="beka's coffee shop", font = (0, 0,"bold"),
                     background = colour)
title_label.pack(side=LEFT)


root.mainloop()
