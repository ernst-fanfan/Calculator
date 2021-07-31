# SMYT STEM
# Ernst R Fanfan
# 7/30/2021

from gui import Gui

# init gui
gui = Gui()

# event loop
while not gui.is_closed():
    gui.read_click()
    gui.update_display()
else:
    gui.close()
