from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog as fd
from functions import GFG
import math
import tkinter.ttk


def image_file_name(prompt_title):
    filetypes = (
        ('png files', '*.png'),
        ('jpg files', '*.jpg'),
        ('jpeg files', '*.jpeg')
    )

    file_name = fd.askopenfilename(
        title=prompt_title,
        initialdir='/home/roia/Pictures',
        filetypes=filetypes)

    return file_name

def choose_image():

    file_name = image_file_name("Choose An Image")
    chosen_img = Image.open(file_name)
    image_size = chosen_img.size
    # resize image to fit the window maintaining ratio
    image_width = image_size[0]
    image_height = image_size[1]

    if image_width > 520:
        new_image_width = image_width - (image_width - 520)
        new_image_height = math.floor(image_height / (image_width / new_image_width))
    elif image_height > 600:
        new_image_height = image_height - (image_height - 600)
        new_image_width = math.floor(image_width / (image_height / new_image_height))
    else:
        new_image_width = image_width
        new_image_height = image_height

    # center the picture in the canvas
    left_space = 600 - new_image_height
    new_y_position = math.floor(left_space/2)


    chosen_img = chosen_img.resize((new_image_width, new_image_height), Image.ANTIALIAS)
    new_chosen_img = ImageTk.PhotoImage(chosen_img)
    right_canvas.create_image(0, 0, image=new_chosen_img, anchor="nw")
    right_canvas.place(x=290, y=new_y_position)
    right_canvas.image = new_chosen_img




def choose_watermark():

    file_name = image_file_name("Choose A Watermark")
    gfg = GFG(file_name, root)
	# This will bind arrow keys to the tkinter
	# toplevel which will navigate the image or drawing
    root.bind("<KeyPress-Left>", lambda e: gfg.left(e))
    root.bind("<KeyPress-Right>", lambda e: gfg.right(e))
    root.bind("<KeyPress-Up>", lambda e: gfg.up(e))
    root.bind("<KeyPress-Down>", lambda e: gfg.down(e))



def add_text():
    pass



# root window
root = Tk()
root.title("Origami Image WatermarK")
root.geometry("800x600")

#-------------------------Left side of the screen---------------------------------#
# logo
canvas = Canvas(width=221, height=332)
logo_img = PhotoImage(file="images/origami_logo_window.png")
canvas.create_image(115, 135, image=logo_img)
canvas.place(x=10, y=2)

# Buttons
choose_image_button = Button(text="Choose Image", command=choose_image)
choose_watermark_button = Button(text="Choose Watermark Image", command=choose_watermark)
text_watermark = Button(text="Add Text Watermark", command=add_text)

# Labels
choose_image_label = Label(text="Select a picture to add watermark to it")
watermark_type = Label(text="Add a picture or a text Watermark")

# widget placement on screen
choose_image_label.place(x=5, y=260)
choose_image_button.place(x=60, y=290)
watermark_type.place(x=8, y=380)
choose_watermark_button.place(x=20, y=410)
text_watermark.place(x=38, y=460)

#------------------------- Line on screen ---------------------------------#
line_canvas = Canvas(width=10, height=1200)
line_canvas.place(x=280, y=0)
line_canvas.create_line(2, 0, 2, 1200)

#-------------------------Right side of the screen---------------------------------#
right_canvas = Canvas(width=520, height=600)
right_canvas.place(x=290, y=0)



# root.bind('<Configure>', resizer)

root.mainloop()
