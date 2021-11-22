# Base file
# Import the GUI base file
from Core.GUI.base import *

# Define the message holder
message = StringVar()


# Clear message
def clear_string():
    message.set("")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    gui = draw_window(message, clear_string)
    gui.mainloop()
