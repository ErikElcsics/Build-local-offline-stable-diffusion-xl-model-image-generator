import sys
from pathlib import Path
from transformers import pipeline
import streamlit as st
import os
from diffusers import DiffusionPipeline
import torch
import ctransformers # use this way to reference - ctransformers.AutoModelForCausalLM because same cls in transformers too
from transformers import AutoTokenizer, AutoModelForCausalLM, TextIteratorStreamer # TextIteratorStreamer to stream
from threading import Thread

sys.path.append(str(Path(__file__).resolve().parents[2]))

@st.cache_resource()
def load_model_local_sdxl(model_path_sdxl, torch_dtype=torch.float16, variant="fp16", use_safetensors=True):

    #### BASE MODEL ####
    base = DiffusionPipeline.from_pretrained(model_path_sdxl,
                                             torch_dtype=torch.float16,
                                             use_safetensors=True)
    base.enable_model_cpu_offload()

    return base

def generate_image_local_sdxl(base, prompt, refiner=None, num_inference_steps=20, guidance_scale=15,
                                  high_noise_frac=0.8, output_type="latent", verbose=False, temprature=0.7):

    image = base(prompt=prompt, num_inference_steps=num_inference_steps,
                     guidance_scale=guidance_scale).images[0]

    return image

#### Local (Offline) Diffusion Model Image Generation ####
st.title("Local (Offline) Diffusion Model Image Generator")

# https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/tree/main
model_path_sdxl = ("Models/models--stabilityai--stable-diffusion-xl-base-1.0/"
                   "snapshots/462165984030d82259a11f4367a4eed129e94a7b")

base = load_model_local_sdxl(model_path_sdxl, None)

user_input = st.text_input("Enter your prompt", value="Tiger")

prompt = user_input

# Adding a slider for the number of images
num_images = st.slider("Select number of images to generate:", 1, 10, 2)

if st.button("Generate Image"):
    with st.spinner('Generating image...'):
        progress_bar = st.progress(0)

        # Adjust for image generation
        for i in range(num_images):
            if i % 2 == 0:
                cols = st.columns(2)  # Create two columns only for even index

            # Generate image
            generated_image = generate_image_local_sdxl(base, prompt)

            # Display image in the appropriate column
            with cols[i % 2]:  # Use modulus to toggle between 0 and 1 for column index
                st.image(generated_image, channels="BGR", use_container_width=True)

            # Update progress after each image is generated and displayed
            progress = ((i + 1) / num_images)
            progress_bar.progress(int(progress * 100))