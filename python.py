from tkinter import *
from PIL import ImageTk, Image


def Course():
    op = Toplevel(root)
    op.title("Course Options")
    op.geometry('250x250')

    olabel = Label(op, text="Select a course:")
    olabel.pack()

    options = ["Software Developer", "Java", "Python", "Full Stack", "CADD"]

    selected_course = StringVar()
    selected_course.set(options[0])

    options_menu = OptionMenu(op, selected_course, *options)
    options_menu.pack()

    def submit_c():
        selected_course_value = selected_course.get()
        print(f"Selected course: {selected_course_value}")
        op.destroy()

    submit_button = Button(op, text="Submit", command=submit_c)
    submit_button.pack()




def Webinar():
    op = Toplevel(root)
    op.title("Upcoming Webinars")
    op.geometry('600x800')
    wpic = ImageTk.PhotoImage(Image.open("/Users/rahulg/Desktop/G/py pro/webi pic.png"))
    l = Label(op, image=wpic)
    l.pack()
    l.image = wpic

    wlabel = Label(op,text = "To register, contact Rahul - 9840979176 ")
    wlabel.pack()


def Internships():
    op = Toplevel(root)
    op.title("Internships")
    op.geometry('250x250')

    ilabel = Label(op, text= "ENQUIRE NOW", font = (" Times New Roman ", 14) )
    ilabel.pack()

    e1 = Entry(op, width = 20, bg = "light yellow")
    e1.insert(0, "Name: " )
    e1.pack()

    e2 = Entry(op, width = 20, bg = "light yellow")
    e2.insert(0, "Email ID: " )
    e2.pack()


    e3 = Entry(op, width = 20, bg = "light yellow")
    e3.insert(0, "Phone No.: " )
    e3.pack()

    

    def submit_c():
        intern_info = e1.get(), e2.get(), e3.get()
        print(f"Internship Participant Info: {intern_info} ")
        op.destroy()

    submit_b = Button(op, text="Submit", command=submit_c)
    submit_b.pack()
    



root = Tk()
root.title("OC")
root.geometry('1000x1000')
root.iconbitmap('rgx icon.png')


logo = ImageTk.PhotoImage(Image.open("/Users/rahulg/Desktop/G/py pro/rgx logo.png"))
l = Label(image=logo)
l.grid(row=1, column=1)


course = Button(root, text="Course", command = Course)
webinar = Button(root, text="Webinar", command = Webinar)
internship = Button(root, text="Internships", command = Internships)
contact = Button(root, text="Contacts")
login = Button(root, text="Student Login")

course.grid(row=1, column=3, pady=10)
webinar.grid(row=1, column=4, pady=10)
internship.grid(row=1, column=5, pady=10)
contact.grid(row=1, column=6, pady=10)
login.grid(row=1, column=7, pady=10)



slide1 = ImageTk.PhotoImage(Image.open("slide1.png"))
slide2 = ImageTk.PhotoImage(Image.open("slide2.png"))
slide3 = ImageTk.PhotoImage(Image.open("slide3.png"))

slidelist = [slide1, slide2, slide3]

s = Label(image=slide1)
s.grid(row=3, column=1, columnspan=7)

current_index = 0

def next_image():
    global current_index
    if slidelist:
        current_index = (current_index + 1) % len(slidelist)
        load_image()

def prev_image():
    global current_index
    if slidelist:
        current_index = (current_index - 1) % len(slidelist)
        load_image()

def load_image():
    s.configure(image=slidelist[current_index])
    s.image = slidelist[current_index]

backB = Button(root, text="<<", command=prev_image)
frontB = Button(root, text=">>", command=next_image)

backB.grid(row=4, column=1)
frontB.grid(row=4, column=7)



partpic = ImageTk.PhotoImage(Image.open("pypro pic.png"))
p = Label(image=partpic)
p.grid(row=6, column= 1, columnspan=7)

tpic = ImageTk.PhotoImage(Image.open("pypro pic2.png"))
t = Label(image=tpic)
t.grid(row=7, column= 1, columnspan=7)


root.mainloop()
