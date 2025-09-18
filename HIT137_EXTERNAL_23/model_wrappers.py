class TextToImageWrapper:
    def __init__(self, model):
        self.model = model

    def generate(self, text_input):
        return self.model.generate_image(text_input)
    

class ImageToTextWrapper:
    def __init__(self, model):
        self.model = model

    def generate(self, image_array):
        return self.mode.generate_text(image_array)
