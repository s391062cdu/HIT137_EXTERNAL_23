class TextToImageWrapper:
    def __init__(self, model):
        self.model = model

    def generate(self, text_input):
        return self.model.run(text_input)
    

class ImageToTextWrapper:
    def __init__(self, model):
        self.model = model

    def generate(self, image_array):
        return self.model.run(image_array)
