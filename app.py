from flask import Flask, request, jsonify
from flask_cors import CORS
from diffusers import StableDiffusionPipeline
import torch
import os
from huggingface_hub import login

app = Flask(__name__)
CORS(app)

# Optional: load token (even if model is public, avoids gated/LFS issues)
hf_token = os.getenv("HF_TOKEN")
if hf_token:
    login(token=hf_token)

pipe = StableDiffusionPipeline.from_pretrained(
    "yohuj/my-model-name",
    torch_dtype=torch.float32,
    use_auth_token=hf_token  # even if public, makes LFS access smoother
)
