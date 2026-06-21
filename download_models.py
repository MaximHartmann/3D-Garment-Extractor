from huggingface_hub import hf_hub_download
import os

os.makedirs("checkpoints", exist_ok=True)

repo_id = "yuxuanx/human3diffusion"

hf_hub_download(repo_id=repo_id, filename="model.safetensors", local_dir="checkpoints")
hf_hub_download(repo_id=repo_id, filename="model_1.safetensors", local_dir="checkpoints")
hf_hub_download(repo_id=repo_id, filename="pifuhd.pt", local_dir="checkpoints")