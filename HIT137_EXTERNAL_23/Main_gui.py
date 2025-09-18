# The main code and GUI setup
# Links all the other codes together

import numpy as np
from base_model import BaseModel
from model_wrappers import TextToImageWrapper, ImageToTextWrapper
from image_model import image_model
from text_model import text_model

t2i_wrapper = TextToImageWrapper(image_model)
i2t_wrapper = ImageToTextWrapper(text_model)

base_model = BaseModel(t2i_wrapper, i2t_wrapper)

import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk



def process_input():
    user_input = input_text.get().strip()

    if user_input.strip():
        output_image = base_model.process_input(user_input)
        display_image(output_image)

    elif selected_image.get():
        img = Image.open(selected_image.get())
        img_array = np.array
        description = base_model.process_input(img_array)
        output_label.confi(text=description)

    def display_image(img_array):
        img = Image.fromarray(img_array.astype(np.uint8))
        img_tk = ImageTk.PhotoImage(img)
        image_label.config(image=img_tk)
        image_label.image = img_tk

    def selected_image_file():
        filename = filedialog.askopenfilename()
        if filename:
            selected_image.set(filename)
    

#Need to setup the gui bit with buttons or menus or whatever. 
# input_text = something -> using this to convert it into image
# 
