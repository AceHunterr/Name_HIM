"""THIS FILE IS JUST FOR CODE TESTING NOTHING TO DO WITH THE PROJECT"""

from tkinter import *

window = Tk()
frame = Frame(window)
window.config(padx=100,pady=100)

def hide_test():
    b1.lower(frame)
    print("Hello")
def show_test():
    b1.lift(frame)


b1 = Button(window,text="1",width=20,height=10)
b1.grid(row=0,column=0,in_=frame)
b2 = Button(window,text="2",width=20,height=10)
b2.grid(row=1,column=0,in_=frame)

test = Button(window,text="test",command=hide_test)
test.grid(row=1,column=1,in_=frame)

test2 = Button(window,text="test2",command=show_test)
test2.grid(row=1,column=2,in_=frame)
frame.grid()

my_dict={
    "b1": b1,
    "b2": b2
}

print(my_dict)
# my_dict["b1"].config(bg="green")

window.mainloop()

# import tkinter as tk
#
# class SampleApp(tk.Tk):
#     def __init__(self, *args, **kwargs):
#         tk.Tk.__init__(self, *args, **kwargs)
#         self.frame = tk.Frame(self)
#         self.frame.pack(side="top", fill="both", expand=True)
#         self.label = tk.Label(self, text="Hello, world")
#         button1 = tk.Button(self, text="Click to hide label",
#                            command=self.hide_label)
#         button2 = tk.Button(self, text="Click to show label",
#                             command=self.show_label)
#         self.label.pack(in_=self.frame)
#         button1.pack(in_=self.frame)
#         button2.pack(in_=self.frame)
#
#     def show_label(self, event=None):
#         self.label.lift(self.frame)
#
#     def hide_label(self, event=None):
#         self.label.lower(self.frame)
#
# if __name__ == "__main__":
#     app = SampleApp()
#     app.mainloop()