Build Local (Offline) Stable Diffusion XL Model Image Generator

This project provides a Streamlit-based web application for generating images from text prompts using a locally hosted Stable Diffusion XL model. It enables users to input descriptive prompts and receive corresponding AI-generated images directly on their machines, ensuring privacy and offline capability.​

Features
- Local Model Hosting: Runs the Stable Diffusion XL model entirely offline on your hardware.​
- Interactive Prompt Input: Enter custom text prompts to generate unique images.​
- Batch Generation: Specify the number of images to generate per prompt.​
- Progress Feedback: Visual progress bar updates during image generation.​

Requirements
Hardware: A GPU with a minimum of 8GB VRAM is recommended for optimal performance.​ (Note: can run with CPU but will be very slow)

Software Dependencies:

Python 3.8 or higher​
Streamlit​
Transformers​
Jakarta AI Research
Diffusers​
Torch​
ctransformers​
Pillow​

Ensure all necessary libraries are installed, and the Stable Diffusion XL model is accessible at the specified path.​

Usage
Clone the Repository:
git clone https://github.com/ErikElcsics/Build-local-offline-stable-diffusion-xl-model-image-generator.git

Navigate to the Project Directory:
cd local-sdxl-image-generator

Install Dependencies:
pip install -r requirements.txt

To download the Stable Diffusion XL Base 1.0 model from Hugging Face to your local machine, follow these steps:

Install Git and Git LFS:

Git: Ensure Git is installed on your system. Download it from git-scm.com if it's not already installed.​

Git LFS (Large File Storage): This extension is necessary for handling large files like model weights. Install it by running:​
git lfs install

Clone the Model Repository:
Use Git to clone the model repository from Hugging Face:​

git clone https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0
This command downloads the entire repository, including all necessary files and directories.​

Access the Downloaded Model Files:

Navigate to the cloned directory:​
cd stable-diffusion-xl-base-1.0
The model files, including sd_xl_base_1.0.safetensors, will be available in this directory.​

Alternative: Manual Download via Web Browser: If you prefer not to use Git, you can manually download the model files:

Visit the Model Repository Page:

Go to the Stable Diffusion XL Base 1.0 repository.​

Download the Model File:

Navigate to the "Files and versions" section.​
Locate the sd_xl_base_1.0.safetensors file.​

Click on the file to open it, then click the "Download" button to save it to your local machine.​

Note: The model file is substantial in size (approximately 6.94 GB), so ensure you have sufficient storage space and a stable internet connection.​

Second Alternative: 
1. Go to - https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/tree/main
2. Click 'Use This Model', then click on 'Diffusers' like shown below in image

![image](https://github.com/user-attachments/assets/6c1f3a32-0dd6-4dc3-923d-21ac9e7594d0)

3. Click 'Copy'

![image](https://github.com/user-attachments/assets/598bb105-df21-46c2-b9ea-301d92b36a3d)

4. Run this code in you PyCharm environment or VS Code Environment and it will download the model into onto your computer in C:\Users\<your username>\.cache\huggingface\hub
5. Copy the model into your 'Model' folder in your project.
 
Notes
Model Path: Update the model_path_sdxl variable in Local_Diffusion_Model_Image_Generator.py to point to the correct location of your Stable Diffusion XL model files.​

For more detailed information about the model and its usage, refer to the official model card on Hugging Face.

Run the Application:
Go to directory in Terminal
streamlit run Local_Diffusion_Model_Image_Generator.py

Generate Images:

1. Enter a descriptive prompt in the provided text box.​
2. Select the number of images to generate using the slider.​
3. Click the "Generate Image" button to initiate the process.​
4. Generated images will be displayed in pairs with a progress bar indicating completion status.​

Notes
Model Path: Update the model_path_sdxl variable in Local_Diffusion_Model_Image_Generator.py to point to the correct location of your Stable Diffusion XL model files.​

Performance: Image generation speed and quality depend on your hardware capabilities. Using a GPU with sufficient VRAM will significantly enhance performance.​

Error Handling: Ensure all dependencies are correctly installed and compatible. Refer to the documentation of each library for troubleshooting assistance.​

Acknowledgments
This project utilizes the Stable Diffusion XL model and leverages the capabilities of the Streamlit library for the user interface.​

![image](https://github.com/user-attachments/assets/709b379c-9fde-42a5-b4e8-098299d3944c)

![image](https://github.com/user-attachments/assets/34c5aeb0-0e5e-46f7-9b67-1e157a2d71e5)

![image](https://github.com/user-attachments/assets/84ac61b2-9495-431d-a0d1-47c1b3fc0a56)

![image](https://github.com/user-attachments/assets/d413e495-75a7-4378-90d3-06713b48bd9d)





