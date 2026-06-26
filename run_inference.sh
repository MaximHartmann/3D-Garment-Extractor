#!/bin/bash
export PYTORCH_CUDA_ALLOC_CONF=max_split_size_mb:128

echo "Starting 2D to 3D Generation..."


singularity exec --nv docker://pytorch/pytorch:2.1.0-cuda12.1-cudnn8-devel bash -c "
    export PYTHONPATH=\$PWD/.venv/lib/python3.10/site-packages:\$PYTHONPATH
    python src/Human3Diffusion/infer.py --test_imgs test_imgs --output output
"

echo "Starting TSDF mesh extraction"

singularity exec --nv docker://pytorch/pytorch:2.1.0-cuda12.1-cudnn8-devel bash -c "
    export PYTHONPATH=\$PWD/.venv/lib/python3.10/site-packages:\$PYTHONPATH
    python src/Human3Diffusion/infer_mesh.py --test_imgs test_imgs --output output --mesh_quality low
"

echo "Starting 3D Garment Segmentation..."

source ~/miniconda3/etc/profile.d/conda.sh
conda activate close
cd src/CloSe
echo "Preparing mesh for segmentation..."
python create_npz.py
echo "Running CloSeNet inference..."
python demo.py --scan_path my_scan.npz
echo "Extracting final garments..."
python extract_garment.py
cd ../..
echo "Done!"