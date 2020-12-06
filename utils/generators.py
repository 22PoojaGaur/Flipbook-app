# author @22PoojaGaur

from fpdf import FPDF


class PDF(FPDF):
    pass


class MyPDF:

    def __init__(self):
        self.pdf = PDF(orientation='P', unit='cm', format='A4')

        self.width = 21
        self.height = 29.7

    def add_page(self):
        self.pdf.add_page()

    def add_line(self):
        self.pdf.set_line_width(1.0)
        self.pdf.line(3, self.height/2, self.width - 3, self.height/2)

    def add_image(self, name, type):
        self.pdf.image(name, type=type, x=1, y=1, w=15, h=15)
