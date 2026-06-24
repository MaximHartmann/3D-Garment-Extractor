#!/bin/bash

echo "🧹 1. Bereinige requirements..."
grep -v "^-e" requirements_cluster_exact.txt > requirements_clean.txt

echo "🚀 2. Starte Singularity für das finale Setup..."
singularity exec --nv docker://pytorch/pytorch:2.1.0-cuda12.1-cudnn8-devel bash -c "
    echo '📦 Erstelle frisches Environment (.venv_final)...'
    python -m venv .venv_final
    source .venv_final/bin/activate

    echo '📥 Installiere exakte Pip-Pakete...'
    pip install -r requirements_clean.txt

    echo '🔧 Repariere GLM Mathe-Bibliothek...'
    rm -rf src/gaussian-opacity-fields/submodules/diff-gaussian-rasterization/third_party/glm
    git clone https://github.com/g-truc/glm.git src/gaussian-opacity-fields/submodules/diff-gaussian-rasterization/third_party/glm

    echo '🔨 Kompiliere Rasterizer...'
    pip install -e src/gaussian-opacity-fields/submodules/diff-gaussian-rasterization/ --no-build-isolation

    echo '🔨 Kompiliere Simple-KNN...'
    pip install -e src/gaussian-opacity-fields/submodules/simple-knn/ --no-build-isolation
"

echo "✅ Alles fertig installiert in '.venv_final'."
