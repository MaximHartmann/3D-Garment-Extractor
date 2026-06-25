#!/bin/bash
export PYTORCH_CUDA_ALLOC_CONF=max_split_size_mb:128
singularity exec --nv docker://pytorch/pytorch:2.1.0-cuda12.1-cudnn8-devel bash -c "
    source .venv/bin/activate
    python src/Human3Diffusion/infer.py --test_imgs test_imgs --output output
"
