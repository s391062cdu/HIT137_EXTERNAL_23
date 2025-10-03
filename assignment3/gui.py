import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import ai_models


class Application:
    def __init__(self, root):
        self.root = root
        self.root.title("Text ↔ Image AI Generator")

        # Left: Text to Image
        left_frame = tk.Frame(root, padx=10, pady=10)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        tk.Label(left_frame, text="Text to Image").pack()
        self.prompt_entry = tk.Text(left_frame, height=5, width=40)
        self.prompt_entry.pack()

        self.gen_button = tk.Button(left_frame, text="Generate Image", command=self.generate_image)
        self.gen_button.pack(pady=5)

        self.img_label = tk.Label(left_frame, text="Generated image will appear here")
        self.img_label.pack()

        # Right: Image to Text
        right_frame = tk.Frame(root, padx=10, pady=10)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        tk.Label(right_frame, text="Image to Text").pack()

        self.upload_btn = tk.Button(right_frame, text="Upload Image", command=self.upload_image)
        self.upload_btn.pack(pady=5)

        self.uploaded_label = tk.Label(right_frame, text="Uploaded image will appear here")
        self.uploaded_label.pack()

        self.caption_btn = tk.Button(right_frame, text="Generate Caption", command=self.generate_caption)
        self.caption_btn.pack(pady=5)

        self.caption_box = tk.Text(right_frame, height=5, width=40)
        self.caption_box.pack()

        self.uploaded_path = None

    #  Functions 
    def generate_image(self):
        prompt = self.prompt_entry.get("1.0", tk.END).strip()
        if not prompt:
            return
        image = ai_models.generate_image_from_text(prompt)
        image.thumbnail((300, 300))
        img_tk = ImageTk.PhotoImage(image)
        self.img_label.config(image=img_tk)
        self.img_label.image = img_tk

    def upload_image(self):
        filename = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg")])
        if filename:
            self.uploaded_path = filename
            img = Image.open(filename)
            img.thumbnail((300, 300))
            img_tk = ImageTk.PhotoImage(img)
            self.uploaded_label.config(image=img_tk)
            self.uploaded_label.image = img_tk

    def generate_caption(self):
        if not self.uploaded_path:
            return
        caption = ai_models.generate_caption_from_image(self.uploaded_path)
        self.caption_box.delete("1.0", tk.END)
        self.caption_box.insert(tk.END, caption)


if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    root.mainloop()


