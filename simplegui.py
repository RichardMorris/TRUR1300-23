from tkinter import * 
                            # function to display welcome message, 
                            # called when button pressed
def welcome(): 
    name = text_box1.get(1.0, END)  # gets the text from first text box
    text_box2.delete(1.0, END)      # clear second text box
    text_box2.insert(END, "Welcome " + name) # set the text of second text box

root = Tk()                 # Creates the Tk main window object 
root.geometry("200x150")    # sets the size
frame = Frame(root)         # Creates a Frame that allows multiple object to be added
frame.pack()                # Fit the frame in the root

                            # Create a Label object
label = Label(frame, text = "Enter your name:")
label.pack()
                            # Create a text box object
text_box1 = Text(frame, height = 1, width = 10)
text_box1.pack()
                            # Create a button object
button = Button(frame, text = "Welcome", command = welcome)
button.pack()
                            # Create second text box object
text_box2 = Text(frame, height = 1, width = 20)
text_box2.config(font=("Arial", 20)) # Set the font
text_box2.pack()

root.mainloop()