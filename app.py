from flask import Flask, request, jsonify
from flask_cors import CORS
from diffusers import StableDiffusionPipeline
import torch
import io
import base64
from PIL import Image
from pathlib import Path


# Initialize Flask app
app = Flask(__name__)
CORS(app, resources={r"/generate": {"origins": "*"}})


model_path = Path("backend/my_model").resolve()
# Load your locally saved model
pipe = StableDiffusionPipeline.from_pretrained(
    str(model_path),  # ✅ Convert to string
    torch_dtype=torch.float32
)


# Set device
device = "cuda" if torch.cuda.is_available() else "cpu"
pipe.to(device)

# Define route
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

# Run server
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
