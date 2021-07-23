import NumFuntions as nf
import OperationFunctions as of
import queue


class Operations:
    first_number = None
    second_number = None
    operation_function = None
    queue = +
    event_switcher = {
        "0": nf.zerobutton,
        "1": nf.onebutton,
        "2": nf.twobutton,
        "3": nf.threebutton,
        "4": nf.fourbutton,
        "5": nf.fivebutton,
        "6": nf.sixbutton,
        "7": nf.sevenbutton,
        "8": nf.eightbutton,
        "9": nf.ninebutton,
        "+": of.add,
        "-": of.subtract,
        "x": of.multiply,
        "/": of.divide,
        "AC": of.clear
    }

    def __init__(self):
        pass

    def update_view(self, event):
        if self.queue == [] and not event.isNumber(): return None
        if

        return None
