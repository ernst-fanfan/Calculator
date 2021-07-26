# SMYT STEM
# Ernst R Fanfan
# 7/21/2021

import NumFuntions as nF
import OperationFunctions as oF

EVENT_SWITCHER = {
    "0": nF.zerobutton,
    "1": nF.onebutton,
    "2": nF.twobutton,
    "3": nF.threebutton,
    "4": nF.fourbutton,
    "5": nF.fivebutton,
    "6": nF.sixbutton,
    "7": nF.sevenbutton,
    "8": nF.eightbutton,
    "9": nF.ninebutton,
    ".": nF.period,
    "+": oF.add,
    "-": oF.subtract,
    "x": oF.multiply,
    "/": oF.divide,
}


def set_operator(_operation, _data):
    _operation += _data
    _operator_found = True
    return _operation, _operator_found


def number_placer(number_str, power) -> int:
    result = 0
    for digit in number_str:
        digit_int = EVENT_SWITCHER.get(digit)()
        result += digit_int * 10 ** power
        power -= 1
    return result


def parse_number(number_str) -> int:
    try:
        number_before_decimal_str, number_after_decimal_str = number_str.split(".")
        number_after_decimal_int = number_placer(number_after_decimal_str, -1)
    except ValueError:
        number_before_decimal_str, number_after_decimal_int = number_str, 0

    power = len(number_before_decimal_str) - 1

    number_before_decimal_int = number_placer(number_before_decimal_str, power)

    number_int = number_after_decimal_int + number_before_decimal_int

    return number_int


class Operations:
    operation_function: object()
    raw_data = ""
    operator_detected = False

    def __init__(self):
        pass

    def update_view(self, event):
        # handle second operator
        if not event.isnumeric() and event not in [".", "="] and self.operator_detected is True: self.get_result()

        if event == "AC": return self.clear()
        if self.raw_data == "" and event == ".": return "0."
        if self.raw_data == "" and not event.isnumeric(): return None
        if not event.isnumeric() and not self.raw_data[-1].isnumeric(): return None
        if event == "=": return self.get_result()
        if not event.isnumeric() and event != ".": self.operator_detected = True

        self.raw_data += event

        return self.raw_data

    def raw_split(self):
        first, second, operation, operator_found = "", "", "", False

        for data in self.raw_data:
            if operator_found is False and (data.isnumeric() or data == "."): first += data
            if operator_found is True and (data.isnumeric() or data == "."): second += data
            if not data.isnumeric() and data != ".": operation, operator_found = set_operator(operation, data)

        return first, second, operation

    def get_result(self):
        first_number_str, second_number_str, operation_str = self.raw_split()
        first_number = parse_number(first_number_str)
        second_number = parse_number(second_number_str)
        self.operation_function = EVENT_SWITCHER.get(operation_str)
        self.raw_data = str(self.operation_function(first_number, second_number))
        self.operator_detected = False
        return self.raw_data

    def clear(self):
        self.raw_data = ""
        self.operator_detected = False
        return self.raw_data
