# version: 0.0.1
# author: picklez
# purpose: to just play around with graphical rendering in python
# I just kinda wanted to see how you would put a cosine and sine function on to a window

import numpy
import math
import tkinter
from PIL import Image,ImageTk

height = 900
width = 1600
x_axis_line = int(height/2)
y_axis_line = int(width/2)
y_multiplier = height/4
x_pi_pixel_ratio = (4 * math.pi) / width

def create_blank_x(new_image):
    # draw x axis!
    for i in range(width):
        # draws axis line!
        new_image[x_axis_line][i][0] = 255
        new_image[x_axis_line][i][1] = 255
        new_image[x_axis_line][i][2] = 255
        # draws hash marks!
        if i == 0 or i == int(width/4) or i == int(3*width/4) or i == int(width/8) or i == int(3*width/8) or i == int(5*width/8) or i == int(7*width/8):
            for ii in range(1,11):
                new_image[x_axis_line-ii][i][0] = 255
                new_image[x_axis_line-ii][i][1] = 255
                new_image[x_axis_line-ii][i][2] = 255
                new_image[x_axis_line+ii][i][0] = 255
                new_image[x_axis_line+ii][i][1] = 255
                new_image[x_axis_line+ii][i][2] = 255
    # draw y axis!
    for j in range(height):
        # draws axis line!
        new_image[j][y_axis_line][0] = 255
        new_image[j][y_axis_line][1] = 255
        new_image[j][y_axis_line][2] = 255
        # draws hash marks!
        if j == 0 or j == int(height/4) or j == int(3*height/4) or j == int(height/8) or j == int(3*height/8) or j == int(5*height/8) or j == int(7*height/8):
            for jj in range(1,11):
                new_image[j][y_axis_line-jj][0] = 255
                new_image[j][y_axis_line-jj][1] = 255
                new_image[j][y_axis_line-jj][2] = 255
                new_image[j][y_axis_line+jj][0] = 255
                new_image[j][y_axis_line+jj][1] = 255
                new_image[j][y_axis_line+jj][2] = 255
    return new_image

def create_sin_image(new_image):
    for x in range(width):
        equation = x_axis_line - ( math.sin( x * x_pi_pixel_ratio ) * y_multiplier)
        new_image[int(equation)][x][0] = 0
        new_image[int(equation)][x][1] = 0
        new_image[int(equation)][x][2] = 255
    return new_image
    
def create_cos_image(new_image):
    for x in range(width):
        equation = x_axis_line - ( math.cos( x * x_pi_pixel_ratio ) * y_multiplier)
        new_image[int(equation)][x][0] = 255
        new_image[int(equation)][x][1] = 0
        new_image[int(equation)][x][2] = 0
    return new_image

def window_on_run(img):
    window = tkinter.Tk()
    window.title("Visual Testing")
    window.configure(width=width,height=height)
    window.configure(bg='black')
    winWidth = window.winfo_reqwidth()
    winHeight = window.winfo_reqheight()
    posRight = int(window.winfo_screenwidth() / 2 - winWidth /2)
    posDown = int(window.winfo_screenheight() / 2 - winHeight / 2)
    window.geometry("+{}+{}".format(posRight, posDown))
    
    canvas = tkinter.Canvas(window)
    canvas = tkinter.Canvas(window, width=width, height=height)
    canvas.pack()
    
    img2 = ImageTk.PhotoImage(image=Image.fromarray((img.copy()).astype(numpy.uint8)))
    canvas.create_image(0, 0, anchor=tkinter.NW, image=img2)
    canvas.update()
    
    window.mainloop()
    
new_image = numpy.empty((height,width,3))
new_image = create_blank_x(new_image)
new_image = create_sin_image(new_image)
new_image = create_cos_image(new_image)
window_on_run(new_image)