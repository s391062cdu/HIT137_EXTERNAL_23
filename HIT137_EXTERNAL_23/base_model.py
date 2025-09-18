# This model is designed to be the default run method
# It is overridden by the image and text models
# Mainly to reduce duplicating code for both image and text models

import numpy as np

class BaseModel:
    def __init__(self, image_model, text_model):

        self.image_model = image_model
        self.text_model = text_model

    def process_input (self, input_data):

        if isinstance (input_data, str):
            return self.generate_image_from_text(input_data)
        # If data is words, make an image

        elif isinstance (input_data, np.ndarray):
            return self.generate_text_from_image(input_data)
        # If data is an image, return words

        else:
            raise TypeError("Input must be either text or image")
        
        
    def generate_image_from_text(self, image_model):
        return self.text_to_image_model(image_model)
    
    def generate_text_from_image(self, text_model):
        return self.image_to_text_model(text_model)
    
