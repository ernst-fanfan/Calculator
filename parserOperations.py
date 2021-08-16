# SMYT STEM
# Ernst R Fanfan
# 7/26/2021


class Parser:
    raw_data = ""

    def __init__(self):
        pass

    def parse(self, display):
        self.multiplication_checker(display)
        return str(self.raw_data)

    def multiplication_checker(self, display):
        self.raw_data = eval(display.replace("x", "*"))


    