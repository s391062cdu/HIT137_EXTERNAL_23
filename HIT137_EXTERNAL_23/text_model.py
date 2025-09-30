# Takes image input from user
# Generates caption or description based on input

from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import numpy as np
import torch
from base_model import HuggingFaceModel
from utils import log_function_call

processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

class TextModel(HuggingFaceModel):
    def __init__(self, model_id="Salesforce/blip-image-captioning-base"):
        super().__init__(model_id)
        self.device = "cpu"

        self.processor = BlipProcessor.from_pretrained(self.model_id)
        self._pipe = BlipForConditionalGeneration.from_pretrained(self.model_id)
        self._pipe.to(self.device)

    @log_function_call
    def run(self, image_array: np.ndarray) -> str:
        image = Image.fromarray(image_array.astype(np.uint8))
        inputs = self.processor(image, return_tensors = "pt").to(self.device)
        out = self._pipe.generate(**inputs)
        caption = self.processor.decode(out[0], skip_special_tokens=True)
        return caption
    
text_model = TextModel()