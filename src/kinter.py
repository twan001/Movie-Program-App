import Tkinter as tk 
from Tkinter import *
import main as m
TIMES = [
	"12:00",
	"1:00",
	"2:00",
	"3:00",
	"4:00",
	"5:00",
	"6:00",
	"7:00",
	"8:00",
	"9:00",
	"10:00",
	"11:00"
]

AP = [
	"AM",
	"PM"
]
HEIGHT = 700
WIDTH = 800

def find_movie(mov, zip_code, start_time, am_pm_0, end_time, am_pm_1 ):
	top = tk.Toplevel()


	empty_movie = False
	empty_zip_code = False
	if(mov == ""):
		label1 = Label(top, text="Please enter a valid movie")
		empty_movie = True
		label1.pack()
	# else:
	# 	label1 = Label(top, text= "The movie selected is " +  str(mov))
	# 	label1.pack()

	if(zip_code == ""):
	    label0 = Label(top, text= "Please enter a correct zip code")
	    empty_zip_code = True
	    label0.pack()
	# else:
	#     label0 = Label(top, text= "The zip code is " +  str(zip_code))
	#     label0.pack()

	if(empty_movie == False and empty_movie == False):
		print("Here")
		print(start_time)
		output = m.find_times((str(mov)).upper(),int(zip_code),(start_time+am_pm_0),\
			(end_time+am_pm_1))
		display_output(output, top)


def display_output(output,top):
	print(output)
	for k in output:
		label1 = Label(top,text=k)
		label1.pack()
		for i in output[k]:
			label1=Label(top,text=i)
			label1.pack()
		# return mov, zip_code, start_time, am_pm_0, end_time, am_pm_1




def create_interface():
	root = tk.Tk()

	canvas = tk.Canvas(root,height=HEIGHT,width=WIDTH,bg='black')
	
	canvas.pack()


	frame = tk.Frame(root, bg='#80c1ff')
	frame.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.8)


	Label(frame, padx=10, pady=5, text='Movie',font=(None, 25),bg='#80c1ff',fg='white').grid(row=0,column=0) 
	Label(frame, pady=5,text='Zip Code',font=(None, 25),bg='#80c1ff',fg='white').grid(row=1,column=0) 


	e1 = Entry(frame,width=100) 
	e2 = Entry(frame,width=100)


	e1.grid(row=0, column=1) 
	e2.grid(row=1, column=1) 


	frame1 = tk.Frame(frame, bg='#80c1ff')
	frame1.place(relx=0.001,rely=0.2,relwidth=0.5,relheight=0.1)

	frame2 = tk.Frame(frame, bg='#80c1ff')
	frame2.place(relx=0.5,rely=0.2,relwidth=0.5,relheight=0.1)

	# start time drop down menu
	Label(frame1,text="Start Time: ", font=(None,25),bg='#80c1ff',fg='white').grid(row=0,column=0)
	start_time = StringVar(root)
	start_time.set(TIMES[0])

	start_time_w = OptionMenu(frame1, start_time, *TIMES)
	start_time_w.grid(row=0,column=1)
	start_time_w.configure(bg='#80c1ff')

	am_pm_0 = StringVar(root)
	am_pm_0.set(AP[0])

	am_pm_0_w = OptionMenu(frame1, am_pm_0, *AP)
	am_pm_0_w.configure(bg='#80c1ff')
	am_pm_0_w.grid(row=0,column=2)
	# start time drop down menu


	# end time drop down menu
	Label(frame2,text="End Time: ", font=(None,25),bg='#80c1ff',fg='white').grid(row=0,column=1)

	end_time = StringVar(root)
	end_time.set(TIMES[0]) 

	end_time_w = OptionMenu(frame2, end_time, *TIMES)
	end_time_w.grid(row=0,column=2)
	end_time_w.configure(bg='#80c1ff')

	am_pm_1 = StringVar(root)
	am_pm_1.set(AP[0])

	am_pm_1_w = OptionMenu(frame2, am_pm_1, *AP)
	am_pm_1_w.grid(row=0,column=3)
	am_pm_1_w.configure(bg='#80c1ff')
	# # end time drop down menu

	# # # ,command=lambda:print_e(e1.get(),e2.get())
	submit_button = tk.Button(frame1, text='Find',highlightbackground='#80c1ff',command=lambda:find_movie(e1.get(),e2.get(),\
		start_time.get(), am_pm_0.get(), end_time.get(), am_pm_1.get()))
	submit_button.grid(row=2,column=1)


	root.mainloop()

def main():
	create_interface()

if __name__ == "__main__":
	main()
