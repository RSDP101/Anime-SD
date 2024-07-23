
import torch
from diffusers import StableDiffusionPipeline
import matplotlib.pyplot as plt
from PIL import Image

# Load the fine-tuned model
model_path = "sd-anime-model"
pipe = StableDiffusionPipeline.from_pretrained(model_path, torch_dtype=torch.float16).to("cuda")
pipe.safety_checker = None
# Run inference
prompt = "a girl with bunny ears"
num_images = 1

with torch.autocast("cuda"):
    images = pipe(prompt, num_images_per_prompt=num_images).images

# Display the generated images


for img in images:
    plt.figure(figsize=(10,10))
    plt.imshow(img)
    plt.axis('off')  # Hide axes
    plt.show()

