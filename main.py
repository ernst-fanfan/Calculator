# SMYT STEM
# Ernst R Fanfan
# 7/21/2021

import gui as g
from operations import Operations

# initializing
EVENT_LIST = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "/", "-", "+", "x"]


# init gui
VIEW = None
WINDOW = g.gui_init()
background_processes = Operations()

# event loop
while True:
    event, values = WINDOW.read()
    if g.is_closed(event):
        break

    # event processor
    if event in EVENT_LIST:
        VIEW = background_processes.update_view(event)
        g.update_display(WINDOW, VIEW)

WINDOW.close()
