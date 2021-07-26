import PySimpleGUI as sg


def gui_init():
    width = 5
    height = 2
    size = (width, height)

    # create display
    display = [
        [
            sg.In(size=(28, height), key="-DISPLAY-"), sg.Button(button_text="AC", size=size)
        ]
    ]

    # create first column
    first_column = [
        [sg.Button(button_text="7", size=size)],
        [sg.Button(button_text="4", size=size)],
        [sg.Button(button_text="1", size=size)],
        [sg.Button(button_text="0", size=size)],
    ]

    # create second column
    second_column = [
        [sg.Button(button_text="8", size=size)],
        [sg.Button(button_text="5", size=size)],
        [sg.Button(button_text="2", size=size)],
        [sg.Button(button_text=".", size=size)],
    ]

    # create third column
    third_column = [
        [sg.Button(button_text="9", size=size)],
        [sg.Button(button_text="6", size=size)],
        [sg.Button(button_text="3", size=size)],
        [sg.Button(button_text="=", size=size, button_color="red")],
    ]

    # create four column
    fourth_column = [
        [sg.Button(button_text="/", size=size)],
        [sg.Button(button_text="x", size=size)],
        [sg.Button(button_text="-", size=size)],
        [sg.Button(button_text="+", size=size)],
    ]

    # ----full layout------
    layout = [
        [
            display
        ],
        [
            sg.HSeparator(),
        ],
        [
            sg.Column(first_column),
            sg.Column(second_column),
            sg.Column(third_column),
            sg.Column(fourth_column)
        ]
    ]

    # -----build window
    window = sg.Window("SMYT Calculator", layout=layout)
    return window


def is_closed(event):
    return event == "Exit" or event == sg.WIN_CLOSED


def update_display(window, view):
    window["-DISPLAY-"].update(view)



