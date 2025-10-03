Saturday 29/09/25, - Aidan
Contacted Abhijith as I was struggling to finish the assignment from the work Connor had done. He informed me that the assignment needed to be split into three folders: AI Models. He also talked me through an example code. The 'Assignment3' folder follows these instructions.

setup Instructions for Running main.py - Zayne

1. Install Python
   - Download and install Python 3.11  
   - When installing, tick “Add Python to PATH”.

2. Set up the project folder
   - Download or clone this project from GitHub.
   - Open a terminal (PowerShell on Windows) in the project folder.

3. Create a virtual environment:
   python -m venv .venv
   
Then activate it:
   .venv\Scripts\activate

4. Install required packages
   Run this inside the activated environment:
   pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

   pip install diffusers transformers accelerate safetensors pillow datasets

   (this installs PyTorch with GPU support and other libraries needed)

5. Check PyTorch and CUDA (to make sure GPU is detected):
   python
   >>> import torch
   >>> print(torch.cuda.is_available())
   >>> print(torch.cuda.get_device_name(0))
   - If it shows True and your GPU name → it’s works
   - If False, the program will still run, but much slower (CPU only).

6. Run the program
   python assignment3/main.py


Common Errors and Fixes

- ModuleNotFoundError (e.g., No module named 'PIL')
  → Run: pip install pillow

- Error: requirements.txt not found
  → Just install the packages manually as listed above (step 4).
