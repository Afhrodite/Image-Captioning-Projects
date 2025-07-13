import gradio as gr
import numpy as np
from PIL import Image
from transformers import AutoProcessor, BlipForConditionalGeneration

# Load the pretrained processor and model once
processor = AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

def caption_image(input_image: np.ndarray, max_length: int = 50) -> str:
    """
    Generate a caption for an input image using BLIP image captioning model.

    Args:
        input_image (np.ndarray): Image in numpy array format from Gradio.
        max_length (int): Maximum length of the generated caption.

    Returns:
        str: Generated caption describing the image.
    """
    # Convert numpy array to PIL Image and ensure RGB
    image = Image.fromarray(input_image).convert("RGB")

    # Prepare inputs for the model
    inputs = processor(images=image, return_tensors="pt")

    # Generate output ids
    output_ids = model.generate(**inputs, max_length=max_length)

    # Decode to text
    caption = processor.batch_decode(output_ids, skip_special_tokens=True)[0]

    return caption

# Define the Gradio interface
iface = gr.Interface(
    fn=caption_image,
    inputs=gr.Image(type="numpy", label="Upload an Image"),
    outputs=gr.Textbox(label="Generated Caption"),
    title="Image Captioning with BLIP",
    description="This is a simple web app for generating captions for images using a trained model.",
    examples=None
)

if __name__ == "__main__":
    iface.launch()