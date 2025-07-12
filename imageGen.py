# -*- coding: utf-8 -*-
#"This file is part of DayDreamer.

!pip install diffusers transformers accelerate --upgrade
!pip install safetensors

import torch
from diffusers import StableDiffusionPipeline
import matplotlib.pyplot as plt

from huggingface_hub import login
login("HF_TOKEN")

pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    torch_dtype=torch.float16,
    use_safetensors=True
).to("cuda")

user_prompt = input("Enter your image prompt: ")
image = pipe(user_prompt).images[0]

plt.imshow(image)
plt.axis('off')
plt.show()

!pip install flask flask-cors

!ngrok config add-authtoken ngrok_config_addauthtoken

from pyngrok import ngrok
public_url = ngrok.connect(5000)
print("🔗 Public URL:", public_url)

!pip install flask-cors

# 🧠 Add this cell to define and run Flask API

from flask import Flask, request, jsonify
from flask_cors import CORS
import io
import base64
from PIL import Image


app = Flask(__name__)
CORS(app)  # ← this line is required
CORS(app, resources={r"/generate": {"origins": "*"}})



@app.route('/generate', methods=['POST'])
def generate_image():
    data = request.get_json()
    prompt = data.get("prompt", "")

    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400

    try:
        image = pipe(prompt).images[0]
        buffer = io.BytesIO()
        image.save(buffer, format="PNG")
        image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
        return jsonify({"image": f"data:image/png;base64,{image_base64}"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

app.run(host='0.0.0.0', port=5000)

