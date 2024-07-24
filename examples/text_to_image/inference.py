import torch
from diffusers import StableDiffusionPipeline
from PIL import Image
import os

# Load the fine-tuned model
model_path = "sd-anime-model"
pipe = StableDiffusionPipeline.from_pretrained(model_path, torch_dtype=torch.float16).to("cuda")
pipe.safety_checker = None

# Run inference
prompt = "A girl playing with a dog"
num_images = 1

with torch.autocast("cuda"):
    images = pipe(prompt, num_images_per_prompt=num_images).images

# Save the generated images
output_dir = os.path.dirname(__file__)
output_path = os.path.join(output_dir, 'output.png')

for img in images:
    img.save(output_path)
    print(f"Image saved to {output_path}")





