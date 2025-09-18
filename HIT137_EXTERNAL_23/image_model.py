# Takes text input from user
# Generates an image output based on text

from diffusers import StableDiffusionPipeline
import torch

class ImageModel:
    def __init__(self):
        self._pipe = StableDiffusionPipeline.from_pretrained(
            "CompVis/stable-diffusion-v1-4",
            torch_dtype=torch.float32
        )
        self._pipe.to("cpu")

    def run(self, prompt):
        image = self._pipe(prompt).images[0]
        return image