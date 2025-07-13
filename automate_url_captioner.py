import requests
from PIL import Image
from io import BytesIO
from bs4 import BeautifulSoup
from transformers import AutoProcessor, BlipForConditionalGeneration


def download_image(img_url):
    """Download an image from a URL and return a PIL Image object."""
    response = requests.get(img_url)
    image = Image.open(BytesIO(response.content))
    return image


def generate_caption(image, processor, model, max_new_tokens=50):
    """Generate caption for a PIL Image using the given processor and model."""
    inputs = processor(image.convert("RGB"), return_tensors="pt")
    outputs = model.generate(**inputs, max_new_tokens=max_new_tokens)
    caption = processor.decode(outputs[0], skip_special_tokens=True)
    return caption


def main():
    url = "https://en.wikipedia.org/wiki/IBM"

    print(f"Downloading page: {url}")
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    img_elements = soup.find_all("img")

    # Load model and processor once
    processor = AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

    captions_file = "captions.txt"
    with open(captions_file, "w") as f:
        for img_element in img_elements:
            img_url = img_element.get("src")
            if not img_url:
                continue

            # Skip SVGs and very small icons
            if "svg" in img_url or "1x1" in img_url:
                continue

            # Fix incomplete URLs
            if img_url.startswith("//"):
                img_url = "https:" + img_url
            elif not img_url.startswith("http://") and not img_url.startswith("https://"):
                continue

            try:
                image = download_image(img_url)
                # Skip very small images (e.g., icons)
                if image.width * image.height < 400:
                    continue

                caption = generate_caption(image, processor, model)
                f.write(f"{img_url}: {caption}\n")
                print(f"Captioned: {img_url} -> {caption}")

            except Exception as e:
                print(f"Error processing image {img_url}: {e}")


if __name__ == "__main__":
    main()