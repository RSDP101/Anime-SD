import os
import subprocess

# List of model names (though this list is not used in this script)
models_list = [
    "stabilityai/stable-diffusion-xl-base-1.0",
    "CompVis/stable-diffusion-v1-4",
    "stablediffusionapi/anything-v5",
    "waifu-diffusion v1.4"
]

# Set environment variables
os.environ['MODEL_NAME'] = "CompVis/stable-diffusion-v1-4"
os.environ['DATASET_NAME'] = "rod101/Anime1K"

# Command to execute
command = [
    "accelerate", "launch", "train_text_to_image.py",
    f"--pretrained_model_name_or_path={os.environ['MODEL_NAME']}",
    f"--dataset_name={os.environ['DATASET_NAME']}",
    "--use_ema",
    "--resolution=512", "--center_crop", "--random_flip",
    "--train_batch_size=1",
    "--gradient_accumulation_steps=4",
    "--gradient_checkpointing",
    "--mixed_precision=fp16",
    "--max_train_steps=200",
    "--learning_rate=1e-05",
    "--max_grad_norm=1",
    "--lr_scheduler=constant", "--lr_warmup_steps=0",
    "--output_dir=sdxl-anime-model"
]

# Execute the command
subprocess.run(command, check=True)
