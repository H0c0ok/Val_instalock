from tkinter import *
import main
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")


def button1_click():
    agent = Option_Menu_1.get()
    if main.main(agent) == "True":
        root = Tk()
        root.configure(bg='#242424', highlightcolor='#FFF700')
        root.geometry("200x100")
        root.title("System")
        label3 = Label(root, text="Successful picked", bg='#242424', fg="#FFCD00")
        label3.pack(padx=10)
    elif main.main(agent) == "Time":
        root = Tk()
        root.configure(bg='#242424', highlightcolor='#FFF700')
        root.geometry("200x100")
        root.title("System")
        label3 = Label(root, text="Time error", bg='#242424', fg="#FFCD00")
        label3.pack(padx=10)
    window.destroy()


def button2_click():
    window.destroy()


def on_select_label1(event):
    label1.config(text=event)


window = Tk()
window.geometry("300x300")
window.title("Valorant picker")
window.configure(bg='#242424', highlightcolor='#FFF700')

mas_agents = ['brimstone', 'phoenix', 'sage', 'sova', 'viper', 'cypher',
              'reyna', 'killjoy', 'breach', 'omen', 'jett', 'raze',
              'skye', 'yoru', 'astra', 'kayo', 'chamber', 'neon',
              'fade', 'harbor', 'gekko', 'deadlock']

Option_Menu_1 = customtkinter.CTkOptionMenu(window, values=mas_agents, command=on_select_label1)
Option_Menu_1.pack(side=LEFT)
Option_Menu_1.set("Choose agent")

button1 = customtkinter.CTkButton(master=window, text="Pick and close", command=button1_click, width=50, height=50)
button1.pack()
button2 = customtkinter.CTkButton(master=window, text="close", command=button2_click, width=50, height=50)
button2.pack()

label = Label(window, text="Choosing...", bg='#242424', fg="#FFCD00")
label.pack()
label1 = Label(window, text="Select", bg='#242424', fg="#FFD940")
label1.pack()

window.mainloop()
