# author @22PoojaGaur

from fpdf import FPDF


class PDF(FPDF):
    pass


class MyPDF:

    def __init__(self):
        self.pdf = PDF(orientation='P', unit='cm', format='A4')

        self.width = 21
        self.height = 29.7

        self.C = None
        self.R = None

    def add_page(self):
        self.pdf.add_page()

    def add_line(self):
        self.pdf.set_line_width(1.0)
        self.pdf.line(3, self.height/2, self.width - 3, self.height/2)

    def add_image(self, name, type):
        self.pdf.image(name, type=type, x=1, y=1, w=15, h=15)

    def add_image_with_pos(self, name, type, start, end):
        # find size
        img_grid_width = end[1] - start[1] + 1
        img_grid_height = end[0] - start[0] + 1

        img_width = (self.width * float(img_grid_width)) / self.C
        img_height = (self.height * float(img_grid_height)) / self.R

        print ('START position is ', start[1], ' ', start[0])
        x = (start[1] * float(self.width)) / self.C
        y = (start[0] * float(self.height)) / self.R

        #self.pdf.set_xy(x, y)
        self.pdf.image(name, type=type, x=x, y=y, w=img_width, h=img_height)

    def set_grid_dims(self, dims):
        self.R = dims[0]
        self.C = dims[1]
