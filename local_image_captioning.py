import os
import glob
from PIL import Image
from transformers import Blip2Processor, Blip2ForConditionalGeneration

IMAGE_DIR = "./images"
IMAGE_EXTS = ["jpg", "jpeg", "png"]
OUTPUT_FILE = "captions.txt"
MAX_NEW_TOKENS = 50

processor = Blip2Processor.from_pretrained("Salesforce/blip2-opt-2.7b")
model = Blip2ForConditionalGeneration.from_pretrained("Salesforce/blip2-opt-2.7b")

def generate_caption(image_path):
    image = Image.open(image_path).convert('RGB')
    inputs = processor(image, return_tensors="pt")
    output = model.generate(**inputs, max_new_tokens=MAX_NEW_TOKENS)
    return processor.decode(output[0], skip_special_tokens=True)

def find_images(directory, exts):
    files = []
    for ext in exts:
        files.extend(glob.glob(os.path.join(directory, f"*.{ext}")))
        files.extend(glob.glob(os.path.join(directory, f"*.{ext.upper()}")))
    return files

def main():
    images = find_images(IMAGE_DIR, IMAGE_EXTS)
    if not images:
        print(f"No images found in {IMAGE_DIR}")
        return
    with open(OUTPUT_FILE, "w") as f:
        for img_path in images:
            caption = generate_caption(img_path)
            f.write(f"{os.path.basename(img_path)}: {caption}\n")
            print(f"{os.path.basename(img_path)}: {caption}")

if __name__ == "__main__":
    main()