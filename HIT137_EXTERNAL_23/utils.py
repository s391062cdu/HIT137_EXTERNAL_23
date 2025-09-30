#For reusable functions that don't belong in any specific other code
#Also includes the decorator


#Import all important things
import logging
from functools import wraps
import numpy as np

#Re-usable functions to be used generally and by other bits of code
def update_output_message(output_label, message, is_error=False):
    color = "red" if is_error else "black"
    output_label.config(text=message, fg=color)

def clear_miage_display(image_label):
    image_label.config(image='')
    image_label.image=None

#Decorater set up below
logging.basicConfig(level=logging.INFO,)
app_logger = logging.getLogger('Ai_Converter')

def log_function_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        instance_name = args[0].__class__.__name__ if args and hasattr(args[0], '__class__') else ''
        app_logger.info(f"{instance_name}.{func.__name__} started processing.")
      
        try:
            result = func(*args, **kwargs)
            app_logger.info(f"{instance_name}.{func.__name__} comleted successfully.")
            return result
        except Exception as e:
            app_logger.error(f"{instance_name}.{func.__name__} failed {e}")
            raise
    
    return wrapper

