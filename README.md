# 3D-Garment-Extractor

This repository provides an automated pipeline to extract 3D garments (Gaussian Splats) from standard RGB images, configured for the TCML cluster environment.

* **Stage 1 (Human3Diffusion):** Generates a full-body 3D mesh from a single 2D image using Singularity and `uv`.
* **Stage 2 (CloSeNet):** Automatically segments the generated 3D human body and extracts specific clothing items into clean `.ply` meshes using Conda.

## Workflow Instructions

### 1. Resource Allocation
Log in to the TCML cluster and request a node with sufficient VRAM (e.g., A4000) to ensure the model can run without out-of-memory errors:

```bash
salloc --partition=day --gres=gpu:A4000:1 --mem=32G --cpus-per-task=4 --time=02:00:00
srun --pty /bin/bash
```

### 2. Setup
Clone the repository and enter the directory:

```bash
git clone [https://github.com/MaximHartmann/3D-Garment-Extractor.git](https://github.com/MaximHartmann/3D-Garment-Extractor.git)
cd 3D-Garment-Extractor
```

## 2a: Initialize Stage 1 (Human3Diffusion)
Execute the setup script to initialize the virtual environment, compile necessary submodules, and download the required pre-trained models:

```bash
./setup.sh
```

## 2b: Initialize Stage 2 (CloSeNet)
Create the isolated Conda environment for the segmentation model and download the pre-trained weights:

```bash
cd src/CloSe
conda env create -f environment_close.yml
wget -O pretrained/closenet.pth [https://github.com/anticdimi/CloSe/raw/main/pretrained/closenet.pth](https://github.com/anticdimi/CloSe/raw/main/pretrained/closenet.pth)
cd ../..
```

### 3. Running Inference
Place your input images in the test_imgs/ folder. Execute the inference pipeline:

```bash
./run_inference.sh
```

### 4. Output
Once the process is complete, you will find the results in two locations:

- Full Body Scans: output/test/tsdf-rgbd.ply
- Extracted Garments: src/CloSe/out/demo_scan_out/ (Contains individual meshes like mesh_TShirt.ply, mesh_Pants.ply, etc.)

output/test/