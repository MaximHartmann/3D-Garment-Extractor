#!/bin/bash
uv sync
rm -rf src/gaussian-opacity-fields/submodules/diff-gaussian-rasterization/third_party/glm
git clone https://github.com/g-truc/glm.git src/gaussian-opacity-fields/submodules/diff-gaussian-rasterization/third_party/glm
singularity exec --nv docker://pytorch/pytorch:2.1.0-cuda12.1-cudnn8-devel bash -c "
    source .venv/bin/activate
    export CPATH=\$PWD/src/gaussian-opacity-fields/submodules/diff-gaussian-rasterization/third_party/glm:\$CPATH
    pip install -e src/gaussian-opacity-fields/submodules/diff-gaussian-rasterization/ --no-build-isolation
    pip install -e src/gaussian-opacity-fields/submodules/simple-knn/ --no-build-isolation
    pip install pycuda
"
source .venv/bin/activate
python download_models.py
echo "Setup complete. Please run './run_inference.sh' to generate results."
