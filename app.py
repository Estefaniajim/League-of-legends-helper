import tkinter as tk

def delete():
    screen1.destroy()
    screen3.destroy()

def user():
    SN = name_entry.get()
    Pos = Pos_entry.get()
    Ser = Ser_entry.get()
    name_entry.delete(0, tk.END)
    Pos_entry.delete(0, tk.END)
    Ser_entry.delete(0, tk.END)
    login_sucess()
    return SN,Pos,Ser

def login_sucess():
    global screen3
    screen3 = tk.Toplevel(screen)
    screen3.title("Success")
    screen3.geometry("150x100")
    tk.Label(screen3, text="Login Sucess").pack()
    tk.Button(screen3, text="OK", command=delete).pack()

def login():
    global screen1
    screen1 = tk.Toplevel(screen)
    screen1.title("Login")
    screen1.geometry("300x250")

    global SN,Pos,Ser
    SN = tk.StringVar()
    Pos = tk.StringVar()
    Ser = tk.StringVar()

    tk.Label(screen1, text="Enter your info").pack()
    tk.Label(screen1, text="").pack()

    global name_entry, Ser_entry,Pos_entry
    tk.Label(screen1,text="Summoner Name").pack()
    name_entry = tk.Entry(screen1,textvariable = SN)
    name_entry.pack()

    tk.Label(screen1,text="Position").pack()
    Pos_entry = tk.Entry(screen1,textvariable = Pos)
    Pos_entry.pack()

    tk.Label(screen1,text="Server").pack()
    Ser_entry = tk.Entry(screen1,textvariable = Ser)
    Ser_entry.pack()

    tk.Button(screen1, text="Enter", width =10, height = 1,command=user).pack()
    tk.Label(screen1, text="*Remember to never give your password*").pack()


def main_screen():
    global screen
    screen = tk.Tk()
    screen.geometry("300x250")
    screen.title("League of Legends Helper")
    tk.Label(text="League of Legends Helper", bg="grey", width="300", height="2",font=("Calibre",13)).pack()
    tk.Label(text = "").pack()
    tk.Button(text="Login", height="2", width="30", command = login).pack()
    tk.Label(text="").pack()
    screen.mainloop()

main_screen()



