# This model is designed to be the default run method
# It is overridden by the image and text models
# Mainly to reduce duplicating code for both image and text models

#import all necessary programs/parts
import numpy as np
from abc import ABC, abstractmethod
from model_wrappers import TextToImageWrapper, ImageToTextWrapper
from image_model import ImageModel, image_model
from text_model import TextModel, text_model

#Here is structure for all both ai models
class HuggingFaceModel(ABC):
    def __init__(self, model_id):
        self.model_id = model_id
        self.image_model = image_model
        self.text_model = text_model
        self._pipe = None

    @abstractmethod
    def run(self, input_data):
        pass


class BaseModel:
#This bit makes sure that the rigtht ai model gets used
    def __init__(self, t2i_wrapper, i2t_wrapper):
        self.t2i_wrapper = t2i_wrapper
        self.i2t_wrapper = i2t_wrapper

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
    