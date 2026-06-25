# 3D-Garment-Extractor

This repository provides an automated pipeline to extract 3D garments (Gaussian Splats) from standard RGB images, configured for the TCML cluster environment.

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

Execute the setup script to initialize the virtual environment, compile necessary submodules, and download the required pre-trained models:

```bash
./setup.sh
```

### 3. Running Inference
Place your input images in the test_imgs/ folder. Execute the inference pipeline:

```bash
./run_inference.sh
```

### 4. Output
Once the process is complete, you can find the generated 3D models (gs.ply) and corresponding renderings in the following directory:

output/test/