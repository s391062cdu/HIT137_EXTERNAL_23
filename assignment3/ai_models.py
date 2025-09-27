import torch
from diffusers import StableDiffusionPipeline
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image


# Load Stable Diffusion
print("Loading Stable Diffusion...")
sd_pipe = StableDiffusionPipeline.from_pretrained(
    "CompVis/stable-diffusion-v1-4"
).to("cpu")


# Load BLIP
print("Loading BLIP...")
blip_processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
blip_model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")


#  Functions 
def generate_image_from_text(prompt: str):
    """Generate an image from a text prompt using Stable Diffusion."""
    image = sd_pipe(prompt).images[0]
    return image


def generate_caption_from_image(image_path: str):
    """Generate a caption for an uploaded image using BLIP."""
    image = Image.open(image_path).convert("RGB")
    inputs = blip_processor(image, return_tensors="pt")
    out = blip_model.generate(**inputs)
    caption = blip_processor.decode(out[0], skip_special_tokens=True)
    return caption
