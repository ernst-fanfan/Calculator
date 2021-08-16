# SMYT STEM
# Ernst R Fanfan
# 8/6/2021
import PySimpleGUI as Sg
from parserOperations import Parser


class Gui:
    window = None
    event = ""
    value = None
    display = ""

    def __init__(self):
        width = 5
        height = 2
        size = (width, height)

        # row 1
        # display and AC
        display = [
            [
                Sg.In(size=(28, height), key="-DISPLAY-"), Sg.Button(button_text="AC", size=size)
            ]
        ]

        # row 2
        # create first column
        first_column = [
            [Sg.Button(button_text="7", size=size)],
            [Sg.Button(button_text="4", size=size)],
            [Sg.Button(button_text="1", size=size)],
            [Sg.Button(button_text="0", size=size)],
        ]

        # create second column
        second_column = [
            [Sg.Button(button_text="8", size=size)],
            [Sg.Button(button_text="5", size=size)],
            [Sg.Button(button_text="2", size=size)],
            [Sg.Button(button_text=".", size=size)],
        ]

        # create third column
        third_column = [
            [Sg.Button(button_text="9", size=size)],
            [Sg.Button(button_text="6", size=size)],
            [Sg.Button(button_text="3", size=size)],
            [Sg.Button(button_text="=", size=size, button_color="red")],
        ]

        # create four column
        fourth_column = [
            [Sg.Button(button_text="/", size=size)],
            [Sg.Button(button_text="x", size=size)],
            [Sg.Button(button_text="-", size=size)],
            [Sg.Button(button_text="+", size=size)],
        ]

        # ----full layout------
        layout = [
            [
                display
            ],
            [
                Sg.HSeparator(),
            ],
            [
                Sg.Column(first_column),
                Sg.Column(second_column),
                Sg.Column(third_column),
                Sg.Column(fourth_column)
            ]
        ]

        # -----build window
        self.window = Sg.Window("SMYT Calculator", layout=layout)

    # Setters
    def read_click(self):
        self.event, self.value = self.window.read()
        self.process_click()

    # Getters
    def get_event(self):
        return self.event

    def get_value(self):
        return self.value

    def get_window(self):
        return self.window

    # methods
    def is_closed(self):
        return self.event == "Exit" or self.event == Sg.WIN_CLOSED

    def update_display(self):
        self.window["-DISPLAY-"].update(self.display)

    def close(self):
        self.window.close()

    def process_click(self):
        switcher = {"AC": self.clear_display, "=": self.get_result, "Exit": self.close, Sg.WIN_CLOSED: self.close,
                    "-": self.operator, "+": self.operator, "x": self.operator,
                    "/": self.operator}

        # call code associated to the event or add to command stack
        func = switcher.get(self.event, self.stack)
        func()

    def clear_display(self):
        self.display = ""

    # get result based on stack
    def get_result(self):
        parser = Parser()
        if not self.operator_check(): self.display = parser.parse(self.display)
        self.update_display()

    # stack events
    def stack(self):
        self.display += self.event

    # check if last event was an operator
    def operator_check(self):
        operators = ["-", "+", "x", "/"]
        if self.display[-1] in operators: return True
        return False

    # process operator event
    def operator(self):
        if not self.operator_check(): self.stack()
