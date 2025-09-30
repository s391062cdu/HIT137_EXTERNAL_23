# Takes text input from user
# Generates an image output based on text

from diffusers import StableDiffusionPipeline
import torch
from base_model import HuggingFaceModel
from utils import log_function_call


class ImageModel(HuggingFaceModel):
    def __init__(self, model_id="ComVis/stable-diffusion-v1-4"):
        super().__init__(model_id)

    
        self._pipe = StableDiffusionPipeline.from_pretrained(self.model.id, torch_dtype=torch.float32)
        self._pipe.to("cpu")

    @log_function_call
    def run(self, prompt):
        image = self._pipe(prompt).images[0]
        return image
    
image_model = ImageModel()