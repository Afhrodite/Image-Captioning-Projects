import torch
from PIL import Image
from transformers import AutoProcessor, BlipForConditionalGeneration

# Load the pretrained processor and model
processor = AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

def generate_caption(img_path):
    # Safely load and convert image
    with Image.open(img_path) as image:
        image = image.convert('RGB')

    # Prepare inputs
    text = "the image of"  # can also try text=None
    inputs = processor(images=image, text=text, return_tensors="pt")

    # Generate caption
    outputs = model.generate(**inputs, max_length=50)

    # Decode to text
    caption = processor.batch_decode(outputs, skip_special_tokens=True)[0]
    return caption

if __name__ == "__main__":
    img_path = "images/flower_heart.png"
    caption = generate_caption(img_path)
    print(caption)