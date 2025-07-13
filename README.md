# Image Captioning Projects

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![PyTorch](https://img.shields.io/badge/PyTorch-2.1.0-red?logo=pytorch)
![Transformers](https://img.shields.io/badge/Transformers-4.40.1-blueviolet?logo=transformers)
![Pillow](https://img.shields.io/badge/Pillow-10.3.0-orange?logo=pillow)
![NumPy](https://img.shields.io/badge/NumPy-1.24%2B-yellow?logo=python)
![Gradio](https://img.shields.io/badge/Gradio-4.18.0-brightgreen?logo=gradio)
![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)
![Project Status](https://img.shields.io/badge/Project-Image%20Captioning%20Module-success)


_Created by **Réka Gábosi**_

## Table of Contents

1. [Overview](#overview)  
2. [File Structure](#file-structure)  
3. [How to Install and Run](#how-to-install-and-run)  
4. [Project 1: Local Image Captioning (`local_image_captioning.py`)](#project-1-local-image-captioning-local_image_captioningpy)  
5. [Project 2: Single Image Captioning (`image_cap.py`)](#project-2-single-image-captioning-image_cappy)  
6. [Project 3: Interactive Web App (`image_captioning_app.py`)](#project-3-interactive-web-app-image_captioning_apppy)  
7. [Project 4: URL Image Captioning (`automate_url_captioner.py`)](#project-4-url-image-captioning-automate_url_captionerpy)  
8. [Acknowledgements](#acknowledgements)  

## Overview

This repository contains 4 projects from **Module 1** of the IBM course  
*Building Generative AI-Powered Applications with Python*.

Each project explores different aspects of generative AI, natural language understanding, and Python app development. This repo serves as a practical implementation and learning tool for those concepts.

**Note:** Each project's code has been restructured and cleaned up for better readability and easier understanding.

## File Structure

```ini
├──images 
│    ├── pixel_hedgehog.png
│    └── flower_heart.png
│
├── automate_url_captioner.py
├── captions.txt
├── image_cap.py
├── image_captioning_app.py
├── local_image_captioning.py
├── README.md
├── requirements.txt
└── LICENSE
```

## How to Install and Run

1. Clone this repository:

    ```bash
    git clone https://github.com/Afhrodite/Image-Captioning-Projects
    cd Image-Captioning-Projects
    ```

2. (Optional) Create and activate a Python virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate      # Linux/Mac
    .\venv\Scripts\activate       # Windows
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. `Run the local batch caption generator (local_image_captioning.py)` - processes all images in images/ folder:
    ```bash
    python3 local_image_captioning.py
    ```


    `Run the single image caption script (image_cap.py)`
    ```bash
    python3 image_cap.py
    ```

    To change the image in image_cap.py, edit the following line inside the script:

        img_path = "images/flower_heart.png"

    Replace "flower_heart.png" with any image filename in your images/ directory.


    `Run the interactive web app (image_captioning_app.py)`
    ```bash
    python3 image_captioning_app.py
    ```
    Upload an image in the browser to get captions.


    `Run the URL image captioning (automate_url_captioner.py)`
    ```bash
    python3 automate_url_captioner.py
    ```
    The script downloads images from the hardcoded Wikipedia page on IBM:
    ```bash
    url = "https://en.wikipedia.org/wiki/IBM"
    ```
    It skips small images and SVG icons, then writes captions to captions.txt while printing progress in the terminal.

## Project 1: Local Image Captioning (`local_image_captioning.py`)

This script uses the Hugging Face **BLIP-2** model (`Salesforce/blip2-opt-2.7b`) to generate captions for images stored locally in the `/images` folder. It processes images with extensions `.jpg`, `.jpeg`, and `.png` and outputs captions to `captions.txt`.

**Example output from `captions.txt`:**
- pixel_hedgehog.png: a pixel pixel with a face and a black background
- flower_heart.png: a pixel heart with pink flowers

*Note:* The caption for `pixel_hedgehog.png` was not predicted correctly, while `flower_heart.png` was captioned well. This highlights the challenges in AI image understanding for certain types of pixel art.

## Project 2: Single Image Captioning (`image_cap.py`)

Generates a caption for a single specified image using the BLIP base model.

**Example output:**
- the image of a pixeled lion → Incorrect, it was a pixel hedgehog
- pixel heart with flowers → Correct caption

## Project 3: Interactive Web App (`image_captioning_app.py`)

A simple Gradio web app to upload images and get captions dynamically.

**Example captions observed:**
- a bunch of oranges → Incorrect, it was pixel art honeycomb
- pixel heart with pink flowers → Correct
- pixel style lion → Correct
- black bird with colorful smoke and stars → Correct
- yellow background with honeycomb and bees → Partially correct (mentions bees, misses honeycomb)

## Project 4: URL Image Captioning (`automate_url_captioner.py`)

This script downloads images from a specified URL webpage, then generates captions for each image using the BLIP base model (`Salesforce/blip-image-captioning-base`).

It uses:
- `requests` to fetch webpage and images
- `BeautifulSoup` to parse HTML and find `<img>` tags
- `transformers` to load the BLIP model and processor
- `PIL` to process images

**Example terminal output:**
- Captioned: https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/IBM_CHQ_-_Oct_2014.jpg/250px-IBM_CHQ_-_Oct_2014.jpg -> a large building
- Captioned: https://upload.wikimedia.org/wikipedia/commons/thumb/2/20/IBM_Electronic_Data_Processing_Machine_-_GPN-2000-001881.jpg/250px-IBM_Electronic_Data_Processing_Machine_-_GPN-2000-001881.jpg -> a man in a room with a computer
- Captioned: https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/IBM360-67AtUmichWithMikeAlexander.jpg/250px-IBM360-67AtUmichWithMikeAlexander.jpg -> a man sitting at a desk
- Error processing image https://upload.wikimedia.org/wikipedia/commons/thumb/7/7a/Saturn_IB_and_V_Instrument_Unit.jpg/250px-Saturn_IB_and_V_Instrument_Unit.jpg: cannot identify image file <_io.BytesIO object at 0x732f0d00b330>
- Captioned: https://upload.wikimedia.org/wikipedia/commons/thumb/a/a6/IBM_PC-IMG_7271_%28transparent%29.png/250px-IBM_PC-IMG_7271_%28transparent%29.png -> a computer with a keyboard and monitor
- Captioned: https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/IBMinventions.png/250px-IBMinventions.png -> a hard disk and a hard drive
- Captioned: https://upload.wikimedia.org/wikipedia/commons/thumb/3/34/IBM_Beijing%2C_Pangu_Plaza.jpg/250px-IBM_Beijing%2C_Pangu_Plaza.jpg -> a tall building with a large sign on it
- Captioned: https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/Mira_-_Blue_Gene_Q_at_Argonne_National_Laboratory_-_Skin.jpg/250px-Mira_-_Blue_Gene_Q_at_Argonne_National_Laboratory_-_Skin.jpg -> a large room with a large mural on the wall
- Error processing image https://upload.wikimedia.org/wikipedia/commons/thumb/6/60/IBM_Q_system_%28Fraunhofer_2%29.jpg/250px-IBM_Q_system_%28Fraunhofer_2%29.jpg: cannot identify image file <_io.BytesIO object at 0x732f0dcff010>
- Captioned: https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/IBM_Yorktown_Heights.jpg/250px-IBM_Yorktown_Heights.jpg -> a large building
- Captioned: https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/Benoit_Mandelbrot%2C_TED_2010.jpg/250px-Benoit_Mandelbrot%2C_TED_2010.jpg -> a man in a suit and tie sitting on a chair
- Captioned: https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/IBM_ads_at_JFK.jpg/250px-IBM_ads_at_JFK.jpg -> a long hallway with a sign that says it's time to go
- Error processing image https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Ibmaustin_designcamp.jpg/250px-Ibmaustin_designcamp.jpg: cannot identify image file <_io.BytesIO object at 0x732f0b1f22f0>
- Captioned: https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/Watson_Jeopardy_demo.jpg/250px-Watson_Jeopardy_demo.jpg -> a large room with a lot of people
- Captioned: https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/Nuvola_apps_ksim.png/20px-Nuvola_apps_ksim.png -> a computer screen with a green screen

*Note:* Some images fail to process due to format issues, which is expected.

## Acknowledgements

This project was developed as part of the **IBM course: Building Generative AI-Powered Applications with Python**, provided on Coursera.

Special thanks to:
- **IBM Skills Network** for the project framework and Watson NLU access.