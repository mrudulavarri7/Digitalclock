from tkinter import *
import time

def update_clock():
    current_time = time.strftime("%H:%M:%S")
    hour, minute, second = current_time.split(':')

    if int(hour) > 12:
        hour = str(int(hour) - 12)
        lb_dn.config(text="PM")
    else:
        lb_dn.config(text="AM")

    lb_hr.config(text=hour)
    lb_mn.config(text=minute)
    lb_sc.config(text=second)

    clk.after(1000, update_clock) # Update clock every second

clk = Tk()
clk.title("Clock")
clk.geometry("1350x700+0+0") # Width, height, x-axis, y-axis

# Background color (consider using hex code for consistency)
clk.config(bg="#0C1E28")

font_style = ("Times New Roman", 75, "bold") # Consistent font

lb_hr = Label(clk, text="12", font=font_style, bg="#0875B7", fg="white")
lb_hr.place(x=350, y=200, width=150, height=150)

lb_hr_txt = Label(clk, text="HOUR", font=("Times New Roman", 20, "bold"), bg="#0875B7", fg="white")
lb_hr_txt.place(x=350, y=360, width=150, height=50)

lb_mn = Label(clk, text="00", font=font_style, bg="#008EA4", fg="white")
lb_mn.place(x=520, y=200, width=150, height=150)

lb_mn_txt = Label(clk, text="MINUTE", font=("Times New Roman", 20, "bold"), bg="#008EA4", fg="white")
lb_mn_txt.place(x=520, y=360, width=150, height=50)

lb_sc = Label(clk, text="00", font=font_style, bg="#06B4B8", fg="white")
lb_sc.place(x=690, y=200, width=150, height=150)

lb_sc_txt = Label(clk, text="SECOND", font=("Times New Roman", 20, "bold"), bg="#06B4B8", fg="white")
lb_sc_txt.place(x=690, y=360, width=150, height=50)

lb_dn = Label(clk, text="AM", font=("Times New Roman", 70, "bold"), bg="#9F0646", fg="white")
lb_dn.place(x=860, y=200, width=150, height=150)

lb_dn_txt = Label(clk, text="NOON", font=("Times New Roman", 20, "bold"), bg="#9F0646", fg="white")
lb_dn_txt.place(x=860, y=360, width=150, height=50)

update_clock() # Call the update function initially
clk.mainloop()
