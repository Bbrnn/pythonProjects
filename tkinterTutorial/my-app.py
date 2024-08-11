import tkinter as tk

def say_hello():
    label.config(text="Hello, tkinter")


#Create the main window
root = tk.Tk()
root.title("My First GUI App")

#Create widgets
label = tk.Label(root, text = "Click the button")
button = tk.Button(root, text = "Click me", command=say_hello)


#Pack or Grid widgets
#Arrange widgets in the main window
label.pack(pady=10)
button.pack(pady=10)

#CHANGING THE BACKGROUND COLOR
#STYLE THE WINDOW
root.configure(bg="purple")
label.configure(bg="yellow")
button.configure(bg="blue", fg ="white")

#Run the application

root.mainloop()