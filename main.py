from tkinter import *
from tkinter import filedialog
import tkinterdnd2
from PIL import ImageTk, Image, ImageDraw, ImageFont

# watermark = tkinterdnd2.Tk()
#
#
#
# # Todo 1: create canvas with tkinter
#
# watermark.title('My watermark app')
# watermark.config(bg='#e19f7b')
# app_title = Label(watermark, text=" Welcome to Maud's Watermarker", bg="#e19f7b",  font=("bold", 30))
# app_title.pack()
# c = Canvas(watermark, width=700, height=600)
# c.place(x=250, y=250)
# # Todo 2: upload image with tkinter
#
# # create upload button
# upload_button = Button(watermark, text="Upload image ", height=10, width=30, bg="#E8C07D", command=uploading_image)
# upload_button.place(x=1000, y=500)
#
#
# #  click event listener to load the photo files GUI
# def uploading_image():
#     img = ImageTk.PhotoImage(Image.open(r"imagepath\imagename.extension"))
#     c.create_image(x, y, image=img, anchor=NW)
# #  when loaded add the logo automatically
# Todo 3: add a logo on the uploaded image

# Todo 4: store the final image
#
#
# watermark.mainloop()

root = Tk()
root.withdraw()
filename = filedialog.askopenfilename(initialdir="yourpathtodownloads", title='Select an Image:')


def add_watermark(image, wm_text):
    opened_image = Image.open(image)

    image_width, image_height = opened_image.size
    draw = ImageDraw.Draw(opened_image)

    font_size = int(image_width / 8)

    font = ImageFont.truetype('Arial.ttf', font_size)

    x, y = int(image_width / 2), int(image_height / 2)

    draw.text((x, y), wm_text, font=font, fill='#FFF', stroke_width=5, stroke_fill='#222', anchor='ms')
    opened_image.show()


add_watermark(filename, 'Maud brew')
