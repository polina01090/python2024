from tkinter import *
from tkinter import ttk

from PIL import Image, ImageTk

root = Tk()
x = int(root.winfo_screenwidth() * 0.8)  # размер  по горизонтали
y = int(root.winfo_screenheight() * 0.8)  # размер по вертикали

root.geometry('{}x{}'.format(x, y))
root.resizable(False, False)
root.title('Math train')

#  вкладки
notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True)

frame1 = Frame(notebook, width=x, height=y - int(x * 0.1), background="#D9D9D9")
frame2 = Frame(notebook, width=x, height=y, background="#D9D9D9")

frame1.pack()
frame2.pack(fill='both', expand=True)

reg_logo = Image.open("./images/reg.png")
reg_logo = reg_logo.resize((int(x * 0.19), int(y * 0.1)))
reg_logo_img = ImageTk.PhotoImage(reg_logo)

log_logo = Image.open("./images/log.png")
log_logo = log_logo.resize((int(x * 0.1), int(y * 0.1)))
log_logo_img = ImageTk.PhotoImage(log_logo)

image1 = Image.open("./images/elem1.png")
image1 = image1.resize((int(image1.size[0]), int(image1.size[1])))
test = ImageTk.PhotoImage(image1)
ttk.Label(frame1, image=test, background="#D9D9D9").place(x=0, y=0)
ttk.Label(frame2, image=test, background="#D9D9D9").place(x=0, y=0)

image2 = Image.open("./images/elem2.png")
test2 = ImageTk.PhotoImage(image2)
ttk.Label(frame1, image=test2, background="#D9D9D9").place(x=x - test2.width(), y=0)
ttk.Label(frame2, image=test2, background="#D9D9D9").place(x=x - test2.width(), y=0)

image3 = Image.open("./images/elem3.png")
test3 = ImageTk.PhotoImage(image3)
ttk.Label(frame1, image=test3, background="#D9D9D9").place(x=x - test3.width(), y=y - test3.height() - (y * 0.15))
ttk.Label(frame2, image=test3, background="#D9D9D9").place(x=x - test3.width(), y=y - test3.height() - (y * 0.15))

image4 = Image.open("./images/elem4.png")
test4 = ImageTk.PhotoImage(image4)
ttk.Label(frame1, image=test4, background="#D9D9D9").place(x=0, y=y - test4.height() - (y * 0.15))
ttk.Label(frame2, image=test4, background="#D9D9D9").place(x=0, y=y - test4.height() - (y * 0.15))

notebook.add(frame1, image=reg_logo_img)
notebook.add(frame2, image=log_logo_img)

text = Label(frame2, text="Войти", foreground="black", background="yellow", font=("JetBrains Mono", 32, "bold"))
text.place(x=image1.width + 10, y=image1.height / 2)
InpLog = Entry(frame2, font=("JetBrains Mono", 20), background="#ADC5C3", borderwidth=10, relief="ridge")
InpLog.place(x=image1.width + 10, y=image1.height, width=x * 0.275, height=y * 0.08)

InpPass = Entry(frame2, font=("JetBrains Mono", 20), background="#ADC5C3", borderwidth=10, relief="ridge")
InpPass.place(x=image1.width + 10, y=image1.height + y * 0.08 + y * 0.05, width=x * 0.275, height=y * 0.08)

SendBtn = Button(frame2)
SendBtn.place(x=image1.width + 10, y=image1.height + y * 0.08 + y * 0.2)

text2 = Label(frame1, text="Регистрация", foreground="black", background="yellow", font=("JetBrains Mono", 32, "bold"))
text2.place(x=image1.width + 10, y=image1.height / 2)
root.mainloop()
